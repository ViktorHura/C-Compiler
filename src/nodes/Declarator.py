from .Node import *
from src.Type import *


class Declarator(Node):
    def __init__(self, identifier, typ):
        super().__init__()
        self.identifier = identifier
        self.type = typ

    def makePointer(self, const=False):
        self.type = self.type.makePointer()
        self.type.const = const

    def toArray(self, array_size):
        self.type = self.type.makeArray(array_size)

    def getIdentifier(self):
        return self.identifier

    def getID(self):
        return f'var_{self.identifier}_{id(self)}'

    def getLabel(self):
        return f'Declarator: {self.type} {self.identifier}'

    def hasInit(self):
        return not self.isLeaf()

    def acceptVisitor(self, visitor):
        visitor.enterDeclarator(self)
        for child in self.m_children:
            child.acceptVisitor(visitor)
        visitor.exitDeclarator(self)
