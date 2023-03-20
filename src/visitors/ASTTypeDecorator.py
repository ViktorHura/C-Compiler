from .ASTVisitor import *
from src.Type import *

from collections import deque
from copy import deepcopy

class ASTTypeDecorator(ASTVisitor):
    def __init__(self):
        self.stack = deque()

    def exitVariable(self, node: Variable):
        t = node.getSymbolTable().lookUpType(node.getValue())
        self.stack.append(t)
        node.setType(t)

    def exitAssignment(self, node: Assignment):
        t_rhs = self.stack.pop()
        t_lhs = self.stack.pop()
        t = t_lhs
        if t != t_rhs:
            self._addConversion(node, node.getChild(1), t_rhs, t)
        self.stack.append(t)
        node.setType(t)

    def exitUnaryOperation(self, node: UnaryOperation):
        t = self.stack.pop()

        if node.isDereference():
            d = t.dereference()
            if d is None:
                self.stack.append(t)
                return
            else:
                t = d
        elif node.isAddress():
            t = t.makePointer()
        elif node.isBoolean():
            t = Type(CType.BOOL)

        self.stack.append(t)
        node.setType(t)

    def exitBinaryOperation(self, node: BinaryOperation):
        t_rhs = self.stack.pop()
        t_lhs = self.stack.pop()

        if node.isArrayOperator():
            t = Type(t_lhs.getCore())
            if t_rhs != Type(CType.INT):
                print("FATAL ERROR: Non integer index in array access oeprator")
                # self._addConversion(node, node.getChild(1), t_rhs, Type(CType.INT))
        else:
            if node.isLogical():
                t = Type(CType.BOOL)
            elif node.getValue() == "%":
                t = Type(CType.INT)
            else:
                t = max(t_lhs, t_rhs)

            if t != t_lhs:
                self._addConversion(node, node.getChild(0), t_lhs, t)
            if t != t_rhs:
                self._addConversion(node, node.getChild(1), t_rhs, t)

            # return type of binary operations is int
            if node.isBoolean():
                t = Type(CType.BOOL)

        self.stack.append(t)
        node.setType(t)

    def exitLiteral(self, node: Literal):
        self.stack.append(node.getType())

    def enterFunction(self, node: Function):
        node.setType(node.getChild(0).getType())

    def exitFunctionCall(self, node: FunctionCall):
        f = node.getValue()

        # get actual paramter types
        params = []
        for child in range(0, node.getChildrenCount()):
            params.insert(0, self.stack.pop())

        # set return type
        typ = f.getType()
        node.setType(typ)
        self.stack.append(typ)

        # get formal paramater types
        if node.function_identifier in ['scanf', 'printf']:
            formal_types = node.getVariadicTypes()
        else:
            formal_types = []
            for p in f.getParams():
                formal_types.append(p.getType())

        if len(params) != len(formal_types):
            return            
        
        # add conversions from actual types to formal types
        for index, formal_type in enumerate(formal_types):
            param = params[index]
            if (param != formal_type):
                self._addConversion(node, node.getChild(index), param, formal_type)

    def exitBlock(self, node: Block):
        self.stack.clear()

    def exitConversion(self, node: Conversion):
        node.setFromType(self.stack.pop())
        self.stack.append(node.getToType())

    def exitJump(self, node: Jump):
        if node.getValue() == "return":
            functype = node.findFirstNode(Function).getType()
            if functype == Type(CType.VOID):
                return

            if node.getChildrenCount() == 0:
                return

            rtntype = node.getChild(0).getType()

            if rtntype != functype:
                self._addConversion(node, node.getChild(0), rtntype, functype)


    def _addConversion(self, node, child, child_type: Type, dest_type: Type):
        # check if conversion is allowed:
        if child_type == Type(CType.INT) and dest_type == Type(CType.CHAR).makePointer():
            return

        conv = Conversion(child_type, dest_type)
        conv.linenr = node.linenr
        node.replaceChild(child, conv)
        conv.pushChild(child)