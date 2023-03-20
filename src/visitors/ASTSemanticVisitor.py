from .ASTVisitor import *
import sys


class ASTSemanticPass1(ASTVisitor):
    def __init__(self):
        self.errors = []
        self.warnings = []

    def getErrors(self):
        return self.errors

    def getWarnings(self):
        return self.warnings

    def enterAssignment(self, node: Assignment):
        # assignment to a constant
        if node.getType().isConstant() and not node.isExplicit():
            err = "[E] on {}: Assignment to a constant".format(node.linenr)
            self.errors.append(err)

        child = node.getChild(0)
        rval = True
        if isinstance(child, Variable):
            rval = False
        elif isinstance(child, UnaryOperation) and child.isDereference():
            rval = False
        elif isinstance(child, BinaryOperation) and child.isArrayOperator():
            rval = False

        if rval:
            err = "[E] on {}: Assignment to an rvalue".format(node.linenr)
            self.errors.append(err)

    def enterUnaryOperation(self, node: UnaryOperation):
        if node.isAddress() or node.isIdentifierOperation():
            child = node.getChild(0)
            rval = True
            if isinstance(child, Variable):
                rval = False
            if isinstance(child, UnaryOperation) and child.isDereference():
                rval = False
            if isinstance(child, BinaryOperation) and child.isArrayOperator():
                rval = False

            if rval:
                err = f"[E] on {node.linenr}: lvalue required as unary ‘{node.getValue()}’ operand but got: {child.getLabel()}"
                self.errors.append(err)

        elif node.isDereference():
            child = node.getChild(0)

            if isinstance(child, Variable):
                typ = child.getSymbolTable().lookUpType(child.getValue())
            else:
                typ = child.getType()

            if not typ.isPointer():
                err = "[E] on {}: Attempting to dereference a non-pointer: {}".format(node.linenr, child.getLabel())
                self.errors.append(err)

        elif node.operator == "-" and node.getType().isPointer():
            err = "[E] on {}: Unary - on pointers not allowed".format(node.linenr)
            self.errors.append(err)

    def enterBinaryOperation(self, node: BinaryOperation):
        if node.isArrayOperator():
            arg1, arg2 = node.getArgs()
            if arg2.getType() != Type(CType.INT):
                self.errors.append(f'[E] on {node.linenr}: Array index is not an integer')
            if not arg1.getType().isArray():
                self.errors.append(f'[E] on {node.linenr}: Array operator on non-array')
        if node.isBoolean():
            arg1, arg2 = node.getArgs()
            if arg1.getType().isArray() or arg2.getType().isArray():
                self.errors.append(f'[E] on {node.linenr}: Comparison of arrays')
        elif node.getValue() == "-":
            arg1, arg2 = node.getArgs()

            # ignore conversions for a second
            try:
                type1 = arg1.getFromType()
            except AttributeError:
                type1 = arg1.getType()
            try:
                type2 = arg2.getFromType()
            except AttributeError:
                type2 = arg2.getType()

            if not type1.isPointer() and type2.isPointer():
                err = "[E] on {}: Invalid subtraction of pointer".format(node.linenr)
                self.errors.append(err)

        elif node.getValue() == "+":
            arg1, arg2 = node.getArgs()

            # ignore conversions for a second
            try:
                type1 = arg1.getFromType()
            except AttributeError:
                type1 = arg1.getType()
            try:
                type2 = arg2.getFromType()
            except AttributeError:
                type2 = arg2.getType()

            if type1.isPointer() and type2.isPointer():
                err = "[E] on {}: Addition of pointer not allowed".format(node.linenr)
                self.errors.append(err)

        elif (node.getValue() == "*" or node.getValue() == "/") and node.getType().isPointer():
            err = "[E] on {}: Operation not allowed on pointer types: {}".format(node.linenr, node.getValue())
            self.errors.append(err)

    def enterConversion(self, node: Conversion):
        to = node.getToType()
        frm = node.getFromType()

        if frm.getInside() == CType.VOID:
            err = "[E] on {}: Invalid conversion from VOID type".format(node.linenr)
            self.errors.append(err)

        fp_p_op = False

        if (to.isFP() and not to.isPointer()) and frm.isPointer():
            fp_p_op = True
        elif (frm.isFP() and not frm.isPointer()) and to.isPointer():
            fp_p_op = True

        if fp_p_op:
            err = "[E] on {}: Conversion between floating point types and pointer types not allowed".format(node.linenr)
            self.errors.append(err)

        if frm > to and not node.isExplicit():
            warn = "[WARNING] on {}: Conversion from richer type: {}, to poorer type: {}, could result in possible loss of information".format(node.linenr, frm, to)
            self.warnings.append(warn)

    def enterFunctionCall(self, node: FunctionCall):
        sig = node.getSignature()
        func_param = node.findFirstNode(Block).getSymbolTable().lookUp(node.getIdentifier())
        if func_param is None:  # function not found, error will be picked up later
            return

        func_sig = func_param.getParent().getSignature(True)

        if func_sig.endswith('...'):
            func_sig = node.getVariadicSignature()

        if not sig == func_sig:
            err = "[E] on {}: Function call does not match function prototype \n expected: {}, but got {}".format(node.linenr, func_sig, sig)
            self.errors.append(err)

    def enterBlock(self, node: Block):
        table = node.getSymbolTable()
        if table.parent is None:  # root symbol table
            main = table.lookUp('main')
            if main is None:
                err = "[E] on {}: No main function is defined in the global scope".format("0:0")
                self.errors.append(err)

    def enterJump(self, node: Jump):
        if node.getValue() == "return":
            if node.getChildrenCount() == 0:
                rtntype = Type(CType.VOID)
            else:
                rtntype = node.getChild(0).getType()

            functype = node.findFirstNode(Function).getType()
            if rtntype != functype:
                err = "[E] on {}: Return type does not match the function return type, declared on {}".format(
                    node.linenr, node.findFirstNode(Function).linenr)
                self.errors.append(err)

        elif node.getValue() == "break" or node.getValue() == "continue":
            find = node.findFirstNode(Construct)
            notfoundfor = True
            while(find is not None):
                if find.getValue() == "iteration":
                    notfoundfor = False
                    break
                else:
                    if find.getParent() is None:
                        break
                    else:
                        find = find.getParent().findFirstNode(Construct)

            if notfoundfor:
                err = "[E] on {}: Loop control statement used outside of a loop".format(
                    node.linenr)
                self.errors.append(err)
