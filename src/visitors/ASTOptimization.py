from .ASTVisitor import *
from copy import deepcopy

class ASTReachableDecorator(ASTVisitor):

    def statement(self, node):
        if node.getLeftSiblingIfExists() is not None:
            predec = node.getLeftSiblingIfExists()
            node.reachable = predec.reachable and predec.terminating_normal
        else:
            node.reachable = node.getParent().reachable

    def enterLiteral(self, node: Literal):
        self.statement(node)

    def enterDeclarator(self, node: Declarator):
        self.statement(node)

    def enterBlock(self, node: Block):
        if node.getParent() is None:
            node.reachable = True
        elif isinstance(node.getParent(), Function):
            node.reachable = True
        elif (node.getLeftSiblingIfExists() is not None and
              not isinstance(node.getParent(), Construct)):
            predec = node.getLeftSiblingIfExists()
            node.reachable = predec.reachable and predec.terminating_normal

        if node.reachable and node.getChildrenCount() > 0:
            node.getChild(0).reachable = True

    def exitBlock(self, node: Block):
        if node.getChildrenCount() > 0:
            node.terminating_normal = node.getChild(-1).terminating_normal

    def enterConversion(self, node: Conversion):
        node.reachable = node.getParent().reachable
        node.getChild(0).reachable = node.reachable

    def enterBinaryOperation(self, node: BinaryOperation):
        self.statement(node)

    def enterUnaryOperation(self, node: UnaryOperation):
        self.statement(node)

    def enterAssignment(self, node: Assignment):
        self.statement(node)

    def enterVariable(self, node: Variable):
        self.statement(node)

    def enterConstruct(self, node: Construct):
        self.statement(node)
        for c in node.m_children:
            c.reachable = node.reachable

    def exitConstruct(self, node: Construct):
        #if node.getChildrenCount() > 0:
        #   node.terminating_normal = node.getChild(-1).terminating_normal
        pass

    def enterJump(self, node: Jump):
        node.terminating_normal = False

        self.statement(node)

    def exitFunction(self, node: Function):
        node.reachable = True
        for c in node.m_children:
            c.reachable = node.reachable

    def enterFunctionCall(self, node: FunctionCall):
        self.statement(node)


class ASTUnreachablePruner(ASTVisitor):
    @staticmethod
    def prune(node):
        if node.getChildrenCount() == 0:
            return

        newchilds = []
        for c in node.m_children:
            if c.reachable:
                newchilds.append(c)
        node.m_children = newchilds

        for c in node.m_children:
            ASTUnreachablePruner.prune(c)

class ASTConstantPropagation(ASTVisitor):
    def enterVariable(self, node: Variable):
        if node.getType().isConstant():
            if not isinstance(node.getParent(), Assignment):
                declarator = node.getSymbolTable().lookUp(node.getValue())
                assignment = declarator.getRightSiblingIfExists()
                if not isinstance(assignment, Assignment):
                    return

                value = deepcopy(assignment.getChild(1))
                node.getParent().replaceChild(node, value)

class ASTUnusedVariableFinder(ASTVisitor):
    def __init__(self):
        self.seen_vars = {}

    def enterDeclarator(self, node: Declarator):
        name = node.getIdentifier()
        # no this is not at all efficient way to get the table, too bad
        dec, table = node.findFirstNode(Block).getSymbolTable().lookUpAndGet(name)
        if dec != node:
            raise Exception("declarator not in any symbol table?")

        var_id = name + str(id(table))
        self.seen_vars[var_id] = 0

    def enterVariable(self, node: Variable):
        dec = node.getSymbolTable().lookUp(node.getValue())
        if isinstance(dec, FunctionParameter):
            return

        var_id = node.getValue() + str(id(node.getSymbolTable()))
        seen = self.seen_vars[var_id]
        parent = node.getParent()
        if isinstance(parent, Assignment) and parent.isExplicit():
            return

        self.seen_vars[var_id] = seen + 1


class ASTUnusedVariablePruner(ASTVisitor):
    def __init__(self, vars):
        self.seen_vars = vars

    def prune(self, node):
        if node.getChildrenCount() == 0:
            return

        newchilds = []
        for c in node.m_children:
            if isinstance(c, Declarator) and not isinstance(c, FunctionParameter):
                name = c.getIdentifier()
                # no this is not at all efficient way to get the table, too bad
                dec, table = c.findFirstNode(Block).getSymbolTable().lookUpAndGet(name)
                if dec != c:
                    raise Exception("declarator not in any symbol table?")

                var_id = name + str(id(table))

                if self.seen_vars[var_id] == 0:
                    table.remove(name)
                    sibling = c.getRightSiblingIfExists()
                    if isinstance(sibling, Assignment) and sibling.isExplicit():
                        node.destroyChild(sibling)
                else:
                    newchilds.append(c)
            else:
                newchilds.append(c)
        node.m_children = newchilds

        for c in node.m_children:
            self.prune(c)


class ASTUnusedConditionals(ASTVisitor):

    def exitConstruct(self, node: Construct):
        if node.getValue() == "selection":
            condition = node.getChild(0)

            if isinstance(condition, Literal):
                if condition.getValue() != 0:  # True
                    node.getParent().replaceChild(node, node.getChild(1))
                else:
                    if node.getChildrenCount() == 2:
                        node.getParent().replaceChild(node, Node())
                    else:
                        node.getParent().replaceChild(node, node.getChild(2))

    @staticmethod
    def prune(node):
        if node.getChildrenCount() == 0:
            return

        newchilds = []
        for c in node.m_children:
            if not type(c) is Node:
                newchilds.append(c)
        node.m_children = newchilds

        for c in node.m_children:
            ASTUnusedConditionals.prune(c)
