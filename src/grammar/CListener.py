# Generated from src/grammar/C.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

# This class defines a complete listener for a parse tree produced by CParser.
class CListener(ParseTreeListener):

    # Enter a parse tree produced by CParser#start.
    def enterStart(self, ctx:CParser.StartContext):
        pass

    # Exit a parse tree produced by CParser#start.
    def exitStart(self, ctx:CParser.StartContext):
        pass


    # Enter a parse tree produced by CParser#function_declaration.
    def enterFunction_declaration(self, ctx:CParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by CParser#function_declaration.
    def exitFunction_declaration(self, ctx:CParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by CParser#function_parameter.
    def enterFunction_parameter(self, ctx:CParser.Function_parameterContext):
        pass

    # Exit a parse tree produced by CParser#function_parameter.
    def exitFunction_parameter(self, ctx:CParser.Function_parameterContext):
        pass


    # Enter a parse tree produced by CParser#return_type.
    def enterReturn_type(self, ctx:CParser.Return_typeContext):
        pass

    # Exit a parse tree produced by CParser#return_type.
    def exitReturn_type(self, ctx:CParser.Return_typeContext):
        pass


    # Enter a parse tree produced by CParser#macro.
    def enterMacro(self, ctx:CParser.MacroContext):
        pass

    # Exit a parse tree produced by CParser#macro.
    def exitMacro(self, ctx:CParser.MacroContext):
        pass


    # Enter a parse tree produced by CParser#statement.
    def enterStatement(self, ctx:CParser.StatementContext):
        pass

    # Exit a parse tree produced by CParser#statement.
    def exitStatement(self, ctx:CParser.StatementContext):
        pass


    # Enter a parse tree produced by CParser#compound_statement.
    def enterCompound_statement(self, ctx:CParser.Compound_statementContext):
        pass

    # Exit a parse tree produced by CParser#compound_statement.
    def exitCompound_statement(self, ctx:CParser.Compound_statementContext):
        pass


    # Enter a parse tree produced by CParser#selection_statement.
    def enterSelection_statement(self, ctx:CParser.Selection_statementContext):
        pass

    # Exit a parse tree produced by CParser#selection_statement.
    def exitSelection_statement(self, ctx:CParser.Selection_statementContext):
        pass


    # Enter a parse tree produced by CParser#iteration_statement.
    def enterIteration_statement(self, ctx:CParser.Iteration_statementContext):
        pass

    # Exit a parse tree produced by CParser#iteration_statement.
    def exitIteration_statement(self, ctx:CParser.Iteration_statementContext):
        pass


    # Enter a parse tree produced by CParser#jump_statement.
    def enterJump_statement(self, ctx:CParser.Jump_statementContext):
        pass

    # Exit a parse tree produced by CParser#jump_statement.
    def exitJump_statement(self, ctx:CParser.Jump_statementContext):
        pass


    # Enter a parse tree produced by CParser#expression.
    def enterExpression(self, ctx:CParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CParser#expression.
    def exitExpression(self, ctx:CParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CParser#char.
    def enterChar(self, ctx:CParser.CharContext):
        pass

    # Exit a parse tree produced by CParser#char.
    def exitChar(self, ctx:CParser.CharContext):
        pass


    # Enter a parse tree produced by CParser#string.
    def enterString(self, ctx:CParser.StringContext):
        pass

    # Exit a parse tree produced by CParser#string.
    def exitString(self, ctx:CParser.StringContext):
        pass


    # Enter a parse tree produced by CParser#int.
    def enterInt(self, ctx:CParser.IntContext):
        pass

    # Exit a parse tree produced by CParser#int.
    def exitInt(self, ctx:CParser.IntContext):
        pass


    # Enter a parse tree produced by CParser#real.
    def enterReal(self, ctx:CParser.RealContext):
        pass

    # Exit a parse tree produced by CParser#real.
    def exitReal(self, ctx:CParser.RealContext):
        pass


    # Enter a parse tree produced by CParser#variable.
    def enterVariable(self, ctx:CParser.VariableContext):
        pass

    # Exit a parse tree produced by CParser#variable.
    def exitVariable(self, ctx:CParser.VariableContext):
        pass


    # Enter a parse tree produced by CParser#type_specifier.
    def enterType_specifier(self, ctx:CParser.Type_specifierContext):
        pass

    # Exit a parse tree produced by CParser#type_specifier.
    def exitType_specifier(self, ctx:CParser.Type_specifierContext):
        pass


    # Enter a parse tree produced by CParser#explicit_cast_type.
    def enterExplicit_cast_type(self, ctx:CParser.Explicit_cast_typeContext):
        pass

    # Exit a parse tree produced by CParser#explicit_cast_type.
    def exitExplicit_cast_type(self, ctx:CParser.Explicit_cast_typeContext):
        pass


    # Enter a parse tree produced by CParser#declaration.
    def enterDeclaration(self, ctx:CParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CParser#declaration.
    def exitDeclaration(self, ctx:CParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CParser#declarator.
    def enterDeclarator(self, ctx:CParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by CParser#declarator.
    def exitDeclarator(self, ctx:CParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by CParser#function_call.
    def enterFunction_call(self, ctx:CParser.Function_callContext):
        pass

    # Exit a parse tree produced by CParser#function_call.
    def exitFunction_call(self, ctx:CParser.Function_callContext):
        pass



del CParser