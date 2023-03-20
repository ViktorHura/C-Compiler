from src.Type import *

import random
import struct

REGISTERS = {
    't': 10,
    's': 8,
    'a': 4,
    'v': 2,
    'f': 31
}

FLOAT_INSTRUCTIONS = {
    '+': 'add.s',
    '-': 'sub.s',
    '*': 'mul.s',
    '/': 'div.s',
}

SIGNED_INT_INSTRUCTIONS = {
    '+': 'add',
    '-': 'sub',
    '*': 'mul',
    '/': 'div',
    '%': 'rem',
    '==': 'seq',
    '!=': 'sne',
    '<': 'slt',
    '>': 'sgt',
    '<=': 'sle',
    '>=': 'sge'
}

UNSIGNED_INT_INSTRUCTIONS = {
    '+': 'addu',
    '-': 'subu',
    '*': 'mulu',
    '/': 'divu',
    '%': 'remu',
    '==': 'seq',
    '!=': 'sne',
    '<': 'sltu',
    '>': 'sgtu',
    '<=': 'sleu',
    '>=': 'sgeu'
}

BOOL_INSTRUCTIONS = {
    '&&': 'and',
    '||': 'or'
}

PRINTF_SYSCALLS = {
    'd': 1,
    's': 1,
    'p': 1,
    'f': 2,
    's': 4,
    'c': 11
}

SCANF_SYSCALLS = {
    'd': 5,
    's': 5,
    'p': 5,
    'f': 6,
    's': 8,
    'c': 12
}

class MIPSContext:
    def __init__(self):
        self.data = []
        self.text = []

        self.locals = dict()
        self.globals = dict()

        self.active_registers = dict()

        self.symbol_table = None

        # init queue
        self.register_queue = dict()
        for register_type in REGISTERS.keys():
            self.register_queue[register_type] = 0
            
        self.offset = 0
        self.offsets = []
        self.global_offset = 0

    def toString(self):
        res = '\t.data\n'
        for line in self.data:
            res += line + '\n'
        
        res += '\n\t.text\n\tmove $fp, $sp\n'
        for line in self.text:
            res += line + '\n'

        return res

    def addString(self, string: str):
        label = f'str_{len(self.data)}'
        self.data.append(f'{label}: .asciiz "{string}"')
        return label

    def addInstruction(self, instruction: str):
        self.text.append(f'\t{instruction}')

    def addStoreInstruction(self, val_reg: 'MIPSValue', addr_reg):
        addr = addr_reg if isinstance(addr_reg, str) else f'0({addr_reg.getRegister()})'
        if val_reg.isFP():
            self.addInstruction(f'swc1 {val_reg.getRegister()} {addr}')
        else:
            self.addInstruction(f'sw {val_reg.getRegister()} {addr}')

    def addLoadInstruction(self, addr_reg, is_float: bool = False) -> 'MIPSValue':
        addr = addr_reg if isinstance(addr_reg, str) else f'0({addr_reg.getRegister()})'
        if is_float:
            result = self.getFloatTemp()
            self.addInstruction(f'lwc1 {result.getRegister()} {addr}')
        else:
            result = self.getTemp()
            self.addInstruction(f'lw {result.getRegister()} {addr}')
        
        return result

    def addLabel(self, label: str):
        self.text.append(f'{label}:')

    def addComment(self, commend: str):
        self.text.append(f'\t#{commend}')

    def startFunction(self, identifier: str, nargs: int):
        self.text.append('\n########################################################################')
        self.text.append(f'# ---> FUNCTION')
        self.addLabel(identifier)
        
        to_store = ['$fp', '$ra']
        for r in ['s']:
            for i in range(REGISTERS[r]):
                to_store.append(f'${r}{i}')
        
        self.offsets.append(self.offset)
        self.offset = -4*nargs
        for i, r in enumerate(to_store):
            self.addInstruction(f'sw {r}, {self.offset - 4*i}($sp)')

        self.addInstruction('move $fp, $sp')
        self._get_next_offset(len(to_store)+1)
        
    def endFunction(self, identifier: str, nargs: int):
        self.addLabel(f'{identifier}_end')

        self.addInstruction('move $sp, $fp')

        to_store = ['$fp', '$ra']
        for r in ['s']:
            for i in range(REGISTERS[r]):
                to_store.append(f'${r}{i}')
        
        for i, r in enumerate(to_store):
            self.addInstruction(f'lw {r}, {-4*nargs - 4*i}($sp)')

        self.addInstruction('jr $ra')
        self.text.append(f'# <--- FUNCTION')
        self.text.append('########################################################################\n')

        self.offset = self.offsets.pop()

    def loadImmediate(self, value, value_type: str):
        if value_type == 's':
            reg = self.getTemp()
            label = self.addString(value)
            self.addInstruction(f'la {reg.getRegister()}, {label}')
            return reg
        elif value_type == 'f':
            reg = self.getTemp()
            freg = self.getFloatTemp()
            val = hex(struct.unpack('<I', struct.pack('<f', value))[0])
            self.addInstruction(f'li {reg.getRegister()}, {val}')
            self.addInstruction(f'mtc1 {reg.getRegister()}, {freg.getRegister()}')
            reg.release()
            return freg
        else:
            reg = self.getTemp()
            self.addInstruction(f'li {reg.getRegister()}, {value}')
            return reg


    def getTemp(self):
        return MIPSValue(self, 's')

    def getFloatTemp(self):
        return MIPSValue(self, 'f')

    def getRegister(self, name):
        self._release_register(name)
        return MIPSValue(self, name[1], name)

    def saveActiveRegister(self, register_type: str):
        for name, reg in self.active_registers.items():
            if name[1] == register_type:
                reg._store_value()

    def createLocal(self, lvalue_id : str, size: int = 1):
        offset = self._get_next_offset(size)
        self.locals[lvalue_id] = offset
        return self.getLValueAddress(lvalue_id)

    def createGlobal(self, lvalue_id: str, size: int = 1):
        offset = self.global_offset
        self.global_offset -= 4*size
        self.globals[lvalue_id] = offset
        return self.getLValueAddress(lvalue_id)

    def createParam(self, lvalue_id: str, n: int):
        self.locals[lvalue_id] = -4*n
        return self.getLValueAddress(lvalue_id)


    def getLValueAddress(self, lvalue_id: str):
        if lvalue_id in self.locals:
            return f'{self.locals[lvalue_id]}($fp)'
        elif lvalue_id in self.globals:
            return f'{self.globals[lvalue_id]}($gp)'
        else:
            return None 

    @staticmethod
    def getInstruction(op, typ):
        if op in ['&&', '||']:
            return BOOL_INSTRUCTIONS[op]
        elif typ.isFP():
            return FLOAT_INSTRUCTIONS.get(op)
        else:
            return SIGNED_INT_INSTRUCTIONS[op]

    @staticmethod
    def getPrintSyscall(fmt: str) -> int:
        return PRINTF_SYSCALLS[fmt]

    @staticmethod
    def getScanSyscall(fmt: str) -> int:
        return SCANF_SYSCALLS[fmt]

    #######################################################################
    ### mips context internals, should not be called from inside a Node ###
    #######################################################################

    def _get_available_register(self, register_type: str) -> str:
        """ Returns a register name that is not in use. If you wish to use this register, you should register immediately. """
        # search for free register
        for i in range(REGISTERS[register_type]):
            reg = f'${register_type}{i}'
            if reg not in self.active_registers:
                return reg

        # recycle random register if no free was found
        reg = f'${register_type}{self.register_queue[register_type]}'
        self.register_queue[register_type] = (self.register_queue[register_type] + 1) % REGISTERS[register_type]
        self._release_register(reg)
        return reg

    def _claim_register(self, register: str, value):
        """ Claim the register so it can put it's value on the stack if it needs to. """
        assert register not in self.active_registers

        self.active_registers[register] = value

    def _release_register(self, register: str, persist: bool = True):
        """ Release the register so another value can use it (if persist is True, the previous value is pushed on the stack first). """
        
        # remove register from active registers
        prev_value = self.active_registers.pop(register, None)

        # persist value on stack 
        if persist and prev_value:
            prev_value._store_value()

    def _get_next_offset(self, size: int = 1):
        """ Get next stack offset and increase the stack pointer. """
        result = self.offset
        self.offset -= 4 * size
        self.addInstruction(f'subu $sp, $sp, {4*size}')
        return result
        
    
class MIPSValue:
    def __init__(self, context: MIPSContext, register_type: str, register = None):
        self.context = context
        self.type = register_type
        self.offset = None

        if register is None:
            self.register = self.context._get_available_register(self.type)
        else:
            self.register = register

        self.context._claim_register(self.register, self)

    def release(self):
        """ Release this register. It should not be used after this. """

        # release register if it's active
        if self.register is not None:
            self.context._release_register(self.register, False)
            self.register = None

        # forget about stack
        self.offset = None

    def getRegister(self):
        """ Get register for this value """
        assert self.register is not None or self.offset is not None

        # load the value from the stack if it's not in a register
        if self.register is None:
            self._load_value()

        return self.register

    def isFP(self) -> bool:
        return self.type == 'f'

    ### Internals

    def _load_value(self):
        """ Load value from stack and claim register """
        assert self.register is None

        # claim register
        self.register = self.context._get_available_register(self.type)
        self.context._claim_register(self.register, self)

        # load value from stack
        if self.type == 'f':
            self.context.addInstruction(f'lwc1 {self.register}, {self.offset}($fp)')
        else:
            self.context.addInstruction(f'lw {self.register}, {self.offset}($fp)')

    def _store_value(self):
        """ Store value on stack and give up register"""
        assert self.register is not None

        # reserve place on stack
        if self.offset is None:
            self.offset = self.context._get_next_offset()

        # store value on stack (or refresh if it is already there)
        if self.type == 'f':
            self.context.addInstruction(f'swc1 {self.register}, {self.offset}($fp)')
        else:
            self.context.addInstruction(f'sw {self.register}, {self.offset}($fp)')
        
        # give up register
        self.register = None

