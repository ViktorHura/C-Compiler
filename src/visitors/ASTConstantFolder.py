from .ASTVisitor import *

class ASTConstantFolder(ASTVisitor):
    def exitBinaryOperation(self, node: BinaryOperation):
        left = node.getChild(0)
        right = node.getChild(1)

        if isinstance(left, Literal) and isinstance(right, Literal):
            typ = node.getType()
            v1 = left.getValue()
            v2 = right.getValue()
            op = node.getValue()

            if op == "+":
                newval = v1 + v2
            elif op == "-":
                newval = v1 - v2
            elif op == "*":
                newval = v1 * v2
            elif op == "/":
                newval = v1 / v2
            elif op == "<":
                newval = v1 < v2
            elif op == ">":
                newval = v1 > v2
            elif op == "==":
                newval = (v1 == v2)
            elif op == "%":
                newval = v1 % v2
            elif op == ">=":
                newval = (v1 >= v2)
            elif op == "<=":
                newval = (v1 <= v2)
            elif op == "!=":
                newval = (v1 != v2)
            elif op == "&&":
                newval = (v1 and v2)
            elif op == "||":
                newval = (v1 or v2)
            else:
                return

            newval = typ.convertValue(newval)

            lit = Literal(newval, typ)
            node.getParent().replaceChild(node, lit)

    def exitUnaryOperation(self, node: UnaryOperation):
        child = node.getChild(0)

        if isinstance(child, Literal):
            typ = node.getType()
            val = child.getValue()
            op = node.getValue()

            if op == "+":
                newval = val
            elif op == "-":
                newval = -1 * val
            else:
                return

            lit = Literal(newval, typ)
            node.getParent().replaceChild(node, lit)

    def exitConversion(self, node: Conversion):
        child = node.getChild(0)

        if isinstance(child, Literal):
            val = child.getValue()

            if node.getToType().isPointer():
                return

            newval = node.getToType().convertValue(val)

            lit = Literal(newval, node.getToType())
            node.getParent().replaceChild(node, lit)