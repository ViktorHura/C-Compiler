from .Node import *
from .Assignment import Assignment
from src.Type import *


class UnaryOperation(Node):
    def __init__(self, operator=""):
        super().__init__()
        self.operator = operator

    def getValue(self):
        return self.operator

    def getLabel(self):
        return "{}: {} -> {}".format(self.operator, self.getArgType(), self.getType())

    def getArgType(self):
        return self.getChild(0).getType()

    def isDereference(self):
        return self.operator == '*'

    def isAddress(self):
        return self.operator == '&'

    def isIdentifierOperation(self):
        return self.operator[0:2] in ['++', '--']

    def isBoolean(self):
        return self.operator in ['!']

    def acceptVisitor(self, visitor):
        visitor.enterUnaryOperation(self)
        for child in self.m_children:
            child.acceptVisitor(visitor)
        visitor.exitUnaryOperation(self)

    ############
    ### LLVM ###
    ############

    def generateLLVMIncrDecr(self, context):
        arg_addr = self.getChild(0).generateLLVMAddress(context)
        arg_value = self.getChild(0).generateLLVM(context)
        typ = self.getType().getLLVM()

        new_value = context.getTemp()
        instr = context.getInstruction(self.operator[0], typ)
        context.addInstruction(f'{new_value} = {instr} {typ} {arg_value}, 1')
        context.addInstruction(f'store {typ} {new_value}, {typ}* {arg_addr}')

        # return value before increment
        return arg_value if self.operator[2:] == 'post' else new_value

    def generateLLVM(self, context):
        if self.operator == '*':
            arg = self.getChild(0).generateLLVM(context)
            typ = self.getType().getLLVM()

            result = context.getTemp()
            context.addInstruction(f'{result} = inttoptr {LLVMType(CType.POINTER)} {arg} to {typ}*')

            result2 = context.getTemp()
            context.addInstruction(f'{result2} = load {typ}, {typ}* {result}')
            return result2

        elif self.operator == '-':
            arg = self.getChild(0).generateLLVM(context)
            typ = self.getType().getLLVM()

            result = context.getTemp()

            context.addInstruction(f'{result} = sub {typ} 0, {arg}')
            return result
        elif self.isIdentifierOperation():
            return self.generateLLVMIncrDecr(context)
        else:
            return self.getChild(0).generateLLVM(context)

    def generateLLVMAddress(self, context):
        if self.operator == '*':
            arg = self.getChild(0).generateLLVM(context)
            typ = self.getType().getLLVM()

            result = context.getTemp()
            context.addInstruction(f'{result} = inttoptr {LLVMType(CType.POINTER)} {arg} to {typ}*')
            return result
        
        return self.generateLLVM(context)

    ############
    ### MIPS ###
    ############

    def generateMIPS(self, context):
        if self.operator == '*':
            # get value of child (this register contains a memory address)
            addr = self.getChild(0).generateMIPS(context)

            # load value at memory address
            result = context.addLoadInstruction(addr, self.getType().isFP())
            addr.release()

            return result
        elif self.operator == '&':
            return self.getChild(0).generateMIPSAddress(context)
        elif self.operator == '-':
            arg = self.getChild(0).generateMIPS(context)
            result = context.getTemp()

            context.addInstruction(f'sub {result.getRegister()}, $zero, {arg.getRegister()}')
            arg.release()
            return result
        elif self.isIdentifierOperation():
            return self.generateMIPSIncrDecr(context)
        else:
            return self.getChild(0).generateMIPS(context)

    def generateMIPSAddress(self, context):
        if self.operator == '*':
            # get value of child (will be interpreted as memory address)
            return self.getChild(0).generateMIPS(context)
        else:
            print("Assignment to rvalue")

    def generateMIPSIncrDecr(self, context):
        arg_addr = self.getChild(0).generateMIPSAddress(context)
        arg_value = self.getChild(0).generateMIPS(context)
        typ = self.getType()

        instr = context.getInstruction(self.operator[0], typ)        

        new_value = context.getFloatTemp() if typ.isFP() else context.getTemp()
        context.addInstruction(f'{instr}i {new_value.getRegister()}, {arg_value.getRegister()}, 1')
        context.addStoreInstruction(new_value, arg_addr)

        arg_addr.release()

        # return value before increment
        if self.operator[2:] == 'post':
            new_value.release()
            return arg_value
        else:
            arg_value.release()
            return new_value
