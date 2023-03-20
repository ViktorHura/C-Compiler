from .Node import *
from src.Type import *


class FunctionCall(Node):
    def __init__(self, function_identifier):
        super().__init__()
        self.function_identifier = function_identifier  # points to function construct
        
        # super dangerous: this can be the forward declaration node instead of the actual funciton node
        self.function = None

    def getValue(self):
        return self.function

    def setValue(self, value):
        self.function = value

    def getLabel(self):
        return f'Call {self.function.getLabel()}'

    def getIdentifier(self):
        return self.function_identifier

    def getSignature(self):
        sig = ''
        for i in range(0, len(self.m_children)):
            var = self.getChild(i)
            sig += str(var.getType()) + ","
        return sig

    def getVariadicSignature(self):
        sig = ''
        for typ in self.getVariadicTypes():
            sig += f'{typ},'
        return sig

    def getVariadicTypes(self):
        if self.function_identifier not in ['printf', 'scanf']:
            return None

        format_string = self.getChild(0).m_value
        idx = 0

        types = []
        fparams = self.function.getParams()
        for fp in fparams:
            types.append(fp.getType())

        while idx < len(format_string):
            char = format_string[idx]
            if char == '%':
                idx += 1
                while format_string[idx].isnumeric():
                    idx += 1

                # d, i, s, c
                typ = format_string[idx]
                if typ == 'd':
                    typ = Type(CType.INT)
                elif typ == 'i':
                    typ = Type(CType.INT)
                elif typ == 's':
                    typ = Type(CType.CHAR).makePointer()
                elif typ == 'c':
                    typ = Type(CType.CHAR)
                elif typ == 'f':
                    typ = Type(CType.DOUBLE)
                elif typ == 'p':
                    typ = Type(CType.POINTER)
                else:
                    continue
                
                if self.function_identifier == 'scanf':
                    typ = typ.makePointer()

                types.append(typ)
            idx += 1

        return types

    def acceptVisitor(self, visitor):
        visitor.enterFunctionCall(self)
        for child in self.m_children:
            child.acceptVisitor(visitor)
        visitor.exitFunctionCall(self)

    def generateLLVMStdio(self, context):
        fmt = self.getChild(0).generateLLVM(context)
        # convert our pointer system to stdio pointer system
        fmptr = context.getTemp()
        context.addInstruction(f'{fmptr} = inttoptr {LLVMType(CType.POINTER)} {fmt} to i8*')

        # get variadic parameters
        params = ''
        for i in range(1, self.getChildrenCount()):
            p = self.getChild(i)
            
            # convert our pointers to their pointers
            original_type = p.getType()
            if original_type.isPointer():
                inside_type = original_type.dereference().getLLVM()
                original = p.generateLLVM(context)
                original_type = original_type.getLLVM()
                val = context.getTemp()
                context.addInstruction(f'{val} = inttoptr {original_type} {original} to {inside_type}*')
                typ = f'{inside_type}*'
            else:
                typ = p.getType().getLLVM()
                val = p.generateLLVM(context)

            params +=  f'{typ} {val},'

        result = context.getTemp()
        if len(params) > 0:
            context.addInstruction( \
                f'{result} = call i32 (i8*, ...) @{self.function_identifier}' \
                f'(i8* {fmptr}, {params[:-1]})')
        else:
             context.addInstruction( \
                f'{result} = call i32 (i8*, ...) @{self.function_identifier}' \
                f'(i8* {fmptr})')


    def generateLLVM(self, context):
        if self.function_identifier in ['printf', 'scanf']:
            return self.generateLLVMStdio(context)

        f = context.symbol_table.lookUp(self.function_identifier).getParent()
        iden = f.getID()
        typ = self.getType()

        # get formal parameter types
        param_types = []
        param_types_string = ''
        for p in f.getParams():
            t = p.getType().getLLVM()
            param_types.append(t)
            param_types_string += str(t) + ','
        param_types_string = param_types_string[0:-1]

        # get parameter values
        params_string = ''
        for i in range(len(param_types)):
            params_string += f'{param_types[i]} {self.getChild(i).generateLLVM(context)},'
        params_string = params_string[0:-1]
        
        # add instruction
        if (typ == Type(CType.VOID)):
            context.addInstruction(f'call {typ.getLLVM()} ({param_types_string}) @{iden}({params_string})')
        else:
            result = context.getTemp()
            context.addInstruction(f'{result} = call {typ.getLLVM()} ({param_types_string}) @{iden}({params_string})')
            return result

    def generateMIPS(self, context):
        if self.function_identifier == 'printf':
            return self.generateMIPSPrintf(context)
        elif self.function_identifier == 'scanf':
            return self.generateMIPSScanf(context)

        f = context.symbol_table.lookUp(self.function_identifier).getParent()
        iden = f.getID()

        # prepare arguments
        for i in range(len(f.getParams())):
            param = self.getChild(i).generateMIPS(context)
            context.addStoreInstruction(param, f'{-4*i}($sp)')
            param.release()

        # save active temp and float registers
        context.saveActiveRegister('f')
        context.saveActiveRegister('t')

        # call
        context.addInstruction(f'jal {iden}')
        
        if f.getType().isFP():
            result = context.getFloatTemp()
            context.addInstruction(f'mov.s {result.getRegister()}, $f0')
        else:
            result = context.getTemp()
            context.addInstruction(f'move {result.getRegister()}, $v0')
        return result

    def generateMIPSPrintf(self, context):
        # parse format string
        fmt = self.getChild(0).getValue()
        prints = []
        curr = ""
        idx = 0
        while idx < len(fmt):
            char = fmt[idx]
            
            if char == '%' and not idx + 1 >= len(fmt):
                if len(curr) > 0:
                    prints.append(curr)
                curr = ''
                idx += 1
                if (fmt[idx]) in ['d', 's', 'c', 'f']:
                    prints.append(f'%{fmt[idx]}')
                else:
                    print(f'Unknow format argument: {fmt[idx]}')
            else:
                curr += char
            idx += 1
        if len(curr) > 0:
            prints.append(curr)
        
        # create instructions
        idx = 1
        for p in prints:
            if p[0] == '%':

                reg = self.getChild(idx).generateMIPS(context)

                if p[1] == 'd' or p[1] == 'i':
                    t = 1
                    move_fmt = 'move $a0, {}'
                elif p[1] == 'f':
                    t = 2
                    f12 = context.getRegister('$f12')
                    move_fmt = 'mov.s $f12, {}'
                    f12.release()
                elif p[1] == 'c':
                    t = 11
                    move_fmt = 'move $a0, {}'
                elif p[1] == 's':
                    t = 4
                    move_fmt = 'move $a0, {}'

                
                context.addInstruction(move_fmt.format(reg.getRegister()))
                reg.release()
                context.addInstruction(f'li $v0, {t}')
                context.addInstruction('syscall')
                idx+=1
            else:
                label = context.addString(p)
                context.addInstruction(f'la $a0, {label}')
                context.addInstruction('li $v0, 4')
                context.addInstruction('syscall')

    def generateMIPSScanf(self, context):
        fmt = self.getChild(0).getValue()

        scans = []
        for scan in fmt.split('%'):
            if len(scan) == 0:
                continue

            typ = scan[-1]
            size = scan[:-1]
            scans.append((typ, size))

        for i, s in enumerate(scans):
            l = s[1]
            s = s[0]
            t = context.getScanSyscall(s)
            reg = self.getChild(i+1).generateMIPS(context)
            
            context.addInstruction(f'li $v0, {t}')

            if s == 's':
                context.addInstruction(f'move $a0, {reg.getRegister()}')
                context.addInstruction(f'li $a1, {int(l)+1}')

            context.addInstruction('syscall')
            
            if s == 'f':
                context.addInstruction(f'swc1 $f0, 0({reg.getRegister()})')
            elif s == 's':
                pass
            else:
                context.addInstruction(f'sw $v0, 0({reg.getRegister()})')