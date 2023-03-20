from .ASTVisitor import *

class ASTDotVisitor(ASTVisitor):
    def __init__(self, dotStringList, showSymbolTable=True, showReachability=False):
        self.m_dotStringList = dotStringList
        self.symbolTable = showSymbolTable
        self.showReachability = showReachability

    def parseNode(self, node):
        rootString = str(id(node)) # get the unique ID for our root

        reachability = ""
        if self.showReachability:
            reachability = " | " + str(int(node.terminating_normal)) + " " + str(int(node.reachable))

        rootString += " [label=\"" + node.getLabel() + reachability + "\"];" # and add the correct label

        self.m_dotStringList.append(rootString)

        for i, child in enumerate(node.m_children):
            edgeString = f"{id(child)} -> {id(node)} [dir=none,label={i}];"
            self.m_dotStringList.append(edgeString)

    def enterLiteral(self, node : Literal):
        self.parseNode(node)

    def enterNode(self, node: Node):
        self.parseNode(node)

    def enterDeclaration(self, node: Declaration):
        self.parseNode(node)

    def enterDeclarator(self, node: Declarator):
        self.parseNode(node)

    def enterTypeSpecifier(self, node: TypeSpecifier):
        self.parseNode(node)

    def enterBlock(self, node: Block):
        self.parseNode(node)

        if self.symbolTable:
            # draw the symbol table for the block
            tableString = str(id(node.getSymbolTable()))
            tableString += " [shape=record, label = \""

            tableString += node.getSymbolTable().toDot()

            tableString += "\"];"
            self.m_dotStringList.append(tableString)

            # if symbol table has a parent, connect them
            if node.getSymbolTable().parent is not None:
                edgeString = str(id(node.getSymbolTable())) + " -> " + str(id(node.getSymbolTable().parent)) + ";"
                self.m_dotStringList.append(edgeString)

            # connect block to symbol table
            edgeString = str(id(node)) + " -> " + str(id(node.getSymbolTable())) + "[dir=none,style=dashed];"
            self.m_dotStringList.append(edgeString)

    def enterConversion(self, node: Conversion):
        self.parseNode(node)

    def enterBinaryOperation(self, node: BinaryOperation):
        self.parseNode(node)

    def enterUnaryOperation(self, node: UnaryOperation):
        self.parseNode(node)

    def enterAssignment(self, node: Assignment):
        self.parseNode(node)

    def enterVariable(self, node: Variable):
        self.parseNode(node)

    def enterConstruct(self, node: Construct):
        self.parseNode(node)

    def enterJump(self, node: Jump):
        self.parseNode(node)

    def enterFunctionParameter(self, node: FunctionParameter):
        self.parseNode(node)

    def enterFunction(self, node: Function):
        self.parseNode(node)

    def enterFunctionCall(self, node: FunctionCall):
        self.parseNode(node)
