from src.grammar.CListener import CListener
from src.grammar.CParser import CParser
from src.nodes import *
from src.Type import *

from copy import deepcopy
import sys

class ASTBuilder(CListener):
    def __init__(self):
        self.m_root = Block()
        self.m_current = self.m_root
        self.errors = []

    def getErrors(self) -> list:
        return self.errors

    def up(self, ctx):
        self.m_current.linenr = str(ctx.start.line) + ":" + str(ctx.start.column)
        self.m_current = self.m_current.getParent()

    def getRoot(self):
        return self.m_root

    def getTypeFromChildren(self, node):
        l = []
        for i in range(node.getChildCount()):
            l.append(node.getChild(i).getText())

        typ = CType.VOID
        if 'int' in l:
            typ = CType.INT
        elif 'float' in l:
            typ = CType.FLOAT
        elif 'char' in l:
            typ = CType.CHAR
        return Type(typ)

    def has_cast(self, ctx):
        for c in ctx.children:
            if isinstance(c, CParser.Explicit_cast_typeContext):
                return True, c
        return False, None

    # expression
    def enterExpression(self, ctx):
        if ctx.op:
            operator = ctx.op.text
            if operator == '=':
                result = Assignment()
            elif ctx.getChildCount() == 2:  # operator + child
                if operator in ['++', '--']:
                    full = ctx.getText()
                    if full.startswith('++') or full.startswith('--'):
                        result = UnaryOperation(operator + 'pre')
                    else:
                        result = UnaryOperation(operator + 'post')
                else:
                    result = UnaryOperation(operator)
            else:
                if operator == '[':
                    operator = '[]'
                result = BinaryOperation(operator)

            self.m_current = self.m_current.pushChild(result)
        else:
            cast, typnode = self.has_cast(ctx)

            if cast:
                typ = self.getTypeFromChildren(typnode)

                conv = Conversion(Type(CType.VOID), typ)
                conv.setExplicit()

                self.m_current = self.m_current.pushChild(conv)

    def exitExpression(self, ctx):
        # only go up if expression was added (skip empty parenthesis nodes and so on)
        cast, _ = self.has_cast(ctx)
        if ctx.op or cast:
            self.up(ctx)

    def enterVariable(self, ctx):
        result = Variable(ctx.getText())
        self.m_current = self.m_current.pushChild(result)

    def exitVariable(self, ctx):
        self.up(ctx)

    # char literal
    def enterChar(self, ctx):
        value = ctx.getChild(0).getText()  # get value of literal (no need to optimise this)
        child = Literal(ord(value[1]), Type(CType.CHAR), False)
        child.linenr = str(ctx.start.line) + ":" + str(ctx.start.column)
        self.m_current.pushChild(child)  # add as child, no need to enter in AST, literal is leaf

    # string literal
    def enterString(self, ctx):
        value = ctx.getChild(0).getText()[1:-1]  # get value of literal (no need to optimise this)
        child = Literal(value, Type(CType.CHAR).makePointer())
        child.linenr = str(ctx.start.line) + ":" + str(ctx.start.column)
        self.m_current.pushChild(child)  # add as child, no need to enter in AST, literal is leaf

    # int literal
    def enterInt(self, ctx):
        value = ctx.getChild(0).getText()  # get value of literal (no need to optimise this)
        # TODO: check for signed and long suffix
        child = Literal(int(value), Type(CType.INT))
        child.linenr = str(ctx.start.line) + ":" + str(ctx.start.column)
        self.m_current.pushChild(child)  # add as child, no need to enter in AST, literal is leaf

    # real literal
    def enterReal(self, ctx):
        value = ctx.getChild(0).getText()  # get value of literal (no need to optimise this)
        # TODO: check for float and long suffix
        child = Literal(float(value), Type(CType.FLOAT))
        child.linenr = str(ctx.start.line) + ":" + str(ctx.start.column)
        self.m_current.pushChild(child)  # add as child, no need to enter in AST, literal is leaf

    # Declarations
    def enterDeclaration(self, ctx: CParser.DeclarationContext):
        dec = Declaration()
        self.m_current = self.m_current.pushChild(dec)

    def exitDeclaration(self, ctx: CParser.DeclarationContext):
        self.up(ctx)

    # TypeSpecifier
    def enterType_specifier(self, ctx: CParser.Type_specifierContext, function=False):
        typ = self.getTypeFromChildren(ctx)

        if function: # dealing with a function return type
            ptr = ctx.STAR_OP() is not None
            if ptr:
                typ = typ.makePointer()

            ident = ctx.parentCtx.IDENTIFIER().getText()

            self.m_current = self.m_current.pushChild(FunctionParameter(ident, typ))
        else:
            const = ctx.CONST()
            typ.const = len(const) > 0

            self.m_current = self.m_current.pushChild(TypeSpecifier(typ))

    def exitType_specifier(self, ctx: CParser.Type_specifierContext):
        self.up(ctx)

    # Declarator
    def enterDeclarator(self, ctx):
        full = ctx.getText()
        identifier = ctx.IDENTIFIER().getText()
        typ = deepcopy(self.m_current.getChild(0).getType())
        dec = Declarator(identifier, typ)

        ptr = len(ctx.STAR_OP())
        arr = ctx.LBRACKET() is not None
        
        for i in range(0, ptr):
            full = full[1:].strip() # consume one pointer
            if full.startswith('const'):
                dec.makePointer(True)
                full = full[5:].strip()
            else:
                dec.makePointer(False)

        if arr:
            size = ctx.INT_LITERAL()
            if size:
                dec.toArray(int(size.getText()))
            else:
                self.errors.append(f'[E] on {ctx.start.line}:{ctx.start.column}: Non integer array size: {ctx.getText()}')

        self.m_current = self.m_current.pushChild(dec)

    def exitDeclarator(self, ctx):
        self.up(ctx)

    def enterCompound_statement(self, ctx: CParser.Compound_statementContext):
        self.m_current = self.m_current.pushChild(Block())

    def exitCompound_statement(self, ctx: CParser.Compound_statementContext):
        self.up(ctx)

    def enterSelection_statement(self, ctx:CParser.Selection_statementContext):
        self.m_current = self.m_current.pushChild(Construct('selection'))

    def exitSelection_statement(self, ctx:CParser.Selection_statementContext):
        self.up(ctx)

    def enterIteration_statement(self, ctx:CParser.Iteration_statementContext):
        self.m_current = self.m_current.pushChild(Construct('iteration'))

    def exitIteration_statement(self, ctx:CParser.Selection_statementContext):
        self.up(ctx)

    def enterJump_statement(self, ctx:CParser.Jump_statementContext):
        if ctx.BREAK() is not None:
            kind = 'break'
        elif ctx.CONTINUE() is not None:
            kind = 'continue'
        else:
            kind = 'return'

        self.m_current = self.m_current.pushChild(Jump(kind))

    def exitJump_statement(self, ctx:CParser.Jump_statementContext):
        self.up(ctx)

    def enterFunction_declaration(self, ctx:CParser.Function_declarationContext):
        self.m_current = self.m_current.pushChild(Function())

    def exitFunction_declaration(self, ctx:CParser.Function_declarationContext):
        self.up(ctx)

    def enterReturn_type(self, ctx):
        self.enterType_specifier(ctx, True)

    def exitReturn_type(self, ctx):
        self.up(ctx)

    def enterFunction_parameter(self, ctx):
        typ = CType.VOID  # set the type void temporarily, we will get real type later from child
        ident = ctx.IDENTIFIER().getText()
        self.m_current = self.m_current.pushChild(FunctionParameter(ident, typ))

    def exitFunction_parameter(self, ctx):
        self.m_current.setType(self.m_current.getChild(0).getType())  # get our type from the type specifier child
        self.m_current.destroyChildAt(0)  # remove said child
        ptr = ctx.STAR_OP() is not None  # check for pointer
        if ptr:
            self.m_current.setType(self.m_current.type.makePointer())
        self.up(ctx)

    def enterFunction_call(self, ctx):
        ide = ctx.IDENTIFIER().getText()
        self.m_current = self.m_current.pushChild(FunctionCall(ide))

    def exitFunction_call(self, ctx):
        self.up(ctx)

    def enterMacro(self, ctx):
        path = ctx.PATH().getText()
        if path == 'stdio.h':
            f1 = self.m_current.pushChild(Function())
            f1.pushChild(FunctionParameter('printf', Type(CType.INT)))
            f1.pushChild(FunctionParameter('format', Type(CType.CHAR).makePointer()))
            f2 = self.m_current.pushChild(Function())
            f2.pushChild(FunctionParameter('scanf', Type(CType.INT)))
            f2.pushChild(FunctionParameter('format', Type(CType.CHAR).makePointer()))
        else:
            self.errors.append(f'[E] on {ctx.start.line}:{ctx.start.column}: Unknown import: {path}')

    # def enterExplicit_cast_op(self, ctx:CParser.Explicit_cast_opContext):
    #     self.m_current = self.m_current.pushChild(UnaryOperation("explicit_cast"))
    #
    # def exitExplicit_cast_op(self, ctx:CParser.Explicit_cast_opContext):
    #     self.up(ctx)