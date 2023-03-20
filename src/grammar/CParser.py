# Generated from src/grammar/C.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3Y")
        buf.write("\u011b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\2\5\2*\n\2\3\2\3\2\3\2\3\2\7\2\60\n\2\f\2\16")
        buf.write("\2\63\13\2\3\3\3\3\3\3\3\3\3\3\3\3\7\3;\n\3\f\3\16\3>")
        buf.write("\13\3\5\3@\n\3\3\3\3\3\3\4\3\4\3\4\5\4G\n\4\5\4I\n\4\3")
        buf.write("\4\3\4\3\5\3\5\5\5O\n\5\3\5\5\5R\n\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7`\n\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\7\bg\n\b\f\b\16\bj\13\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\5\t\u0082\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0095\n\n\3")
        buf.write("\n\3\n\5\n\u0099\n\n\3\n\3\n\5\n\u009d\n\n\3\n\3\n\5\n")
        buf.write("\u00a1\n\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00a9\n")
        buf.write("\13\3\13\5\13\u00ac\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00bd\n\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u00db")
        buf.write("\n\f\f\f\16\f\u00de\13\f\3\r\3\r\3\r\3\r\5\r\u00e4\n\r")
        buf.write("\3\16\3\16\3\17\5\17\u00e9\n\17\3\17\3\17\5\17\u00ed\n")
        buf.write("\17\3\20\3\20\3\21\3\21\3\21\3\21\7\21\u00f5\n\21\f\21")
        buf.write("\16\21\u00f8\13\21\3\22\3\22\5\22\u00fc\n\22\7\22\u00fe")
        buf.write("\n\22\f\22\16\22\u0101\13\22\3\22\3\22\3\22\3\22\5\22")
        buf.write("\u0107\n\22\3\22\3\22\5\22\u010b\n\22\3\23\3\23\3\23\3")
        buf.write("\23\3\23\7\23\u0112\n\23\f\23\16\23\u0115\13\23\5\23\u0117")
        buf.write("\n\23\3\23\3\23\3\23\2\3\26\24\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$\2\n\5\2\6\6\17\17\23\23\5\2.\62\66")
        buf.write("\66;;\3\2\62\64\3\2\60\61\3\2@C\3\2>?\3\2#-\3\2./\2\u013c")
        buf.write("\2\61\3\2\2\2\4\64\3\2\2\2\6C\3\2\2\2\bQ\3\2\2\2\nS\3")
        buf.write("\2\2\2\f_\3\2\2\2\16a\3\2\2\2\20\u0081\3\2\2\2\22\u00a0")
        buf.write("\3\2\2\2\24\u00ab\3\2\2\2\26\u00bc\3\2\2\2\30\u00e3\3")
        buf.write("\2\2\2\32\u00e5\3\2\2\2\34\u00e8\3\2\2\2\36\u00ee\3\2")
        buf.write("\2\2 \u00f0\3\2\2\2\"\u00ff\3\2\2\2$\u010c\3\2\2\2&)\5")
        buf.write("\4\3\2\'*\7N\2\2(*\5\16\b\2)\'\3\2\2\2)(\3\2\2\2*\60\3")
        buf.write("\2\2\2+,\5 \21\2,-\7N\2\2-\60\3\2\2\2.\60\5\n\6\2/&\3")
        buf.write("\2\2\2/+\3\2\2\2/.\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61")
        buf.write("\62\3\2\2\2\62\3\3\2\2\2\63\61\3\2\2\2\64\65\5\b\5\2\65")
        buf.write("\66\7T\2\2\66?\7G\2\2\67<\5\6\4\289\7O\2\29;\5\6\4\2:")
        buf.write("8\3\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=@\3\2\2\2><\3")
        buf.write("\2\2\2?\67\3\2\2\2?@\3\2\2\2@A\3\2\2\2AB\7H\2\2B\5\3\2")
        buf.write("\2\2CH\5\34\17\2DF\7\62\2\2EG\7\7\2\2FE\3\2\2\2FG\3\2")
        buf.write("\2\2GI\3\2\2\2HD\3\2\2\2HI\3\2\2\2IJ\3\2\2\2JK\7T\2\2")
        buf.write("K\7\3\2\2\2LN\t\2\2\2MO\7\62\2\2NM\3\2\2\2NO\3\2\2\2O")
        buf.write("R\3\2\2\2PR\7 \2\2QL\3\2\2\2QP\3\2\2\2R\t\3\2\2\2ST\7")
        buf.write("U\2\2TU\7@\2\2UV\7V\2\2VW\7B\2\2W\13\3\2\2\2X`\5\16\b")
        buf.write("\2YZ\5\26\f\2Z[\7N\2\2[`\3\2\2\2\\`\5\20\t\2]`\5\22\n")
        buf.write("\2^`\5\24\13\2_X\3\2\2\2_Y\3\2\2\2_\\\3\2\2\2_]\3\2\2")
        buf.write("\2_^\3\2\2\2`\r\3\2\2\2ah\7K\2\2bg\5\f\7\2cd\5 \21\2d")
        buf.write("e\7N\2\2eg\3\2\2\2fb\3\2\2\2fc\3\2\2\2gj\3\2\2\2hf\3\2")
        buf.write("\2\2hi\3\2\2\2ik\3\2\2\2jh\3\2\2\2kl\7L\2\2l\17\3\2\2")
        buf.write("\2mn\7\22\2\2no\7G\2\2op\5\26\f\2pq\7H\2\2qr\5\f\7\2r")
        buf.write("\u0082\3\2\2\2st\7\22\2\2tu\7G\2\2uv\5\26\f\2vw\7H\2\2")
        buf.write("wx\5\f\7\2xy\7\f\2\2yz\5\f\7\2z\u0082\3\2\2\2{|\7\34\2")
        buf.write("\2|}\7G\2\2}~\5\26\f\2~\177\7H\2\2\177\u0080\5\f\7\2\u0080")
        buf.write("\u0082\3\2\2\2\u0081m\3\2\2\2\u0081s\3\2\2\2\u0081{\3")
        buf.write("\2\2\2\u0082\21\3\2\2\2\u0083\u0084\7\"\2\2\u0084\u0085")
        buf.write("\7G\2\2\u0085\u0086\5\26\f\2\u0086\u0087\7H\2\2\u0087")
        buf.write("\u0088\5\f\7\2\u0088\u00a1\3\2\2\2\u0089\u008a\7\n\2\2")
        buf.write("\u008a\u008b\5\f\7\2\u008b\u008c\7\"\2\2\u008c\u008d\7")
        buf.write("G\2\2\u008d\u008e\5\26\f\2\u008e\u008f\7H\2\2\u008f\u0090")
        buf.write("\7N\2\2\u0090\u00a1\3\2\2\2\u0091\u0092\7\20\2\2\u0092")
        buf.write("\u0094\7G\2\2\u0093\u0095\5 \21\2\u0094\u0093\3\2\2\2")
        buf.write("\u0094\u0095\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098\7")
        buf.write("N\2\2\u0097\u0099\5\26\f\2\u0098\u0097\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009c\7N\2\2\u009b")
        buf.write("\u009d\5\26\f\2\u009c\u009b\3\2\2\2\u009c\u009d\3\2\2")
        buf.write("\2\u009d\u009e\3\2\2\2\u009e\u009f\7H\2\2\u009f\u00a1")
        buf.write("\5\f\7\2\u00a0\u0083\3\2\2\2\u00a0\u0089\3\2\2\2\u00a0")
        buf.write("\u0091\3\2\2\2\u00a1\23\3\2\2\2\u00a2\u00a3\7\4\2\2\u00a3")
        buf.write("\u00ac\7N\2\2\u00a4\u00a5\7\b\2\2\u00a5\u00ac\7N\2\2\u00a6")
        buf.write("\u00a8\7\26\2\2\u00a7\u00a9\5\26\f\2\u00a8\u00a7\3\2\2")
        buf.write("\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ac")
        buf.write("\7N\2\2\u00ab\u00a2\3\2\2\2\u00ab\u00a4\3\2\2\2\u00ab")
        buf.write("\u00a6\3\2\2\2\u00ac\25\3\2\2\2\u00ad\u00ae\b\f\1\2\u00ae")
        buf.write("\u00bd\5$\23\2\u00af\u00b0\t\3\2\2\u00b0\u00bd\5\26\f")
        buf.write("\16\u00b1\u00b2\7G\2\2\u00b2\u00b3\5\36\20\2\u00b3\u00b4")
        buf.write("\7H\2\2\u00b4\u00b5\5\26\f\r\u00b5\u00bd\3\2\2\2\u00b6")
        buf.write("\u00b7\7G\2\2\u00b7\u00b8\5\26\f\2\u00b8\u00b9\7H\2\2")
        buf.write("\u00b9\u00bd\3\2\2\2\u00ba\u00bd\5\32\16\2\u00bb\u00bd")
        buf.write("\5\30\r\2\u00bc\u00ad\3\2\2\2\u00bc\u00af\3\2\2\2\u00bc")
        buf.write("\u00b1\3\2\2\2\u00bc\u00b6\3\2\2\2\u00bc\u00ba\3\2\2\2")
        buf.write("\u00bc\u00bb\3\2\2\2\u00bd\u00dc\3\2\2\2\u00be\u00bf\f")
        buf.write("\f\2\2\u00bf\u00c0\t\4\2\2\u00c0\u00db\5\26\f\r\u00c1")
        buf.write("\u00c2\f\13\2\2\u00c2\u00c3\t\5\2\2\u00c3\u00db\5\26\f")
        buf.write("\f\u00c4\u00c5\f\n\2\2\u00c5\u00c6\t\6\2\2\u00c6\u00db")
        buf.write("\5\26\f\13\u00c7\u00c8\f\t\2\2\u00c8\u00c9\t\7\2\2\u00c9")
        buf.write("\u00db\5\26\f\n\u00ca\u00cb\f\b\2\2\u00cb\u00cc\7<\2\2")
        buf.write("\u00cc\u00db\5\26\f\t\u00cd\u00ce\f\7\2\2\u00ce\u00cf")
        buf.write("\7=\2\2\u00cf\u00db\5\26\f\b\u00d0\u00d1\f\6\2\2\u00d1")
        buf.write("\u00d2\t\b\2\2\u00d2\u00db\5\26\f\6\u00d3\u00d4\f\21\2")
        buf.write("\2\u00d4\u00db\t\t\2\2\u00d5\u00d6\f\17\2\2\u00d6\u00d7")
        buf.write("\7I\2\2\u00d7\u00d8\5\26\f\2\u00d8\u00d9\7J\2\2\u00d9")
        buf.write("\u00db\3\2\2\2\u00da\u00be\3\2\2\2\u00da\u00c1\3\2\2\2")
        buf.write("\u00da\u00c4\3\2\2\2\u00da\u00c7\3\2\2\2\u00da\u00ca\3")
        buf.write("\2\2\2\u00da\u00cd\3\2\2\2\u00da\u00d0\3\2\2\2\u00da\u00d3")
        buf.write("\3\2\2\2\u00da\u00d5\3\2\2\2\u00db\u00de\3\2\2\2\u00dc")
        buf.write("\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\27\3\2\2\2\u00de")
        buf.write("\u00dc\3\2\2\2\u00df\u00e4\7R\2\2\u00e0\u00e4\7S\2\2\u00e1")
        buf.write("\u00e4\7P\2\2\u00e2\u00e4\7Q\2\2\u00e3\u00df\3\2\2\2\u00e3")
        buf.write("\u00e0\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e2\3\2\2\2")
        buf.write("\u00e4\31\3\2\2\2\u00e5\u00e6\7T\2\2\u00e6\33\3\2\2\2")
        buf.write("\u00e7\u00e9\7\7\2\2\u00e8\u00e7\3\2\2\2\u00e8\u00e9\3")
        buf.write("\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00ec\t\2\2\2\u00eb\u00ed")
        buf.write("\7\7\2\2\u00ec\u00eb\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed")
        buf.write("\35\3\2\2\2\u00ee\u00ef\t\2\2\2\u00ef\37\3\2\2\2\u00f0")
        buf.write("\u00f1\5\34\17\2\u00f1\u00f6\5\"\22\2\u00f2\u00f3\7O\2")
        buf.write("\2\u00f3\u00f5\5\"\22\2\u00f4\u00f2\3\2\2\2\u00f5\u00f8")
        buf.write("\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7")
        buf.write("!\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f9\u00fb\7\62\2\2\u00fa")
        buf.write("\u00fc\7\7\2\2\u00fb\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2")
        buf.write("\u00fc\u00fe\3\2\2\2\u00fd\u00f9\3\2\2\2\u00fe\u0101\3")
        buf.write("\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0102")
        buf.write("\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u0106\7T\2\2\u0103")
        buf.write("\u0104\7I\2\2\u0104\u0105\7P\2\2\u0105\u0107\7J\2\2\u0106")
        buf.write("\u0103\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u010a\3\2\2\2")
        buf.write("\u0108\u0109\7#\2\2\u0109\u010b\5\26\f\2\u010a\u0108\3")
        buf.write("\2\2\2\u010a\u010b\3\2\2\2\u010b#\3\2\2\2\u010c\u010d")
        buf.write("\7T\2\2\u010d\u0116\7G\2\2\u010e\u0113\5\26\f\2\u010f")
        buf.write("\u0110\7O\2\2\u0110\u0112\5\26\f\2\u0111\u010f\3\2\2\2")
        buf.write("\u0112\u0115\3\2\2\2\u0113\u0111\3\2\2\2\u0113\u0114\3")
        buf.write("\2\2\2\u0114\u0117\3\2\2\2\u0115\u0113\3\2\2\2\u0116\u010e")
        buf.write("\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\3\2\2\2\u0118")
        buf.write("\u0119\7H\2\2\u0119%\3\2\2\2\")/\61<?FHNQ_fh\u0081\u0094")
        buf.write("\u0098\u009c\u00a0\u00a8\u00ab\u00bc\u00da\u00dc\u00e3")
        buf.write("\u00e8\u00ec\u00f6\u00fb\u00ff\u0106\u010a\u0113\u0116")
        return buf.getvalue()


class CParser ( Parser ):

    grammarFileName = "C.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'auto'", "'break'", "'case'", "'char'", 
                     "'const'", "'continue'", "'default'", "'do'", "'double'", 
                     "'else'", "'enum'", "'extern'", "'float'", "'for'", 
                     "'goto'", "'if'", "'int'", "'long'", "'register'", 
                     "'return'", "'short'", "'signed'", "'sizeof'", "'static'", 
                     "'struct'", "'switch'", "'typedef'", "'union'", "'unsigned'", 
                     "'void'", "'volatile'", "'while'", "'='", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'&='", "'|='", "'^='", "'<<='", 
                     "'>>='", "'++'", "'--'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'~'", "'&'", "'|'", "'^'", "'<<'", "'>>'", 
                     "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'.'", "'->'", "'?'", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "':'", "';'", "','", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'#include'" ]

    symbolicNames = [ "<INVALID>", "AUTO", "BREAK", "CASE", "CHAR", "CONST", 
                      "CONTINUE", "DEFAULT", "DO", "DOUBLE", "ELSE", "ENUM", 
                      "EXTERN", "FLOAT", "FOR", "GOTO", "IF", "INT", "LONG", 
                      "REGISTER", "RETURN", "SHORT", "SIGNED", "SIZEOF", 
                      "STATIC", "STRUCT", "SWITCH", "TYPEDEF", "UNION", 
                      "UNSIGNED", "VOID", "VOLATILE", "WHILE", "ASSIGN_OP", 
                      "PLUS_ASSIGN_OP", "MINUS_ASSIGN_OP", "STAR_ASSIGN_OP", 
                      "SLASH_ASSIGN_OP", "PERCENT_ASSIGN_OP", "AMPERSAND_ASSIGN_OP", 
                      "BAR_ASSIGN_OP", "CARET_ASSIGN_OP", "SHIFTL_ASSIGN_OP", 
                      "SHIFTR_ASSING_OP", "INCREMENT_OP", "DECREMENT_OP", 
                      "PLUS_OP", "MINUS_OP", "STAR_OP", "SLASH_OP", "PERCENT_OP", 
                      "TILDE_OP", "AMPERSAND_OP", "BAR_OP", "CARET_OP", 
                      "SHIFTL_OP", "SHIFTR_OP", "NOT_OP", "AND_OP", "OR_OP", 
                      "EQ_OP", "NEQ_OP", "LT_OP", "LE_OP", "GT_OP", "GE_OP", 
                      "DOT_OP", "ARROW_OP", "QUESTION_OP", "LPAREN", "RPAREN", 
                      "LBRACKET", "RBRACKET", "LBRACE", "RBRACE", "COLON", 
                      "SEMICOLON", "COMMA", "INT_LITERAL", "REAL_LITERAL", 
                      "CHAR_LITERAL", "STRING_LITERAL", "IDENTIFIER", "INCLUDE", 
                      "PATH", "COMMENT", "LINE_COMMENT", "WS" ]

    RULE_start = 0
    RULE_function_declaration = 1
    RULE_function_parameter = 2
    RULE_return_type = 3
    RULE_macro = 4
    RULE_statement = 5
    RULE_compound_statement = 6
    RULE_selection_statement = 7
    RULE_iteration_statement = 8
    RULE_jump_statement = 9
    RULE_expression = 10
    RULE_literal = 11
    RULE_variable = 12
    RULE_type_specifier = 13
    RULE_explicit_cast_type = 14
    RULE_declaration = 15
    RULE_declarator = 16
    RULE_function_call = 17

    ruleNames =  [ "start", "function_declaration", "function_parameter", 
                   "return_type", "macro", "statement", "compound_statement", 
                   "selection_statement", "iteration_statement", "jump_statement", 
                   "expression", "literal", "variable", "type_specifier", 
                   "explicit_cast_type", "declaration", "declarator", "function_call" ]

    EOF = Token.EOF
    AUTO=1
    BREAK=2
    CASE=3
    CHAR=4
    CONST=5
    CONTINUE=6
    DEFAULT=7
    DO=8
    DOUBLE=9
    ELSE=10
    ENUM=11
    EXTERN=12
    FLOAT=13
    FOR=14
    GOTO=15
    IF=16
    INT=17
    LONG=18
    REGISTER=19
    RETURN=20
    SHORT=21
    SIGNED=22
    SIZEOF=23
    STATIC=24
    STRUCT=25
    SWITCH=26
    TYPEDEF=27
    UNION=28
    UNSIGNED=29
    VOID=30
    VOLATILE=31
    WHILE=32
    ASSIGN_OP=33
    PLUS_ASSIGN_OP=34
    MINUS_ASSIGN_OP=35
    STAR_ASSIGN_OP=36
    SLASH_ASSIGN_OP=37
    PERCENT_ASSIGN_OP=38
    AMPERSAND_ASSIGN_OP=39
    BAR_ASSIGN_OP=40
    CARET_ASSIGN_OP=41
    SHIFTL_ASSIGN_OP=42
    SHIFTR_ASSING_OP=43
    INCREMENT_OP=44
    DECREMENT_OP=45
    PLUS_OP=46
    MINUS_OP=47
    STAR_OP=48
    SLASH_OP=49
    PERCENT_OP=50
    TILDE_OP=51
    AMPERSAND_OP=52
    BAR_OP=53
    CARET_OP=54
    SHIFTL_OP=55
    SHIFTR_OP=56
    NOT_OP=57
    AND_OP=58
    OR_OP=59
    EQ_OP=60
    NEQ_OP=61
    LT_OP=62
    LE_OP=63
    GT_OP=64
    GE_OP=65
    DOT_OP=66
    ARROW_OP=67
    QUESTION_OP=68
    LPAREN=69
    RPAREN=70
    LBRACKET=71
    RBRACKET=72
    LBRACE=73
    RBRACE=74
    COLON=75
    SEMICOLON=76
    COMMA=77
    INT_LITERAL=78
    REAL_LITERAL=79
    CHAR_LITERAL=80
    STRING_LITERAL=81
    IDENTIFIER=82
    INCLUDE=83
    PATH=84
    COMMENT=85
    LINE_COMMENT=86
    WS=87

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.Function_declarationContext)
            else:
                return self.getTypedRuleContext(CParser.Function_declarationContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(CParser.DeclarationContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.SEMICOLON)
            else:
                return self.getToken(CParser.SEMICOLON, i)

        def macro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.MacroContext)
            else:
                return self.getTypedRuleContext(CParser.MacroContext,i)


        def compound_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.Compound_statementContext)
            else:
                return self.getTypedRuleContext(CParser.Compound_statementContext,i)


        def getRuleIndex(self):
            return CParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = CParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.CHAR) | (1 << CParser.CONST) | (1 << CParser.FLOAT) | (1 << CParser.INT) | (1 << CParser.VOID))) != 0) or _la==CParser.INCLUDE:
                self.state = 45
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 36
                    self.function_declaration()
                    self.state = 39
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [CParser.SEMICOLON]:
                        self.state = 37
                        self.match(CParser.SEMICOLON)
                        pass
                    elif token in [CParser.LBRACE]:
                        self.state = 38
                        self.compound_statement()
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 2:
                    self.state = 41
                    self.declaration()
                    self.state = 42
                    self.match(CParser.SEMICOLON)
                    pass

                elif la_ == 3:
                    self.state = 44
                    self.macro()
                    pass


                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_type(self):
            return self.getTypedRuleContext(CParser.Return_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(CParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(CParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CParser.RPAREN, 0)

        def function_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.Function_parameterContext)
            else:
                return self.getTypedRuleContext(CParser.Function_parameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.COMMA)
            else:
                return self.getToken(CParser.COMMA, i)

        def getRuleIndex(self):
            return CParser.RULE_function_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declaration" ):
                listener.enterFunction_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declaration" ):
                listener.exitFunction_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = CParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.return_type()
            self.state = 51
            self.match(CParser.IDENTIFIER)
            self.state = 52
            self.match(CParser.LPAREN)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.CHAR) | (1 << CParser.CONST) | (1 << CParser.FLOAT) | (1 << CParser.INT))) != 0):
                self.state = 53
                self.function_parameter()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CParser.COMMA:
                    self.state = 54
                    self.match(CParser.COMMA)
                    self.state = 55
                    self.function_parameter()
                    self.state = 60
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 63
            self.match(CParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_specifier(self):
            return self.getTypedRuleContext(CParser.Type_specifierContext,0)


        def IDENTIFIER(self):
            return self.getToken(CParser.IDENTIFIER, 0)

        def STAR_OP(self):
            return self.getToken(CParser.STAR_OP, 0)

        def CONST(self):
            return self.getToken(CParser.CONST, 0)

        def getRuleIndex(self):
            return CParser.RULE_function_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_parameter" ):
                listener.enterFunction_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_parameter" ):
                listener.exitFunction_parameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_parameter" ):
                return visitor.visitFunction_parameter(self)
            else:
                return visitor.visitChildren(self)




    def function_parameter(self):

        localctx = CParser.Function_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.type_specifier()
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CParser.STAR_OP:
                self.state = 66
                self.match(CParser.STAR_OP)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CParser.CONST:
                    self.state = 67
                    self.match(CParser.CONST)




            self.state = 72
            self.match(CParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(CParser.FLOAT, 0)

        def INT(self):
            return self.getToken(CParser.INT, 0)

        def CHAR(self):
            return self.getToken(CParser.CHAR, 0)

        def STAR_OP(self):
            return self.getToken(CParser.STAR_OP, 0)

        def VOID(self):
            return self.getToken(CParser.VOID, 0)

        def getRuleIndex(self):
            return CParser.RULE_return_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_type" ):
                listener.enterReturn_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_type" ):
                listener.exitReturn_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_type" ):
                return visitor.visitReturn_type(self)
            else:
                return visitor.visitChildren(self)




    def return_type(self):

        localctx = CParser.Return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_return_type)
        self._la = 0 # Token type
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CParser.CHAR, CParser.FLOAT, CParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.CHAR) | (1 << CParser.FLOAT) | (1 << CParser.INT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CParser.STAR_OP:
                    self.state = 75
                    self.match(CParser.STAR_OP)


                pass
            elif token in [CParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(CParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MacroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCLUDE(self):
            return self.getToken(CParser.INCLUDE, 0)

        def LT_OP(self):
            return self.getToken(CParser.LT_OP, 0)

        def PATH(self):
            return self.getToken(CParser.PATH, 0)

        def GT_OP(self):
            return self.getToken(CParser.GT_OP, 0)

        def getRuleIndex(self):
            return CParser.RULE_macro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro" ):
                listener.enterMacro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro" ):
                listener.exitMacro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro" ):
                return visitor.visitMacro(self)
            else:
                return visitor.visitChildren(self)




    def macro(self):

        localctx = CParser.MacroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_macro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(CParser.INCLUDE)
            self.state = 82
            self.match(CParser.LT_OP)
            self.state = 83
            self.match(CParser.PATH)
            self.state = 84
            self.match(CParser.GT_OP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compound_statement(self):
            return self.getTypedRuleContext(CParser.Compound_statementContext,0)


        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(CParser.SEMICOLON, 0)

        def selection_statement(self):
            return self.getTypedRuleContext(CParser.Selection_statementContext,0)


        def iteration_statement(self):
            return self.getTypedRuleContext(CParser.Iteration_statementContext,0)


        def jump_statement(self):
            return self.getTypedRuleContext(CParser.Jump_statementContext,0)


        def getRuleIndex(self):
            return CParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CParser.LBRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.compound_statement()
                pass
            elif token in [CParser.INCREMENT_OP, CParser.DECREMENT_OP, CParser.PLUS_OP, CParser.MINUS_OP, CParser.STAR_OP, CParser.AMPERSAND_OP, CParser.NOT_OP, CParser.LPAREN, CParser.INT_LITERAL, CParser.REAL_LITERAL, CParser.CHAR_LITERAL, CParser.STRING_LITERAL, CParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.expression(0)
                self.state = 88
                self.match(CParser.SEMICOLON)
                pass
            elif token in [CParser.IF, CParser.SWITCH]:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.selection_statement()
                pass
            elif token in [CParser.DO, CParser.FOR, CParser.WHILE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.iteration_statement()
                pass
            elif token in [CParser.BREAK, CParser.CONTINUE, CParser.RETURN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.jump_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(CParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.StatementContext)
            else:
                return self.getTypedRuleContext(CParser.StatementContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(CParser.DeclarationContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.SEMICOLON)
            else:
                return self.getToken(CParser.SEMICOLON, i)

        def getRuleIndex(self):
            return CParser.RULE_compound_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_statement" ):
                listener.enterCompound_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_statement" ):
                listener.exitCompound_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_statement" ):
                return visitor.visitCompound_statement(self)
            else:
                return visitor.visitChildren(self)




    def compound_statement(self):

        localctx = CParser.Compound_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_compound_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(CParser.LBRACE)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.BREAK) | (1 << CParser.CHAR) | (1 << CParser.CONST) | (1 << CParser.CONTINUE) | (1 << CParser.DO) | (1 << CParser.FLOAT) | (1 << CParser.FOR) | (1 << CParser.IF) | (1 << CParser.INT) | (1 << CParser.RETURN) | (1 << CParser.SWITCH) | (1 << CParser.WHILE) | (1 << CParser.INCREMENT_OP) | (1 << CParser.DECREMENT_OP) | (1 << CParser.PLUS_OP) | (1 << CParser.MINUS_OP) | (1 << CParser.STAR_OP) | (1 << CParser.AMPERSAND_OP) | (1 << CParser.NOT_OP))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (CParser.LPAREN - 69)) | (1 << (CParser.LBRACE - 69)) | (1 << (CParser.INT_LITERAL - 69)) | (1 << (CParser.REAL_LITERAL - 69)) | (1 << (CParser.CHAR_LITERAL - 69)) | (1 << (CParser.STRING_LITERAL - 69)) | (1 << (CParser.IDENTIFIER - 69)))) != 0):
                self.state = 100
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CParser.BREAK, CParser.CONTINUE, CParser.DO, CParser.FOR, CParser.IF, CParser.RETURN, CParser.SWITCH, CParser.WHILE, CParser.INCREMENT_OP, CParser.DECREMENT_OP, CParser.PLUS_OP, CParser.MINUS_OP, CParser.STAR_OP, CParser.AMPERSAND_OP, CParser.NOT_OP, CParser.LPAREN, CParser.LBRACE, CParser.INT_LITERAL, CParser.REAL_LITERAL, CParser.CHAR_LITERAL, CParser.STRING_LITERAL, CParser.IDENTIFIER]:
                    self.state = 96
                    self.statement()
                    pass
                elif token in [CParser.CHAR, CParser.CONST, CParser.FLOAT, CParser.INT]:
                    self.state = 97
                    self.declaration()
                    self.state = 98
                    self.match(CParser.SEMICOLON)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
            self.match(CParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Selection_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CParser.IF, 0)

        def LPAREN(self):
            return self.getToken(CParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(CParser.RPAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.StatementContext)
            else:
                return self.getTypedRuleContext(CParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(CParser.ELSE, 0)

        def SWITCH(self):
            return self.getToken(CParser.SWITCH, 0)

        def getRuleIndex(self):
            return CParser.RULE_selection_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelection_statement" ):
                listener.enterSelection_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelection_statement" ):
                listener.exitSelection_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelection_statement" ):
                return visitor.visitSelection_statement(self)
            else:
                return visitor.visitChildren(self)




    def selection_statement(self):

        localctx = CParser.Selection_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_selection_statement)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(CParser.IF)
                self.state = 108
                self.match(CParser.LPAREN)
                self.state = 109
                self.expression(0)
                self.state = 110
                self.match(CParser.RPAREN)
                self.state = 111
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(CParser.IF)
                self.state = 114
                self.match(CParser.LPAREN)
                self.state = 115
                self.expression(0)
                self.state = 116
                self.match(CParser.RPAREN)
                self.state = 117
                self.statement()
                self.state = 118
                self.match(CParser.ELSE)
                self.state = 119
                self.statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.match(CParser.SWITCH)
                self.state = 122
                self.match(CParser.LPAREN)
                self.state = 123
                self.expression(0)
                self.state = 124
                self.match(CParser.RPAREN)
                self.state = 125
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Iteration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.init = None # DeclarationContext
            self.cond = None # ExpressionContext
            self.iteration = None # ExpressionContext

        def WHILE(self):
            return self.getToken(CParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(CParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(CParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(CParser.StatementContext,0)


        def DO(self):
            return self.getToken(CParser.DO, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.SEMICOLON)
            else:
                return self.getToken(CParser.SEMICOLON, i)

        def FOR(self):
            return self.getToken(CParser.FOR, 0)

        def declaration(self):
            return self.getTypedRuleContext(CParser.DeclarationContext,0)


        def getRuleIndex(self):
            return CParser.RULE_iteration_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIteration_statement" ):
                listener.enterIteration_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIteration_statement" ):
                listener.exitIteration_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIteration_statement" ):
                return visitor.visitIteration_statement(self)
            else:
                return visitor.visitChildren(self)




    def iteration_statement(self):

        localctx = CParser.Iteration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_iteration_statement)
        self._la = 0 # Token type
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CParser.WHILE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(CParser.WHILE)
                self.state = 130
                self.match(CParser.LPAREN)
                self.state = 131
                self.expression(0)
                self.state = 132
                self.match(CParser.RPAREN)
                self.state = 133
                self.statement()
                pass
            elif token in [CParser.DO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.match(CParser.DO)
                self.state = 136
                self.statement()
                self.state = 137
                self.match(CParser.WHILE)
                self.state = 138
                self.match(CParser.LPAREN)
                self.state = 139
                self.expression(0)
                self.state = 140
                self.match(CParser.RPAREN)
                self.state = 141
                self.match(CParser.SEMICOLON)
                pass
            elif token in [CParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.match(CParser.FOR)
                self.state = 144
                self.match(CParser.LPAREN)
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.CHAR) | (1 << CParser.CONST) | (1 << CParser.FLOAT) | (1 << CParser.INT))) != 0):
                    self.state = 145
                    localctx.init = self.declaration()


                self.state = 148
                self.match(CParser.SEMICOLON)
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 44)) & ~0x3f) == 0 and ((1 << (_la - 44)) & ((1 << (CParser.INCREMENT_OP - 44)) | (1 << (CParser.DECREMENT_OP - 44)) | (1 << (CParser.PLUS_OP - 44)) | (1 << (CParser.MINUS_OP - 44)) | (1 << (CParser.STAR_OP - 44)) | (1 << (CParser.AMPERSAND_OP - 44)) | (1 << (CParser.NOT_OP - 44)) | (1 << (CParser.LPAREN - 44)) | (1 << (CParser.INT_LITERAL - 44)) | (1 << (CParser.REAL_LITERAL - 44)) | (1 << (CParser.CHAR_LITERAL - 44)) | (1 << (CParser.STRING_LITERAL - 44)) | (1 << (CParser.IDENTIFIER - 44)))) != 0):
                    self.state = 149
                    localctx.cond = self.expression(0)


                self.state = 152
                self.match(CParser.SEMICOLON)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 44)) & ~0x3f) == 0 and ((1 << (_la - 44)) & ((1 << (CParser.INCREMENT_OP - 44)) | (1 << (CParser.DECREMENT_OP - 44)) | (1 << (CParser.PLUS_OP - 44)) | (1 << (CParser.MINUS_OP - 44)) | (1 << (CParser.STAR_OP - 44)) | (1 << (CParser.AMPERSAND_OP - 44)) | (1 << (CParser.NOT_OP - 44)) | (1 << (CParser.LPAREN - 44)) | (1 << (CParser.INT_LITERAL - 44)) | (1 << (CParser.REAL_LITERAL - 44)) | (1 << (CParser.CHAR_LITERAL - 44)) | (1 << (CParser.STRING_LITERAL - 44)) | (1 << (CParser.IDENTIFIER - 44)))) != 0):
                    self.state = 153
                    localctx.iteration = self.expression(0)


                self.state = 156
                self.match(CParser.RPAREN)
                self.state = 157
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Jump_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(CParser.SEMICOLON, 0)

        def CONTINUE(self):
            return self.getToken(CParser.CONTINUE, 0)

        def RETURN(self):
            return self.getToken(CParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_jump_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJump_statement" ):
                listener.enterJump_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJump_statement" ):
                listener.exitJump_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJump_statement" ):
                return visitor.visitJump_statement(self)
            else:
                return visitor.visitChildren(self)




    def jump_statement(self):

        localctx = CParser.Jump_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_jump_statement)
        self._la = 0 # Token type
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CParser.BREAK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(CParser.BREAK)
                self.state = 161
                self.match(CParser.SEMICOLON)
                pass
            elif token in [CParser.CONTINUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.match(CParser.CONTINUE)
                self.state = 163
                self.match(CParser.SEMICOLON)
                pass
            elif token in [CParser.RETURN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.match(CParser.RETURN)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 44)) & ~0x3f) == 0 and ((1 << (_la - 44)) & ((1 << (CParser.INCREMENT_OP - 44)) | (1 << (CParser.DECREMENT_OP - 44)) | (1 << (CParser.PLUS_OP - 44)) | (1 << (CParser.MINUS_OP - 44)) | (1 << (CParser.STAR_OP - 44)) | (1 << (CParser.AMPERSAND_OP - 44)) | (1 << (CParser.NOT_OP - 44)) | (1 << (CParser.LPAREN - 44)) | (1 << (CParser.INT_LITERAL - 44)) | (1 << (CParser.REAL_LITERAL - 44)) | (1 << (CParser.CHAR_LITERAL - 44)) | (1 << (CParser.STRING_LITERAL - 44)) | (1 << (CParser.IDENTIFIER - 44)))) != 0):
                    self.state = 165
                    self.expression(0)


                self.state = 168
                self.match(CParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def function_call(self):
            return self.getTypedRuleContext(CParser.Function_callContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.ExpressionContext,i)


        def PLUS_OP(self):
            return self.getToken(CParser.PLUS_OP, 0)

        def MINUS_OP(self):
            return self.getToken(CParser.MINUS_OP, 0)

        def STAR_OP(self):
            return self.getToken(CParser.STAR_OP, 0)

        def AMPERSAND_OP(self):
            return self.getToken(CParser.AMPERSAND_OP, 0)

        def NOT_OP(self):
            return self.getToken(CParser.NOT_OP, 0)

        def INCREMENT_OP(self):
            return self.getToken(CParser.INCREMENT_OP, 0)

        def DECREMENT_OP(self):
            return self.getToken(CParser.DECREMENT_OP, 0)

        def LPAREN(self):
            return self.getToken(CParser.LPAREN, 0)

        def explicit_cast_type(self):
            return self.getTypedRuleContext(CParser.Explicit_cast_typeContext,0)


        def RPAREN(self):
            return self.getToken(CParser.RPAREN, 0)

        def variable(self):
            return self.getTypedRuleContext(CParser.VariableContext,0)


        def literal(self):
            return self.getTypedRuleContext(CParser.LiteralContext,0)


        def SLASH_OP(self):
            return self.getToken(CParser.SLASH_OP, 0)

        def PERCENT_OP(self):
            return self.getToken(CParser.PERCENT_OP, 0)

        def LT_OP(self):
            return self.getToken(CParser.LT_OP, 0)

        def LE_OP(self):
            return self.getToken(CParser.LE_OP, 0)

        def GT_OP(self):
            return self.getToken(CParser.GT_OP, 0)

        def GE_OP(self):
            return self.getToken(CParser.GE_OP, 0)

        def EQ_OP(self):
            return self.getToken(CParser.EQ_OP, 0)

        def NEQ_OP(self):
            return self.getToken(CParser.NEQ_OP, 0)

        def AND_OP(self):
            return self.getToken(CParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(CParser.OR_OP, 0)

        def ASSIGN_OP(self):
            return self.getToken(CParser.ASSIGN_OP, 0)

        def PLUS_ASSIGN_OP(self):
            return self.getToken(CParser.PLUS_ASSIGN_OP, 0)

        def MINUS_ASSIGN_OP(self):
            return self.getToken(CParser.MINUS_ASSIGN_OP, 0)

        def STAR_ASSIGN_OP(self):
            return self.getToken(CParser.STAR_ASSIGN_OP, 0)

        def SLASH_ASSIGN_OP(self):
            return self.getToken(CParser.SLASH_ASSIGN_OP, 0)

        def PERCENT_ASSIGN_OP(self):
            return self.getToken(CParser.PERCENT_ASSIGN_OP, 0)

        def SHIFTL_ASSIGN_OP(self):
            return self.getToken(CParser.SHIFTL_ASSIGN_OP, 0)

        def SHIFTR_ASSING_OP(self):
            return self.getToken(CParser.SHIFTR_ASSING_OP, 0)

        def AMPERSAND_ASSIGN_OP(self):
            return self.getToken(CParser.AMPERSAND_ASSIGN_OP, 0)

        def CARET_ASSIGN_OP(self):
            return self.getToken(CParser.CARET_ASSIGN_OP, 0)

        def BAR_ASSIGN_OP(self):
            return self.getToken(CParser.BAR_ASSIGN_OP, 0)

        def RBRACKET(self):
            return self.getToken(CParser.RBRACKET, 0)

        def LBRACKET(self):
            return self.getToken(CParser.LBRACKET, 0)

        def getRuleIndex(self):
            return CParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 172
                self.function_call()
                pass

            elif la_ == 2:
                self.state = 173
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.INCREMENT_OP) | (1 << CParser.DECREMENT_OP) | (1 << CParser.PLUS_OP) | (1 << CParser.MINUS_OP) | (1 << CParser.STAR_OP) | (1 << CParser.AMPERSAND_OP) | (1 << CParser.NOT_OP))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 174
                self.expression(12)
                pass

            elif la_ == 3:
                self.state = 175
                self.match(CParser.LPAREN)
                self.state = 176
                self.explicit_cast_type()
                self.state = 177
                self.match(CParser.RPAREN)
                self.state = 178
                self.expression(11)
                pass

            elif la_ == 4:
                self.state = 180
                self.match(CParser.LPAREN)
                self.state = 181
                self.expression(0)
                self.state = 182
                self.match(CParser.RPAREN)
                pass

            elif la_ == 5:
                self.state = 184
                self.variable()
                pass

            elif la_ == 6:
                self.state = 185
                self.literal()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 218
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 216
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 188
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 189
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.STAR_OP) | (1 << CParser.SLASH_OP) | (1 << CParser.PERCENT_OP))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 190
                        self.expression(11)
                        pass

                    elif la_ == 2:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 191
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 192
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CParser.PLUS_OP or _la==CParser.MINUS_OP):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 193
                        self.expression(10)
                        pass

                    elif la_ == 3:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 194
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 195
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((((_la - 62)) & ~0x3f) == 0 and ((1 << (_la - 62)) & ((1 << (CParser.LT_OP - 62)) | (1 << (CParser.LE_OP - 62)) | (1 << (CParser.GT_OP - 62)) | (1 << (CParser.GE_OP - 62)))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 196
                        self.expression(9)
                        pass

                    elif la_ == 4:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 197
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 198
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CParser.EQ_OP or _la==CParser.NEQ_OP):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 199
                        self.expression(8)
                        pass

                    elif la_ == 5:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 200
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 201
                        localctx.op = self.match(CParser.AND_OP)
                        self.state = 202
                        self.expression(7)
                        pass

                    elif la_ == 6:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 203
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 204
                        localctx.op = self.match(CParser.OR_OP)
                        self.state = 205
                        self.expression(6)
                        pass

                    elif la_ == 7:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 206
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 207
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.ASSIGN_OP) | (1 << CParser.PLUS_ASSIGN_OP) | (1 << CParser.MINUS_ASSIGN_OP) | (1 << CParser.STAR_ASSIGN_OP) | (1 << CParser.SLASH_ASSIGN_OP) | (1 << CParser.PERCENT_ASSIGN_OP) | (1 << CParser.AMPERSAND_ASSIGN_OP) | (1 << CParser.BAR_ASSIGN_OP) | (1 << CParser.CARET_ASSIGN_OP) | (1 << CParser.SHIFTL_ASSIGN_OP) | (1 << CParser.SHIFTR_ASSING_OP))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 208
                        self.expression(4)
                        pass

                    elif la_ == 8:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 209
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 210
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CParser.INCREMENT_OP or _la==CParser.DECREMENT_OP):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

                    elif la_ == 9:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 211
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 212
                        localctx.op = self.match(CParser.LBRACKET)
                        self.state = 213
                        self.expression(0)
                        self.state = 214
                        self.match(CParser.RBRACKET)
                        pass

             
                self.state = 220
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_LITERAL(self):
            return self.getToken(CParser.STRING_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class CharContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(CParser.CHAR_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar" ):
                listener.enterChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar" ):
                listener.exitChar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChar" ):
                return visitor.visitChar(self)
            else:
                return visitor.visitChildren(self)


    class RealContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REAL_LITERAL(self):
            return self.getToken(CParser.REAL_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReal" ):
                listener.enterReal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReal" ):
                listener.exitReal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReal" ):
                return visitor.visitReal(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_LITERAL(self):
            return self.getToken(CParser.INT_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = CParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_literal)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CParser.CHAR_LITERAL]:
                localctx = CParser.CharContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(CParser.CHAR_LITERAL)
                pass
            elif token in [CParser.STRING_LITERAL]:
                localctx = CParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.match(CParser.STRING_LITERAL)
                pass
            elif token in [CParser.INT_LITERAL]:
                localctx = CParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self.match(CParser.INT_LITERAL)
                pass
            elif token in [CParser.REAL_LITERAL]:
                localctx = CParser.RealContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 224
                self.match(CParser.REAL_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = CParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(CParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_specifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(CParser.FLOAT, 0)

        def INT(self):
            return self.getToken(CParser.INT, 0)

        def CHAR(self):
            return self.getToken(CParser.CHAR, 0)

        def CONST(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.CONST)
            else:
                return self.getToken(CParser.CONST, i)

        def getRuleIndex(self):
            return CParser.RULE_type_specifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_specifier" ):
                listener.enterType_specifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_specifier" ):
                listener.exitType_specifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_specifier" ):
                return visitor.visitType_specifier(self)
            else:
                return visitor.visitChildren(self)




    def type_specifier(self):

        localctx = CParser.Type_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_type_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CParser.CONST:
                self.state = 229
                self.match(CParser.CONST)


            self.state = 232
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.CHAR) | (1 << CParser.FLOAT) | (1 << CParser.INT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CParser.CONST:
                self.state = 233
                self.match(CParser.CONST)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Explicit_cast_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(CParser.FLOAT, 0)

        def INT(self):
            return self.getToken(CParser.INT, 0)

        def CHAR(self):
            return self.getToken(CParser.CHAR, 0)

        def getRuleIndex(self):
            return CParser.RULE_explicit_cast_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplicit_cast_type" ):
                listener.enterExplicit_cast_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplicit_cast_type" ):
                listener.exitExplicit_cast_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplicit_cast_type" ):
                return visitor.visitExplicit_cast_type(self)
            else:
                return visitor.visitChildren(self)




    def explicit_cast_type(self):

        localctx = CParser.Explicit_cast_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_explicit_cast_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.CHAR) | (1 << CParser.FLOAT) | (1 << CParser.INT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_specifier(self):
            return self.getTypedRuleContext(CParser.Type_specifierContext,0)


        def declarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.DeclaratorContext)
            else:
                return self.getTypedRuleContext(CParser.DeclaratorContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.COMMA)
            else:
                return self.getToken(CParser.COMMA, i)

        def getRuleIndex(self):
            return CParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = CParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.type_specifier()
            self.state = 239
            self.declarator()
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.COMMA:
                self.state = 240
                self.match(CParser.COMMA)
                self.state = 241
                self.declarator()
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CParser.IDENTIFIER, 0)

        def STAR_OP(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.STAR_OP)
            else:
                return self.getToken(CParser.STAR_OP, i)

        def LBRACKET(self):
            return self.getToken(CParser.LBRACKET, 0)

        def INT_LITERAL(self):
            return self.getToken(CParser.INT_LITERAL, 0)

        def RBRACKET(self):
            return self.getToken(CParser.RBRACKET, 0)

        def ASSIGN_OP(self):
            return self.getToken(CParser.ASSIGN_OP, 0)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def CONST(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.CONST)
            else:
                return self.getToken(CParser.CONST, i)

        def getRuleIndex(self):
            return CParser.RULE_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarator" ):
                listener.enterDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarator" ):
                listener.exitDeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarator" ):
                return visitor.visitDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def declarator(self):

        localctx = CParser.DeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_declarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.STAR_OP:
                self.state = 247
                self.match(CParser.STAR_OP)
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CParser.CONST:
                    self.state = 248
                    self.match(CParser.CONST)


                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 256
            self.match(CParser.IDENTIFIER)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CParser.LBRACKET:
                self.state = 257
                self.match(CParser.LBRACKET)
                self.state = 258
                self.match(CParser.INT_LITERAL)
                self.state = 259
                self.match(CParser.RBRACKET)


            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CParser.ASSIGN_OP:
                self.state = 262
                self.match(CParser.ASSIGN_OP)
                self.state = 263
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(CParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CParser.RPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.COMMA)
            else:
                return self.getToken(CParser.COMMA, i)

        def getRuleIndex(self):
            return CParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = CParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(CParser.IDENTIFIER)
            self.state = 267
            self.match(CParser.LPAREN)
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 44)) & ~0x3f) == 0 and ((1 << (_la - 44)) & ((1 << (CParser.INCREMENT_OP - 44)) | (1 << (CParser.DECREMENT_OP - 44)) | (1 << (CParser.PLUS_OP - 44)) | (1 << (CParser.MINUS_OP - 44)) | (1 << (CParser.STAR_OP - 44)) | (1 << (CParser.AMPERSAND_OP - 44)) | (1 << (CParser.NOT_OP - 44)) | (1 << (CParser.LPAREN - 44)) | (1 << (CParser.INT_LITERAL - 44)) | (1 << (CParser.REAL_LITERAL - 44)) | (1 << (CParser.CHAR_LITERAL - 44)) | (1 << (CParser.STRING_LITERAL - 44)) | (1 << (CParser.IDENTIFIER - 44)))) != 0):
                self.state = 268
                self.expression(0)
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CParser.COMMA:
                    self.state = 269
                    self.match(CParser.COMMA)
                    self.state = 270
                    self.expression(0)
                    self.state = 275
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 278
            self.match(CParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 13)
         




