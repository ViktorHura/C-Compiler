# Generated from src/grammar/C.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

# This class defines a complete generic visitor for a parse tree produced by CParser.

class CVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CParser#start.
    def visitStart(self, ctx:CParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#function_declaration.
    def visitFunction_declaration(self, ctx:CParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#function_parameter.
    def visitFunction_parameter(self, ctx:CParser.Function_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#return_type.
    def visitReturn_type(self, ctx:CParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#macro.
    def visitMacro(self, ctx:CParser.MacroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#statement.
    def visitStatement(self, ctx:CParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#compound_statement.
    def visitCompound_statement(self, ctx:CParser.Compound_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#selection_statement.
    def visitSelection_statement(self, ctx:CParser.Selection_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#iteration_statement.
    def visitIteration_statement(self, ctx:CParser.Iteration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#jump_statement.
    def visitJump_statement(self, ctx:CParser.Jump_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#expression.
    def visitExpression(self, ctx:CParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#char.
    def visitChar(self, ctx:CParser.CharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#string.
    def visitString(self, ctx:CParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#int.
    def visitInt(self, ctx:CParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#real.
    def visitReal(self, ctx:CParser.RealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#variable.
    def visitVariable(self, ctx:CParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#type_specifier.
    def visitType_specifier(self, ctx:CParser.Type_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#explicit_cast_type.
    def visitExplicit_cast_type(self, ctx:CParser.Explicit_cast_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#declaration.
    def visitDeclaration(self, ctx:CParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#declarator.
    def visitDeclarator(self, ctx:CParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#function_call.
    def visitFunction_call(self, ctx:CParser.Function_callContext):
        return self.visitChildren(ctx)



del CParser