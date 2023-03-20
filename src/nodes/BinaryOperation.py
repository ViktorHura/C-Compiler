from .Node import *
from .Assignment import Assignment
from src.Type import *


class BinaryOperation(Node):
    def __init__(self, operator=""):
        super().__init__()
        self.operator = operator

    def getValue(self):
        return self.operator

    def getLabel(self):
        arg1, arg2 = self.getArgTypes()
        return "{}: {}, {} -> {}".format(self.operator, arg1, arg2, self.getType())

    def getArgs(self):
        return self.getChild(0), self.getChild(1)

    def getArgTypes(self):
        arg1, arg2 = self.getArgs()
        return arg1.getType(), arg2.getType()

    def isBoolean(self):
        return self.operator in ['==', '!=', '<', '>', '<=', '>='] or self.isLogical()

    def isLogical(self):
        return self.operator in ['&&', '||']

    def isArrayOperator(self):
        return self.operator == '[]'

    def acceptVisitor(self, visitor):
        visitor.enterBinaryOperation(self)
        for child in self.m_children:
            child.acceptVisitor(visitor)
        visitor.exitBinaryOperation(self)

    ############
    ### LLVM ###
    ############

    def generateLLVMArrayAccess(self, context, get_value=True):
        child1, child2 = self.getArgs()
        array = child1.generateLLVM(context)
        index = child2.generateLLVM(context)
        array_type = child1.getType().getLLVM()
        index_type = child2.getType().getLLVM()

        result = context.getTemp()
        context.addInstruction(f'{result} = getelementptr {array_type}, {array_type}* {array}, i64 0, {index_type} {index}')

        # get information to insert value in array 
        if not get_value:
            return result

        elememt_type = child1.getType().dereferenceArray().getLLVM()

        new_result = context.getTemp()
        context.addInstruction(f'{new_result} = load {elememt_type}, {elememt_type}* {result}')

        return new_result

    def generateLLVM(self, context):
        if self.isArrayOperator():
            return self.generateLLVMArrayAccess(context, True)
        
        child1, child2 = self.getArgs()
        arg1 = child1.generateLLVM(context)
        arg2 = child2.generateLLVM(context)

        typ = child1.getType().getLLVM()
        instruction = context.getInstruction(self.operator, child1.getType())

        result = context.getTemp()

        context.addInstruction(f'{result} = {instruction} {typ} {arg1}, {arg2}')

        return result

    def generateLLVMAddress(self, context):
        if self.isArrayOperator():
            return self.generateLLVMArrayAccess(context, False)

        return self.generateLLVM(context)

    ############
    ### MIPS ###
    ############

    def generateMIPSArray(self, context, get_value: bool = True):
        child1, child2 = self.getArgs()
        array = child1.generateMIPSAddress(context)
        index = child2.generateMIPS(context)

        addr = context.getTemp()
        context.addInstruction(f'sll {index.getRegister()}, {index.getRegister()}, 2')
        context.addInstruction(f'sub {addr.getRegister()}, {array.getRegister()}, {index.getRegister()}')
        array.release()
        index.release()

        if not get_value:
            return addr
        else:
            result = context.addLoadInstruction(addr, child1.getType().isFP())
            addr.release()
            return result

    def generateMIPS(self, context):
        if self.isArrayOperator():
            return self.generateMIPSArray(context, True)

        typ = self.getType()

        # compute children and get registers
        child1, child2 = self.getArgs()
        arg1 = child1.generateMIPS(context)
        arg2 = child2.generateMIPS(context)
        reg1 = arg1.getRegister()
        reg2 = arg2.getRegister()

        # prepare result register of correct type
        if typ.isFP():
            result = context.getFloatTemp()
        else:
            result = context.getTemp()
        reg = result.getRegister()

        # determine instruction for this operation, depending on type
        instruction = context.getInstruction(self.operator, child1.getType())

        # add instruction
        if instruction is not None: # regular case (for int and arithmetic float oepration)
            context.addInstruction(f'{instruction} {reg}, {reg1}, {reg2}')
        else: # special case for float comparisons
            
            # switch operands (because only < and <= are supported)
            if self.operator in ['>', '>=']:
                reg1, reg2 = reg2, reg1 

            # determine comparison submethods
            if self.operator in ['==', '!=']:
                op = 'eq'
            elif self.operator in ['<', '>']:
                op = 'lt'
            elif self.operator in ['<=', '>=']:
                op = 'le'

            # add instructions to set register depending on the condition flag in c1
            context.addInstruction(f'li {reg}, 1')
            context.addInstruction(f'c.{op}.s {reg1}, {reg2}')
            context.addInstruction(f'movt {reg}, $zero')

            # invert result
            if self.operator != '!=':
                    context.addInstruction(f'not {reg}, {reg}')

        # release intermediate values
        arg1.release()
        arg2.release()

        return result

    def generateMIPSAddress(self, context):
        if self.isArrayOperator():
            return self.generateMIPSArray(context, False)
        else:
            print("Assignment to rvalue")