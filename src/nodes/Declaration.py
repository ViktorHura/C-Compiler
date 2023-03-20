from .Node import *

class Declaration(Node):
    def __init__(self):
        super().__init__()

    def getLabel(self):
        return "Declaration"

    def getIdentifier(self):
        return self.m_children[1].id

    def hasInit(self):
        return self.m_children[1].hasInit()

    def acceptVisitor(self, visitor):
        visitor.enterDeclaration(self)
        for child in self.m_children:
            child.acceptVisitor(visitor)
        visitor.exitDeclaration(self)