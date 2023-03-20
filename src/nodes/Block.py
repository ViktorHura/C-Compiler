from .Node import *
from .FunctionParameter import FunctionParameter
from .Assignment import Assignment
from .Literal import Literal

class Block(Node):
    def __init__(self, table: 'SymbolTable' = None):
        super().__init__()
        self.scope_table = table  # points to a symbol table

    def getSymbolTable(self):
        return self.scope_table

    def setSymbolTable(self, table):
        self.scope_table = table

    def getLabel(self):
        if self.scope_table is None:
            return "Block with missing scope ówò"
        return "Block"

    def acceptVisitor(self, visitor):
        visitor.enterBlock(self)
        for child in self.m_children:
            child.acceptVisitor(visitor)
        visitor.exitBlock(self)

    def generateLLVM(self, context):
        # globals
        if self.isRoot():
            for decl in self.scope_table.data.values():
                if isinstance(decl, FunctionParameter):
                    continue
                
                identifier = decl.getID()
                typ = decl.getType().getLLVM()
                assign = decl.getRightSiblingIfExists()
                if assign and isinstance(assign, Assignment) and isinstance(assign.getChild(1), Literal):
                    value = assign.getChild(1).getValue()
                else:
                    value = 'zeroinitializer'
                context.addInstruction(f'@{identifier} = global {typ} {value}')
        # locals
        else:
            for decl in self.scope_table.data.values():
                if isinstance(decl, FunctionParameter):
                    if not decl.isFirstChild():
                        identifier = decl.getID()
                        typ = decl.getType().getLLVM()
                        context.addInstruction(f'%{identifier} = alloca {typ}')
                        context.addInstruction(f'store {typ} %p{identifier}, {typ}* %{identifier}')
                else:
                    identifier = decl.getID()
                    typ = decl.getType().getLLVM()
                    context.addInstruction(f'%{identifier} = alloca {typ}')
        

        context.symbol_table = self.scope_table

        for child in self.m_children:
            child.generateLLVM(context)

    def generateMIPS(self, context: MIPSContext):
        # globals
        if self.isRoot():
            for decl in self.scope_table.data.values():
                if isinstance(decl, FunctionParameter):
                    continue
                
                size = 1
                if decl.getType().isArray():
                    size = decl.getType().array_size

                addr = context.createGlobal(decl.getID(), size)

                assign = decl.getRightSiblingIfExists()
                if assign and isinstance(assign, Assignment) and isinstance(assign.getChild(1), Literal):
                    value = assign.getChild(1).getValue()
                    
                    if decl.getType().isFP():
                        lhs = context.loadImmediate(value, 'f')
                        context.addInstruction(f'swc1 {lhs.getRegister()}, {addr}')
                    else:
                        lhs = context.loadImmediate(value, 'i')
                        context.addInstruction(f'sw {lhs.getRegister()}, {addr}')
                    lhs.release()
            
            context.addInstruction('jal main')
            context.addInstruction('li $v0, 10')
            context.addInstruction('syscall')
        # locals
        else:
            paramn = 0
            for decl in self.scope_table.data.values():
                if isinstance(decl, FunctionParameter):
                    if not decl.isFirstChild():
                        identifier = decl.getID()
                        context.createParam(identifier, paramn)
                        paramn += 1
                else:
                    size = 1
                    if decl.getType().isArray():
                        size = decl.getType().array_size

                    context.createLocal(decl.getID(), size)

        context.symbol_table = self.scope_table
        
        for child in self.m_children:
            child.generateMIPS(context)