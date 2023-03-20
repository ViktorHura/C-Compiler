from src.nodes import *

class ASTVisitor: # abstract visitor for an AST
    def enterNode(self, node: Node):
        pass
    def exitNode(self, node: Node):
        pass

    def enterLiteral(self, node : Literal):
        pass
    def exitLiteral(self, node: Literal):
        pass

    def enterDeclaration(self, node: Declaration):
        pass
    def exitDeclaration(self, node: Declaration):
        pass

    def enterTypeSpecifier(self, node: TypeSpecifier):
        pass
    def exitTypeSpecifier(self, node: TypeSpecifier):
        pass

    def enterDeclarator(self, node: Declarator):
        pass
    def exitDeclarator(self, node: Declarator):
        pass

    def enterBlock(self, node: Block):
        pass
    def exitBlock(self, node: Block):
        pass

    def enterConversion(self, node: Conversion):
        pass

    def exitConversion(self, node: Conversion):
        pass

    def enterBinaryOperation(self, node: BinaryOperation):
        pass

    def exitBinaryOperation(self, node: BinaryOperation):
        pass

    def enterUnaryOperation(self, node: UnaryOperation):
        pass

    def exitUnaryOperation(self, node: UnaryOperation):
        pass

    def enterAssignment(self, node: Assignment):
        pass

    def exitAssignment(self, node: Assignment):
        pass

    def enterVariable(self, node: Variable):
        pass

    def exitVariable(self, node: Variable):
        pass

    def enterConstruct(self, node: Construct):
        pass

    def exitConstruct(self, node: Construct):
        pass

    def enterJump(self, node: Jump):
        pass

    def exitJump(self, node: Jump):
        pass

    def enterFunctionParameter(self, node: FunctionParameter):
        pass

    def exitFunctionParameter(self, node: FunctionParameter):
        pass

    def enterFunction(self, node: Function):
        pass

    def exitFunction(self, node: Function):
        pass

    def enterFunctionCall(self, node: FunctionCall):
        pass

    def exitFunctionCall(self, node: FunctionCall):
        pass