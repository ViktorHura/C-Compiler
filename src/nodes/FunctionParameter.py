from src.nodes import Declarator


class FunctionParameter(Declarator):
    def __init__(self, identifier, typ):
        super().__init__(identifier, typ)

    def getLabel(self):
        return f'Function parameter: {self.type} {self.identifier}'

    def acceptVisitor(self, visitor):
        visitor.enterFunctionParameter(self)
        for child in self.m_children:
            child.acceptVisitor(visitor)
        visitor.exitFunctionParameter(self)