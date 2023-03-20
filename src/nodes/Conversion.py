from .Node import *
from src.Type import *


class Conversion(Node):
    def __init__(self, from_type, to_type):
        super().__init__()
        self.from_type = from_type
        self.type = to_type
        self.explicit = False

    def getFromType(self):
        return self.from_type

    def getToType(self):
        return self.getType()

    def isExplicit(self):
        return self.explicit

    def setExplicit(self):
        self.explicit = True

    def setFromType(self, typ):
        self.from_type = typ

    def getLabel(self):
        return "{} -> {}".format(self.getFromType(), self.getToType())

    def acceptVisitor(self, visitor):
        visitor.enterConversion(self)
        for child in self.m_children:
            child.acceptVisitor(visitor)
        visitor.exitConversion(self)

    def generateLLVM(self, context):
        # get types
        from_type = self.getFromType()
        to_type = self.getToType()
        arg = self.getChild(0).generateLLVM(context)

        # do conversion
        result = context.addConversion(arg, from_type, to_type)

        return result if result is not None else arg

    def generateMIPS(self, context):
        # get types
        from_type = self.getFromType()
        to_type = self.getToType()

        # compute child and get register
        arg = self.getChild(0).generateMIPS(context)
        reg = arg.getRegister()

        # need to handle:
        # int/bool -> float
        # float -> int
        # int -> bool
        # float -> bool
        if from_type.isFP():
            if to_type.isFP():
                return arg
            elif to_type == Type(CType.BOOL):
                result = context.getTemp()
                context.addInstruction(f'li {result.getRegister()}, 1')
                context.addInstruction(f'c.eq.s {reg}, $f31')
                context.addInstruction(f'movt {result.getRegister()}, $zero')
                arg.release()
                return result
            else:
                result = context.getTemp()
                context.addInstruction(f'cvt.w.s {reg}, {reg}')
                context.addInstruction(f'mfc1 {result.getRegister()}, {reg}')
                arg.release()
                return result
        else:
            if to_type.isFP():
                result = context.getFloatTemp()
                context.addInstruction(f'mtc1 {reg}, {result.getRegister()}')
                context.addInstruction(f'cvt.s.w {result.getRegister()}, {result.getRegister()}')
                arg.release()
                return result
            elif to_type == Type(CType.BOOL):
                result = context.getTemp()
                context.addInstruction(f'sne {result.getRegister()}, {reg}, $zero')
                arg.release()
                return result 
            else:
                return arg


