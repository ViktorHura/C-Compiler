from src.Type import *

floatOp = {
    '+': 'fadd',
    '-': 'fsub',
    '*': 'fmul',
    '/': 'fdiv',
    '%': 'frem',
    '==': 'fcmp oeq',
    '!=': 'fcmp one',
    '<': 'fcmp olt',
    '>': 'fcmp ogt',
    '<=': 'fcmp ole',
    '>=': 'fcmp oge'
}

signedIntOp = {
    '+': 'add',
    '-': 'sub',
    '*': 'mul',
    '/': 'sdiv',
    '%': 'srem',
    '==': 'icmp eq',
    '!=': 'icmp ne',
    '<': 'icmp slt',
    '>': 'icmp sgt',
    '<=': 'icmp sle',
    '>=': 'icmp sge'
}

unsignedIntOp = {
    '+': 'add',
    '-': 'sub',
    '*': 'mul',
    '/': 'udiv',
    '%': 'urem',
    '==': 'icmp eq',
    '!=': 'icmp ne',
    '<': 'icmp ult',
    '>': 'icmp ugt',
    '<=': 'icmp ule',
    '>=': 'icmp uge'
}

logicalOp = {
    '&&': 'and',
    '||': 'or'
}

escapeSequence = {
    'a': '07',
    'b': '08',
    'f': '0C',
    'n': '0A',
    'r': '0D',
    't': '09',
    'v': '0B',
    '\\': '5C',
    '\'': '27',
    '"': '22',
    '?': '3F',
}


class LLVMContext:
    def __init__(self):
        self.code = []
        self.temp = 1
        self.braces = 0
        self.symbol_table = None
        self.strings = 1

    def addString(self, string):
        # @.print_pointer = private unnamed_addr constant [4 x i8] c"%p\\0A\\00", align 1\n

        # convert escape sequences to hex
        idx = 0
        length = 1
        val = ''
        while (idx < len(string)):
            char = string[idx]
            val += char
            if (char == '\\'):
                idx += 1
                val += escapeSequence[string[idx]]
            idx += 1
            length += 1
        val += '\\00'

        name = f'@.str_{self.strings}'
        self.strings += 1
        self.code.insert(0, f'{name} = private unnamed_addr constant [{length} x i8] c"{val}", align 1')

        tmp1 = self.getTemp()
        tmp2 = self.getTemp()
        self.addInstruction(f'{tmp1} = getelementptr inbounds [{length} x i8], [{length} x i8]* {name}, i64 0, i64 0')
        self.addInstruction(f'{tmp2} = ptrtoint i8* {tmp1} to {LLVMType(CType.POINTER)}')
        
        return tmp2

    def addInstruction(self, instruction):
        self.code.append(instruction)

    def addConversion(self, arg, from_type, to_type):
        if from_type.isArray():
            return self.addArrayConversion(arg, from_type)

        llvm_ft = from_type.getLLVM()
        llvm_tt = to_type.getLLVM()

        # get conversion instruction
        instruction = llvm_ft.to(llvm_tt)
        if not instruction:
            return None  # no conversion necessary

        if to_type == Type(CType.BOOL):
            return self.addBoolConversion(arg, from_type)

        # add instruction and result
        result = self.getTemp()
        self.addInstruction(f'{result} = {instruction} {llvm_ft} {arg} to {llvm_tt}')

        # align
        # if to_type.isPointer() and not from_type.isPointer():
        #     result2 = self.getTemp()
        #     factor = int(LLVMType(to_type.getCore()).size / 8)
        #     self.addInstruction(f'{result2} = mul {llvm_tt} {result}, {factor}')
        #     return result2
        
        return result

    def addBoolConversion(self, arg, from_type):
        llvm_ft = from_type.getLLVM()

        # get conversion instruction
        instruction = self.getInstruction('!=', llvm_ft)

        result = self.getTemp()
        self.addInstruction(f'{result} = {instruction} {llvm_ft} {arg}, {0.0 if llvm_ft.isFP() else 0}')
        return result

    def addArrayConversion(self, arg, from_type):
        llvm_ft = from_type.getLLVM()
        llvm_inside = from_type.dereferenceArray().getLLVM()
        temp = self.getTemp()
        result = self.getTemp()
        self.addInstruction(f'{temp} = getelementptr {llvm_ft}, {llvm_ft}* {arg}, i64 0, i64 0')
        self.addInstruction(f'{result} = ptrtoint {llvm_inside}* {temp} to {LLVMType(CType.POINTER)}')
        return result

    def addLabel(self, name):
        self.code.append(f'{name}:')

    def startFunction(self, typ, identifier, params):
        self.addInstruction(f'define {typ} @{identifier}({params}) {{')
        self.braces += 1

    def endFunction(self, typ):
        self.braces -= 1
        value = 'zeroinitializer'
        if str(typ) == 'void':
            value = ''
            
        self.addInstruction(f'ret {typ} {value}')
        self.addInstruction('}')
        self.temp = 1

    @staticmethod
    def getInstruction(op, typ):
        if op in ['&&', '||']:
            return logicalOp[op]
        elif typ.isFP():
            return floatOp[op]
        else:
            return signedIntOp[op]

    def getTemp(self):
        self.temp += 1
        return f'%{self.temp-1}'
