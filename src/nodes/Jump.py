from .Node import *
from .Construct import Construct
from .Function import Function

class Jump(Node):
    def __init__(self, kind):
        super().__init__()

        self.kind = kind

    def getValue(self):
        return self.kind

    def getLabel(self):
        return self.kind.title()

    def acceptVisitor(self, visitor):
        visitor.enterJump(self)
        for child in self.m_children:
            child.acceptVisitor(visitor)
        visitor.exitJump(self)

    def getParentLoop(self):
        curr = self.m_parent
        while not (isinstance(curr, Construct) and curr.getValue() == 'iteration'):
            curr = curr.m_parent

        return curr

    def getParentFunction(self):
        curr = self.m_parent
        while not isinstance(curr, Function):
            curr = curr.m_parent
        
        return curr

    def generateLLVM(self, context):
        if self.kind == 'break':
            context.addInstruction(f'br label %end{id(self.getParentLoop())}')
            context.getTemp()  # an implicit basic block is generated which takes up a temp value
        elif self.kind == 'continue':
            context.addInstruction(f'br label %start{id(self.getParentLoop())}')
            context.getTemp()  # an implicit basic block is generated which takes up a temp value
        elif self.kind == 'return':
            # void return
            if (self.getChildrenCount() == 0):
                typ = LLVMType(CType.VOID)
                value = ''
            else:
                value = self.getChild(0).generateLLVM(context)
                typ = self.getChild(0).getType().getLLVM()
            context.addInstruction(f'ret {typ} {value}')
            context.getTemp()

    def generateMIPS(self, context):
        if self.kind == 'break':
            context.addInstruction(f'j end{id(self.getParentLoop())}')
        elif self.kind == 'continue':
            context.addInstruction(f'j start{id(self.getParentLoop())}')
        elif self.kind == 'return':
            if self.getChildrenCount() > 0:
                result = self.getChild(0).generateMIPS(context)
                if result.isFP():
                    ret = context.getRegister('$f0')
                    context.addInstruction(f'mov.s {ret.getRegister()}, {result.getRegister()}')
                    ret.release()
                else:
                    ret = context.getRegister('$v0')
                    context.addInstruction(f'move {ret.getRegister()}, {result.getRegister()}')
                    ret.release()
                result.release()
            context.addInstruction(f'j {self.getParentFunction().getID()}_end')
