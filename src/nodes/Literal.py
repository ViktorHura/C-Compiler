from .Node import *


class Literal(Node):
    def __init__(self, value, typ, signed:bool=True):
        super().__init__()

        self.m_value = value
        self.type = typ
        self.signed = signed

    def getValue(self):
        return self.m_value

    def isSigned(self):
        return self.signed

    def getLabel(self):
        return '{} Literal: {}'.format(self.type, self.m_value)

    def acceptVisitor(self, visitor):
        visitor.enterLiteral(self)
        visitor.exitLiteral(self)

    def isString(self):
        return self.type == Type(CType.CHAR).makePointer()

    def generateLLVM(self, context):
        if self.isString():
            return context.addString(self.m_value)
        else:
            return self.m_value

    def generateMIPS(self, context):
        value_type = 's' if self.isString() else ('f' if self.type.isFP() else 'i')
        return context.loadImmediate(self.getValue(), value_type)
            


