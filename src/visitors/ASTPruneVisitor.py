from .ASTVisitor import *
import copy


class ASTPruneReferenceDereference(ASTVisitor):
    # Will try to simplify * followed by & by eliminating both, will try to match up first then down
    def enterUnaryOperation(self, node: UnaryOperation):
        if node.isAddress():
            up = node.getParent()
            down = node.getChild(0)
            if isinstance(down, UnaryOperation) and down.isDereference():
                up.replaceChild(node, down.getChild(0))
            elif isinstance(up, UnaryOperation) and up.isDereference():
                up.getParent().replaceChild(up, down)
        # replace !a with a == 0
        elif node.getValue() == '!':
            comp = BinaryOperation('==')
            node.replaceSelf(comp)
            comp.pushChild(Literal(0, Type(CType.BOOL)))


class ForLoopContinueFix(ASTVisitor):
    def __init__(self, iteration_expression):
        self.it_exp = iteration_expression
        self.fixed = []

    def exitJump(self, node: Jump):
        if node.getValue() == "continue" and id(node) not in self.fixed:
            index = node.getParent().m_children.index(node)
            node.getParent().insertChild(index, copy.deepcopy(self.it_exp))
            self.fixed.append(id(node))


class ASTPrunePass3(ASTVisitor):

    def __init__(self):
        self.errors = []

    def getErrors(self):
        return self.errors

    def enterFunction(self, node: Function):
        sibling = node.getRightSiblingIfExists()
        if isinstance(sibling, Block):
            node.pushChild(sibling)
            node.getParent().destroyChild(sibling)

    # split assignment from declaration
    def exitDeclaration(self, node : Declarator):
        pos = node.m_parent.m_children.index(node) + 1  # start placing new statements next to the declaration
        for i in reversed(range(1, len(node.m_children))):  # loop through declarators backwards
            declarator = node.getChild(i)
            if len(declarator.m_children) > 0:  # if declarator has children
                asn = Assignment(True)   # create an assignment
                asn.linenr = declarator.linenr

                var = Variable(declarator.getIdentifier())  # create variable
                var.linenr = declarator.linenr

                asn.pushChild(var)  # variable to assignment
                asn.pushChild(declarator.getChild(0))   # declaration moved to assignment

                node.m_parent.insertChild(pos, asn)     # assignment as sibling of this declaration
                declarator.m_children.clear()           # remove assignment from declaration

            elif declarator.getType().isConstant():    # if declarator is constant, it must be initialised at once
                err = "[E] on {}: Const variable must be initialised during declaration: {} ({})".format(node.linenr, declarator.getIdentifier(), declarator.getType())
                self.errors.append(err)

            node.m_parent.insertChild(pos, declarator)

        node.m_parent.destroyChild(node)

    def exitConstruct(self, node: Construct):
        if node.getValue() == 'iteration':
            if node.getChildrenCount() > 2:  # should be a for loop I hope
                parent = node.getParent()
                newblock = Block()  # extra enclosing block
                foundcondition = False  # found the while condition
                new_childs = []  # new children of the construct
                iteration_expression = None
                for i in range(0,len(node.m_children)-1):  # loop through all but last child
                    c = node.m_children[i]
                    if not foundcondition:  # haven't reached the first expression yet
                        # add all declarators and assignments before the construct
                        if isinstance(c, Declarator) or isinstance(c, Assignment):
                            newblock.pushChild(c)
                        else:  # first expression
                            foundcondition = True
                            new_childs.append(c)  # keep it as child of construct
                    else:  # all subsequent expressions go to the end of the iterator block ( should be one or none )
                        node.getChild(-1).pushChild(c)
                        iteration_expression = c

                newblock.pushChild(node)  # finally not forget to add construct to new block
                new_childs.append(node.getChild(-1))  # add the block to the new construct children
                node.m_children = new_childs  # set new children

                # add an extra enclosing block around everything for scoping
                parent.replaceChild(node, newblock)

                # fix up all continue statements so they have the iteration expression right before them
                continueVisitor = ForLoopContinueFix(iteration_expression)
                node.getChild(-1).acceptVisitor(continueVisitor)