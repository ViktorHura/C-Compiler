from enum import IntEnum
from functools import *


class CType(IntEnum):
    VOID = -1
    BOOL = 0
    CHAR = 1
    SHORT = 3
    INT = 4
    LONG = 5
    FLOAT = 6
    DOUBLE = 7
    POINTER = 8
    STRING = 9
    VARIDIC = 10

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def isFP(self):
        return self.value == CType.FLOAT or self.value == CType.DOUBLE


class LLVMType:
    LLVMCONFIG = {
        CType.VOID: ('void', 0),
        CType.CHAR: ('i', 8),
        CType.SHORT: ('i', 16),
        CType.INT: ('i', 32),
        CType.LONG: ('i', 32),
        CType.FLOAT: ('double', 64),
        CType.DOUBLE: ('double', 64),
        CType.POINTER: ('i', 99),
        CType.BOOL: ('i', 1)
    }

    def __init__(self, c_type: CType, array_size=0):
        info = self.LLVMCONFIG.get(c_type)

        self.type = info[0]
        self.size = info[1]
        self.array_size = array_size

    def to(self, to_type):
        if self.isArray() or to_type.isArray():
            return None

        if self.isFP() == to_type.isFP():
            if self.size < to_type.size:
                if self.size == 1:
                    return 'zext' # zero extend bools
                return 'fpext' if self.isFP() else 'sext'
            elif self.size > to_type.size:
                return 'fptrunc' if self.isFP() else 'trunc'
        else:
            if self.isFP():
                return 'fptosi'
            elif to_type.isFP():
                return 'sitofp'
        return None

    def isFP(self):
        return self.type in ['float', 'double']

    def isArray(self):
        return self.array_size > 0

    def __repr__(self):
        result = self.type
        if self.type == 'i':
            result = f'i{self.size}'
        
        if self.isArray():
            result = f'[{self.array_size} x {result}]'

        return result
        

@total_ordering
class Type:
    def __init__(self, inside=None):
        self.inside = inside
        if inside is None:
            self.inside = CType.VOID
        self.const = False
        self.ptr = False
        self.array_size = False

    def getCore(self):
        if not (self.isPointer() or self.isArray()):
            return self.inside
        return self.inside.getCore()

    def getLLVM(self):
        if self.isPointer():
            return LLVMType(CType.POINTER)
        else:
            return LLVMType(self.getCore(), self.array_size)

    def setCore(self, new):
        if not (self.isPointer() or self.isArray()):
            self.inside = new
        else:
            return self.inside.setCore(new)

    def getInside(self):
        return self.inside

    def setInside(self, inside):
        self.inside = inside

    def isFP(self):
        return self.getCore().isFP()

    def dereference(self):
        if self.ptr:
            return self.inside
        return None

    def makePointer(self):
        res = Type(self)
        res.ptr = True
        return res

    def makeArray(self, size):
        res = Type(self)
        res.array_size = size
        return res

    def dereferenceArray(self):
        if self.isArray():
            return self.inside
        return None

    def isPointer(self):
        return self.ptr

    def isConstant(self):
        return self.const

    def isArray(self):
        return self.array_size > 0

    def __eq__(self, other):
        if other is None or self is None:   # false if one is None
            return False

        if ((isinstance(self, CType) and not isinstance(other, CType)) or
                (not isinstance(self, CType) and isinstance(other, CType))):
            return False

        # array types are never equal
        if (self.isArray() or other.isArray()):
            if self.array_size == other.array_size and self.inside.__eq__(other.inside):
                return True
            else:
                return False

        # can't be equal type if one is pointer and other isn't
        if (self.isPointer() and not other.isPointer()) or (not self.isPointer() and other.isPointer()):
            return False

        # both not pointer
        elif not self.ptr:
            return self.inside == other.inside
        #both pointers
        else:
            return self.inside.__eq__(other.inside)

    def __gt__(self, other):

        # array types are not comparable
        if (self.isArray() or other.isArray()):
            return False

        if self.ptr and not other.ptr:
            return True

        elif not self.ptr and other.ptr:
            return False

        elif not self.ptr:
            return self.inside > other.inside

        else:
            return self.inside.__gt__(other.inside)

    def __str__(self):
        if self.isPointer():
            result = self.inside.__str__() + " *"
            if self.const:
                result += " const"
        elif self.isArray():
            result =  f'{self.inside.__str__()}[{self.array_size}]'
        else:
            result = ""
            if self.const:
                result += "const "
            result += CType(self.inside).name

        return result

    def convertValue(self, value):
        typ = self.getInside()
        val = value
        if typ == CType.DOUBLE or typ == CType.FLOAT:
            return float(val)
        elif typ == CType.INT:
            return int(val)
        elif typ == CType.CHAR:
            val = int(value)
            return val % 256
        elif typ == CType.BOOL:
            return 1 if bool(value) else 0

        return value
