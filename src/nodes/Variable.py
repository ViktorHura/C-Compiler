from .Node import *
from .Assignment import Assignment
from .UnaryOperation import UnaryOperation
from .BinaryOperation import BinaryOperation
from src.Type import *


class Variable(Node):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.scope_table = None

    def getValue(self):
        return self.name

    def getSymbolTable(self):
        return self.scope_table

    def setSymbolTable(self, table):
        self.scope_table = table

    def getLabel(self):
        return '{} Variable: {}'.format(self.getType(), self.name)

    def getID(self):
        return self.scope_table.lookUpDeclarator(self.name).getID()

    def acceptVisitor(self, visitor):
        visitor.enterVariable(self)
        visitor.exitVariable(self)

    ############
    ### LLVM ###
    ############

    def generateLLVM(self, context):
        typ = self.getType().getLLVM()
        register = self.getID()

        prefix = '@' if self.scope_table.isRoot() else '%'
        
        if isinstance(self.getParent(), UnaryOperation) and self.getParent().isAddress():
            result = context.getTemp()
            instr = f'{result} = ptrtoint {typ}* {prefix}{register} to {LLVMType(CType.POINTER)}'
            context.addInstruction(instr)
            return result

        if self.getType().isArray():
            return f'{prefix}{register}'
        
        result = context.getTemp()
        instr = f'{result} = load {typ}, {typ}* {prefix}{register}'
        context.addInstruction(instr)
        return result

    def generateLLVMAddress(self, context):
        prefix = '@' if self.scope_table.isRoot() else '%'
        return f'{prefix}{self.getID()}'

    ############
    ### MIPS ###
    ############

    def generateMIPS(self, context: 'MIPSContext') -> 'MIPSValue':
        if self.getType().isArray():
            return self.generateMIPSAddress(context)
        else:
            return context.addLoadInstruction(context.getLValueAddress(self.getID()), self.getType().isFP())

    def generateMIPSAddress(self, context: 'MIPSContext') -> 'MIPSValue':
        result = context.getTemp()
        address = context.getLValueAddress(self.getID())
        context.addInstruction(f'addi {result.getRegister()}, {address[-4:-1]}, {address[:-5]}')
        return result

        
