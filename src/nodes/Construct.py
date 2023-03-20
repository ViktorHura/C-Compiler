from .Node import *
from src.Type import *


class Construct(Node):
    def __init__(self, kind):
        super().__init__()
        self.kind = kind

    def getValue(self):
        return self.kind

    def getLabel(self):
        return f'{self.kind.title()} Construct'

    def acceptVisitor(self, visitor):
        visitor.enterConstruct(self)
        for child in self.m_children:
            child.acceptVisitor(visitor)
        visitor.exitConstruct(self)

    ############
    ### LLVM ###
    ############

    def __generateLLVMSelection(self, context):
        # acquire condition register
        cond = self.getChild(0).generateLLVM(context)
        typ = self.getChild(0).getType()
        cond_bool = context.addConversion(cond, typ, Type(CType.BOOL))
        cond = cond_bool if cond_bool is not None else cond

        i = id(self)

        # if ...
        if len(self.m_children) == 2:
            # branch instruction
            context.addInstruction(f'br i1 {cond}, label %body{i}, label %end{i}')

            # if case
            context.addLabel(f'body{i}')
            self.getChild(1).generateLLVM(context)
            context.addInstruction(f'br label %end{i}')
        # if ... else ...
        else:
            # branch instruction
            context.addInstruction(f'br i1 {cond}, label %body{i}, label %else{i}')

            # if case
            context.addLabel(f'body{i}')
            self.getChild(1).generateLLVM(context)
            context.addInstruction(f'br label %end{i}')
            # else case
            context.addLabel(f'else{i}')
            self.getChild(2).generateLLVM(context)
            context.addInstruction(f'br label %end{i}')

        # mark end of selection statement
        context.addLabel(f'end{i}')

    def __generateLLVMIteration(self, context):
        i = id(self)

        # add start label
        context.addInstruction(f'br label %start{i}')
        context.addLabel(f'start{i}')

        # add condition check
        cond = self.getChild(0).generateLLVM(context)
        context.addInstruction(f'br i1 {cond}, label %body{i}, label %end{i}')

        # add body
        context.addLabel(f'body{i}')
        self.getChild(1).generateLLVM(context)
        context.addInstruction(f'br label %start{i}')

        # add end
        context.addLabel(f'end{i}')

    def generateLLVM(self, context):
        if self.kind == 'selection':
            self.__generateLLVMSelection(context)
        elif self.kind == 'iteration':
            self.__generateLLVMIteration(context)

    ############
    ### MIPS ###
    ############

    def generateMIPS(self, context):
        if self.kind == 'selection':
            self.__generateMIPSSelection(context)
        elif self.kind == 'iteration':
            self.__generateMIPSIteration(context)

    def __generateMIPSSelection(self, context):
        # acquire condition register
        cond = self.getChild(0).generateMIPS(context)
        i = id(self)

        # if ...
        if len(self.m_children) == 2:
            # branch instruction
            context.addInstruction(f'beq {cond.getRegister()}, 1, body{i}')
            context.addInstruction(f'beq {cond.getRegister()}, 0, end{i}')

            # if case
            context.addLabel(f'body{i}')
            self.getChild(1).generateMIPS(context)
            context.addInstruction(f'j end{i}')
        # if ... else ...
        else:
            # branch instruction
            context.addInstruction(f'beq {cond.getRegister()}, 1, body{i}')
            context.addInstruction(f'beq {cond.getRegister()}, 0, else{i}')

            # if case
            context.addLabel(f'body{i}')
            self.getChild(1).generateMIPS(context)
            context.addInstruction(f'j end{i}')
            # else case
            context.addLabel(f'else{i}')
            self.getChild(2).generateMIPS(context)
            context.addInstruction(f'j end{i}')

        # mark end of selection statement
        context.addLabel(f'end{i}')

    def __generateMIPSIteration(self, context):
        i = id(self)

        # add start label
        context.addInstruction(f'j start{i}')
        context.addLabel(f'start{i}')

        # add condition check
        cond = self.getChild(0).generateMIPS(context)
        context.addInstruction(f'beq {cond.getRegister()}, 1, body{i}')
        context.addInstruction(f'beq {cond.getRegister()}, 0, end{i}')

        # add body
        context.addLabel(f'body{i}')
        self.getChild(1).generateMIPS(context)
        context.addInstruction(f'j start{i}')

        # add end
        context.addLabel(f'end{i}')

