from .Node import *
from .Block import Block
from src.Type import *


class Function(Node):
    def __init__(self):
        super().__init__()

    def getLabel(self):
        params = ''
        for p in self.getParams():
            params += f'{p.getType()},'
        return f'{self.getIdentifier()}: {params[0:-1]} -> {self.getType()}'

    def getIdentifier(self):
        return self.getChild(0).getIdentifier()

    def getID(self):
        if self.getIdentifier() == 'main':
            return 'main'
        decl = self.getChild(0)
        return f'func_{decl.getIdentifier()}_{id(decl)}'

    def getParams(self):
        if self.getBlock():
            return self.m_children[1:-1]
        else:
            return self.m_children[1:]

    def getBlock(self):
        child = self.getChild(-1)
        if isinstance(child, Block):
            return child
        else:
            return None

    def acceptVisitor(self, visitor):
        visitor.enterFunction(self)
        for child in self.m_children:
            child.acceptVisitor(visitor)
        visitor.exitFunction(self)

    def getSignature(self, argumentsOnly=False):
        sig = ''
        urange = len(self.m_children) - 1
        if not isinstance(self.getChild(-1), Block):
            urange = urange + 1
        lrange = 0
        if argumentsOnly:
            lrange=1
        for i in range(lrange, urange):
            par = self.getChild(i)
            sig += str(par.getType()) + ","

        if self.getIdentifier() in ['scanf', 'printf']:
            sig += '...'
        return sig

    def generateLLVM(self, context):
        name = self.getIdentifier()
        
        # definition
        if self.getBlock():
            typ = self.getType().getLLVM()
            identifier = self.getID()
            if name == 'main':
                identifier = 'main'

            params = ''
            for p in self.getParams():
                params += f'{p.getType().getLLVM()} %p{p.getID()},'

            context.startFunction(typ, identifier, params[0:-1])

            self.getBlock().generateLLVM(context)
            context.endFunction(typ)
        
        # declare stdio functions
        elif name in ['scanf', 'printf']:
            context.addInstruction(f'declare i32 @{name}(i8*, ...)')

    def generateMIPS(self, context):
        name = self.getIdentifier()
        
        # definition
        if self.getBlock():
            identifier = self.getID()

            params = self.getParams()

            context.startFunction(identifier, len(params))
            self.getBlock().generateMIPS(context)
            context.endFunction(identifier, len(params))