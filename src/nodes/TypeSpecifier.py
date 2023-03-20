from .Node import *
from src.Type import *


class TypeSpecifier(Node):
    def __init__(self, typ: Type):
        super().__init__()
        self.type = typ

    def getLabel(self):
        return f'Type: {self.getType()}'

    def acceptVisitor(self, visitor):
        visitor.enterTypeSpecifier(self)
        for child in self.m_children:
            child.acceptVisitor(visitor)
        visitor.exitTypeSpecifier(self)