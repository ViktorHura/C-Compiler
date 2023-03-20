from .Node import *


class Assignment(Node):
    def __init__(self, explicit=False):
        super().__init__()
        self.explicit = explicit

    def isExplicit(self):
        return self.explicit

    def getLabel(self):
        return "{} Assignment:".format(self.getType())

    def acceptVisitor(self, visitor):
        visitor.enterAssignment(self)
        for child in self.m_children:
            child.acceptVisitor(visitor)
        visitor.exitAssignment(self)

    ############
    ### LLVM ###
    ############

    def generateLLVM(self, context):
        if self.getParent().isRoot():
            return
            
        typ = self.getType().getLLVM()
        lhs = self.getChild(0).generateLLVMAddress(context)
        rhs = self.getChild(1).generateLLVM(context)

        context.addInstruction(f'store {typ} {rhs}, {typ}* {lhs}')

    ############
    ### MIPS ###
    ############

    def generateMIPS(self, context):
        if self.getParent().isRoot():
            return

        addr = self.getChild(0).generateMIPSAddress(context)
        val = self.getChild(1).generateMIPS(context)
        context.addStoreInstruction(val, addr)
        val.release()
        addr.release()
