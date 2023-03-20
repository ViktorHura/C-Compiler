# Generated from src/grammar/C.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2Y")
        buf.write("\u0259\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write("!\3!\3!\3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3")
        buf.write("+\3+\3,\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\38\39\39\39\3:\3:\3;\3;\3;\3<\3<\3<\3")
        buf.write("=\3=\3=\3>\3>\3>\3?\3?\3@\3@\3@\3A\3A\3B\3B\3B\3C\3C\3")
        buf.write("D\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3")
        buf.write("L\3M\3M\3N\3N\3O\6O\u01f2\nO\rO\16O\u01f3\3P\3P\3Q\3Q")
        buf.write("\5Q\u01fa\nQ\3R\3R\3S\7S\u01ff\nS\fS\16S\u0202\13S\3S")
        buf.write("\3S\6S\u0206\nS\rS\16S\u0207\3S\5S\u020b\nS\3T\3T\3T\5")
        buf.write("T\u0210\nT\3U\3U\3U\5U\u0215\nU\3U\3U\3V\3V\3V\7V\u021c")
        buf.write("\nV\fV\16V\u021f\13V\3V\3V\3W\3W\7W\u0225\nW\fW\16W\u0228")
        buf.write("\13W\3X\3X\3X\3X\3X\3X\3X\3X\3X\3Y\6Y\u0234\nY\rY\16Y")
        buf.write("\u0235\3Z\3Z\3Z\3Z\7Z\u023c\nZ\fZ\16Z\u023f\13Z\3Z\3Z")
        buf.write("\3Z\3Z\3Z\3[\3[\3[\3[\7[\u024a\n[\f[\16[\u024d\13[\3[")
        buf.write("\3[\3[\3[\3\\\6\\\u0254\n\\\r\\\16\\\u0255\3\\\3\\\4\u023d")
        buf.write("\u024b\2]\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087")
        buf.write("E\u0089F\u008bG\u008dH\u008fI\u0091J\u0093K\u0095L\u0097")
        buf.write("M\u0099N\u009bO\u009d\2\u009f\2\u00a1P\u00a3\2\u00a5Q")
        buf.write("\u00a7\2\u00a9R\u00abS\u00adT\u00afU\u00b1V\u00b3W\u00b5")
        buf.write("X\u00b7Y\3\2\13\3\2\62;\6\2NNWWnnww\6\2HHNNhhnn\6\2\f")
        buf.write("\f$$))^^\f\2$$))AA^^cdhhppttvvxx\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\6\2\60\61C\\aac|\5\2\13\f\17\17\"\"\2\u0262\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2")
        buf.write("\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3")
        buf.write("\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u00a1\3\2\2\2\2\u00a5")
        buf.write("\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2")
        buf.write("\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5")
        buf.write("\3\2\2\2\2\u00b7\3\2\2\2\3\u00b9\3\2\2\2\5\u00be\3\2\2")
        buf.write("\2\7\u00c4\3\2\2\2\t\u00c9\3\2\2\2\13\u00ce\3\2\2\2\r")
        buf.write("\u00d4\3\2\2\2\17\u00dd\3\2\2\2\21\u00e5\3\2\2\2\23\u00e8")
        buf.write("\3\2\2\2\25\u00ef\3\2\2\2\27\u00f4\3\2\2\2\31\u00f9\3")
        buf.write("\2\2\2\33\u0100\3\2\2\2\35\u0106\3\2\2\2\37\u010a\3\2")
        buf.write("\2\2!\u010f\3\2\2\2#\u0112\3\2\2\2%\u0116\3\2\2\2\'\u011b")
        buf.write("\3\2\2\2)\u0124\3\2\2\2+\u012b\3\2\2\2-\u0131\3\2\2\2")
        buf.write("/\u0138\3\2\2\2\61\u013f\3\2\2\2\63\u0146\3\2\2\2\65\u014d")
        buf.write("\3\2\2\2\67\u0154\3\2\2\29\u015c\3\2\2\2;\u0162\3\2\2")
        buf.write("\2=\u016b\3\2\2\2?\u0170\3\2\2\2A\u0179\3\2\2\2C\u017f")
        buf.write("\3\2\2\2E\u0181\3\2\2\2G\u0184\3\2\2\2I\u0187\3\2\2\2")
        buf.write("K\u018a\3\2\2\2M\u018d\3\2\2\2O\u0190\3\2\2\2Q\u0193\3")
        buf.write("\2\2\2S\u0196\3\2\2\2U\u0199\3\2\2\2W\u019d\3\2\2\2Y\u01a1")
        buf.write("\3\2\2\2[\u01a4\3\2\2\2]\u01a7\3\2\2\2_\u01a9\3\2\2\2")
        buf.write("a\u01ab\3\2\2\2c\u01ad\3\2\2\2e\u01af\3\2\2\2g\u01b1\3")
        buf.write("\2\2\2i\u01b3\3\2\2\2k\u01b5\3\2\2\2m\u01b7\3\2\2\2o\u01b9")
        buf.write("\3\2\2\2q\u01bc\3\2\2\2s\u01bf\3\2\2\2u\u01c1\3\2\2\2")
        buf.write("w\u01c4\3\2\2\2y\u01c7\3\2\2\2{\u01ca\3\2\2\2}\u01cd\3")
        buf.write("\2\2\2\177\u01cf\3\2\2\2\u0081\u01d2\3\2\2\2\u0083\u01d4")
        buf.write("\3\2\2\2\u0085\u01d7\3\2\2\2\u0087\u01d9\3\2\2\2\u0089")
        buf.write("\u01dc\3\2\2\2\u008b\u01de\3\2\2\2\u008d\u01e0\3\2\2\2")
        buf.write("\u008f\u01e2\3\2\2\2\u0091\u01e4\3\2\2\2\u0093\u01e6\3")
        buf.write("\2\2\2\u0095\u01e8\3\2\2\2\u0097\u01ea\3\2\2\2\u0099\u01ec")
        buf.write("\3\2\2\2\u009b\u01ee\3\2\2\2\u009d\u01f1\3\2\2\2\u009f")
        buf.write("\u01f5\3\2\2\2\u00a1\u01f7\3\2\2\2\u00a3\u01fb\3\2\2\2")
        buf.write("\u00a5\u0200\3\2\2\2\u00a7\u020f\3\2\2\2\u00a9\u0211\3")
        buf.write("\2\2\2\u00ab\u0218\3\2\2\2\u00ad\u0222\3\2\2\2\u00af\u0229")
        buf.write("\3\2\2\2\u00b1\u0233\3\2\2\2\u00b3\u0237\3\2\2\2\u00b5")
        buf.write("\u0245\3\2\2\2\u00b7\u0253\3\2\2\2\u00b9\u00ba\7c\2\2")
        buf.write("\u00ba\u00bb\7w\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7q")
        buf.write("\2\2\u00bd\4\3\2\2\2\u00be\u00bf\7d\2\2\u00bf\u00c0\7")
        buf.write("t\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3")
        buf.write("\7m\2\2\u00c3\6\3\2\2\2\u00c4\u00c5\7e\2\2\u00c5\u00c6")
        buf.write("\7c\2\2\u00c6\u00c7\7u\2\2\u00c7\u00c8\7g\2\2\u00c8\b")
        buf.write("\3\2\2\2\u00c9\u00ca\7e\2\2\u00ca\u00cb\7j\2\2\u00cb\u00cc")
        buf.write("\7c\2\2\u00cc\u00cd\7t\2\2\u00cd\n\3\2\2\2\u00ce\u00cf")
        buf.write("\7e\2\2\u00cf\u00d0\7q\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2")
        buf.write("\7u\2\2\u00d2\u00d3\7v\2\2\u00d3\f\3\2\2\2\u00d4\u00d5")
        buf.write("\7e\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8")
        buf.write("\7v\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da\7p\2\2\u00da\u00db")
        buf.write("\7w\2\2\u00db\u00dc\7g\2\2\u00dc\16\3\2\2\2\u00dd\u00de")
        buf.write("\7f\2\2\u00de\u00df\7g\2\2\u00df\u00e0\7h\2\2\u00e0\u00e1")
        buf.write("\7c\2\2\u00e1\u00e2\7w\2\2\u00e2\u00e3\7n\2\2\u00e3\u00e4")
        buf.write("\7v\2\2\u00e4\20\3\2\2\2\u00e5\u00e6\7f\2\2\u00e6\u00e7")
        buf.write("\7q\2\2\u00e7\22\3\2\2\2\u00e8\u00e9\7f\2\2\u00e9\u00ea")
        buf.write("\7q\2\2\u00ea\u00eb\7w\2\2\u00eb\u00ec\7d\2\2\u00ec\u00ed")
        buf.write("\7n\2\2\u00ed\u00ee\7g\2\2\u00ee\24\3\2\2\2\u00ef\u00f0")
        buf.write("\7g\2\2\u00f0\u00f1\7n\2\2\u00f1\u00f2\7u\2\2\u00f2\u00f3")
        buf.write("\7g\2\2\u00f3\26\3\2\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6")
        buf.write("\7p\2\2\u00f6\u00f7\7w\2\2\u00f7\u00f8\7o\2\2\u00f8\30")
        buf.write("\3\2\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7z\2\2\u00fb\u00fc")
        buf.write("\7v\2\2\u00fc\u00fd\7g\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff")
        buf.write("\7p\2\2\u00ff\32\3\2\2\2\u0100\u0101\7h\2\2\u0101\u0102")
        buf.write("\7n\2\2\u0102\u0103\7q\2\2\u0103\u0104\7c\2\2\u0104\u0105")
        buf.write("\7v\2\2\u0105\34\3\2\2\2\u0106\u0107\7h\2\2\u0107\u0108")
        buf.write("\7q\2\2\u0108\u0109\7t\2\2\u0109\36\3\2\2\2\u010a\u010b")
        buf.write("\7i\2\2\u010b\u010c\7q\2\2\u010c\u010d\7v\2\2\u010d\u010e")
        buf.write("\7q\2\2\u010e \3\2\2\2\u010f\u0110\7k\2\2\u0110\u0111")
        buf.write("\7h\2\2\u0111\"\3\2\2\2\u0112\u0113\7k\2\2\u0113\u0114")
        buf.write("\7p\2\2\u0114\u0115\7v\2\2\u0115$\3\2\2\2\u0116\u0117")
        buf.write("\7n\2\2\u0117\u0118\7q\2\2\u0118\u0119\7p\2\2\u0119\u011a")
        buf.write("\7i\2\2\u011a&\3\2\2\2\u011b\u011c\7t\2\2\u011c\u011d")
        buf.write("\7g\2\2\u011d\u011e\7i\2\2\u011e\u011f\7k\2\2\u011f\u0120")
        buf.write("\7u\2\2\u0120\u0121\7v\2\2\u0121\u0122\7g\2\2\u0122\u0123")
        buf.write("\7t\2\2\u0123(\3\2\2\2\u0124\u0125\7t\2\2\u0125\u0126")
        buf.write("\7g\2\2\u0126\u0127\7v\2\2\u0127\u0128\7w\2\2\u0128\u0129")
        buf.write("\7t\2\2\u0129\u012a\7p\2\2\u012a*\3\2\2\2\u012b\u012c")
        buf.write("\7u\2\2\u012c\u012d\7j\2\2\u012d\u012e\7q\2\2\u012e\u012f")
        buf.write("\7t\2\2\u012f\u0130\7v\2\2\u0130,\3\2\2\2\u0131\u0132")
        buf.write("\7u\2\2\u0132\u0133\7k\2\2\u0133\u0134\7i\2\2\u0134\u0135")
        buf.write("\7p\2\2\u0135\u0136\7g\2\2\u0136\u0137\7f\2\2\u0137.\3")
        buf.write("\2\2\2\u0138\u0139\7u\2\2\u0139\u013a\7k\2\2\u013a\u013b")
        buf.write("\7|\2\2\u013b\u013c\7g\2\2\u013c\u013d\7q\2\2\u013d\u013e")
        buf.write("\7h\2\2\u013e\60\3\2\2\2\u013f\u0140\7u\2\2\u0140\u0141")
        buf.write("\7v\2\2\u0141\u0142\7c\2\2\u0142\u0143\7v\2\2\u0143\u0144")
        buf.write("\7k\2\2\u0144\u0145\7e\2\2\u0145\62\3\2\2\2\u0146\u0147")
        buf.write("\7u\2\2\u0147\u0148\7v\2\2\u0148\u0149\7t\2\2\u0149\u014a")
        buf.write("\7w\2\2\u014a\u014b\7e\2\2\u014b\u014c\7v\2\2\u014c\64")
        buf.write("\3\2\2\2\u014d\u014e\7u\2\2\u014e\u014f\7y\2\2\u014f\u0150")
        buf.write("\7k\2\2\u0150\u0151\7v\2\2\u0151\u0152\7e\2\2\u0152\u0153")
        buf.write("\7j\2\2\u0153\66\3\2\2\2\u0154\u0155\7v\2\2\u0155\u0156")
        buf.write("\7{\2\2\u0156\u0157\7r\2\2\u0157\u0158\7g\2\2\u0158\u0159")
        buf.write("\7f\2\2\u0159\u015a\7g\2\2\u015a\u015b\7h\2\2\u015b8\3")
        buf.write("\2\2\2\u015c\u015d\7w\2\2\u015d\u015e\7p\2\2\u015e\u015f")
        buf.write("\7k\2\2\u015f\u0160\7q\2\2\u0160\u0161\7p\2\2\u0161:\3")
        buf.write("\2\2\2\u0162\u0163\7w\2\2\u0163\u0164\7p\2\2\u0164\u0165")
        buf.write("\7u\2\2\u0165\u0166\7k\2\2\u0166\u0167\7i\2\2\u0167\u0168")
        buf.write("\7p\2\2\u0168\u0169\7g\2\2\u0169\u016a\7f\2\2\u016a<\3")
        buf.write("\2\2\2\u016b\u016c\7x\2\2\u016c\u016d\7q\2\2\u016d\u016e")
        buf.write("\7k\2\2\u016e\u016f\7f\2\2\u016f>\3\2\2\2\u0170\u0171")
        buf.write("\7x\2\2\u0171\u0172\7q\2\2\u0172\u0173\7n\2\2\u0173\u0174")
        buf.write("\7c\2\2\u0174\u0175\7v\2\2\u0175\u0176\7k\2\2\u0176\u0177")
        buf.write("\7n\2\2\u0177\u0178\7g\2\2\u0178@\3\2\2\2\u0179\u017a")
        buf.write("\7y\2\2\u017a\u017b\7j\2\2\u017b\u017c\7k\2\2\u017c\u017d")
        buf.write("\7n\2\2\u017d\u017e\7g\2\2\u017eB\3\2\2\2\u017f\u0180")
        buf.write("\7?\2\2\u0180D\3\2\2\2\u0181\u0182\7-\2\2\u0182\u0183")
        buf.write("\7?\2\2\u0183F\3\2\2\2\u0184\u0185\7/\2\2\u0185\u0186")
        buf.write("\7?\2\2\u0186H\3\2\2\2\u0187\u0188\7,\2\2\u0188\u0189")
        buf.write("\7?\2\2\u0189J\3\2\2\2\u018a\u018b\7\61\2\2\u018b\u018c")
        buf.write("\7?\2\2\u018cL\3\2\2\2\u018d\u018e\7\'\2\2\u018e\u018f")
        buf.write("\7?\2\2\u018fN\3\2\2\2\u0190\u0191\7(\2\2\u0191\u0192")
        buf.write("\7?\2\2\u0192P\3\2\2\2\u0193\u0194\7~\2\2\u0194\u0195")
        buf.write("\7?\2\2\u0195R\3\2\2\2\u0196\u0197\7`\2\2\u0197\u0198")
        buf.write("\7?\2\2\u0198T\3\2\2\2\u0199\u019a\7>\2\2\u019a\u019b")
        buf.write("\7>\2\2\u019b\u019c\7?\2\2\u019cV\3\2\2\2\u019d\u019e")
        buf.write("\7@\2\2\u019e\u019f\7@\2\2\u019f\u01a0\7?\2\2\u01a0X\3")
        buf.write("\2\2\2\u01a1\u01a2\7-\2\2\u01a2\u01a3\7-\2\2\u01a3Z\3")
        buf.write("\2\2\2\u01a4\u01a5\7/\2\2\u01a5\u01a6\7/\2\2\u01a6\\\3")
        buf.write("\2\2\2\u01a7\u01a8\7-\2\2\u01a8^\3\2\2\2\u01a9\u01aa\7")
        buf.write("/\2\2\u01aa`\3\2\2\2\u01ab\u01ac\7,\2\2\u01acb\3\2\2\2")
        buf.write("\u01ad\u01ae\7\61\2\2\u01aed\3\2\2\2\u01af\u01b0\7\'\2")
        buf.write("\2\u01b0f\3\2\2\2\u01b1\u01b2\7\u0080\2\2\u01b2h\3\2\2")
        buf.write("\2\u01b3\u01b4\7(\2\2\u01b4j\3\2\2\2\u01b5\u01b6\7~\2")
        buf.write("\2\u01b6l\3\2\2\2\u01b7\u01b8\7`\2\2\u01b8n\3\2\2\2\u01b9")
        buf.write("\u01ba\7>\2\2\u01ba\u01bb\7>\2\2\u01bbp\3\2\2\2\u01bc")
        buf.write("\u01bd\7@\2\2\u01bd\u01be\7@\2\2\u01ber\3\2\2\2\u01bf")
        buf.write("\u01c0\7#\2\2\u01c0t\3\2\2\2\u01c1\u01c2\7(\2\2\u01c2")
        buf.write("\u01c3\7(\2\2\u01c3v\3\2\2\2\u01c4\u01c5\7~\2\2\u01c5")
        buf.write("\u01c6\7~\2\2\u01c6x\3\2\2\2\u01c7\u01c8\7?\2\2\u01c8")
        buf.write("\u01c9\7?\2\2\u01c9z\3\2\2\2\u01ca\u01cb\7#\2\2\u01cb")
        buf.write("\u01cc\7?\2\2\u01cc|\3\2\2\2\u01cd\u01ce\7>\2\2\u01ce")
        buf.write("~\3\2\2\2\u01cf\u01d0\7>\2\2\u01d0\u01d1\7?\2\2\u01d1")
        buf.write("\u0080\3\2\2\2\u01d2\u01d3\7@\2\2\u01d3\u0082\3\2\2\2")
        buf.write("\u01d4\u01d5\7@\2\2\u01d5\u01d6\7?\2\2\u01d6\u0084\3\2")
        buf.write("\2\2\u01d7\u01d8\7\60\2\2\u01d8\u0086\3\2\2\2\u01d9\u01da")
        buf.write("\7/\2\2\u01da\u01db\7@\2\2\u01db\u0088\3\2\2\2\u01dc\u01dd")
        buf.write("\7A\2\2\u01dd\u008a\3\2\2\2\u01de\u01df\7*\2\2\u01df\u008c")
        buf.write("\3\2\2\2\u01e0\u01e1\7+\2\2\u01e1\u008e\3\2\2\2\u01e2")
        buf.write("\u01e3\7]\2\2\u01e3\u0090\3\2\2\2\u01e4\u01e5\7_\2\2\u01e5")
        buf.write("\u0092\3\2\2\2\u01e6\u01e7\7}\2\2\u01e7\u0094\3\2\2\2")
        buf.write("\u01e8\u01e9\7\177\2\2\u01e9\u0096\3\2\2\2\u01ea\u01eb")
        buf.write("\7<\2\2\u01eb\u0098\3\2\2\2\u01ec\u01ed\7=\2\2\u01ed\u009a")
        buf.write("\3\2\2\2\u01ee\u01ef\7.\2\2\u01ef\u009c\3\2\2\2\u01f0")
        buf.write("\u01f2\t\2\2\2\u01f1\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2")
        buf.write("\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u009e\3")
        buf.write("\2\2\2\u01f5\u01f6\t\3\2\2\u01f6\u00a0\3\2\2\2\u01f7\u01f9")
        buf.write("\5\u009dO\2\u01f8\u01fa\5\u009fP\2\u01f9\u01f8\3\2\2\2")
        buf.write("\u01f9\u01fa\3\2\2\2\u01fa\u00a2\3\2\2\2\u01fb\u01fc\t")
        buf.write("\4\2\2\u01fc\u00a4\3\2\2\2\u01fd\u01ff\t\2\2\2\u01fe\u01fd")
        buf.write("\3\2\2\2\u01ff\u0202\3\2\2\2\u0200\u01fe\3\2\2\2\u0200")
        buf.write("\u0201\3\2\2\2\u0201\u0203\3\2\2\2\u0202\u0200\3\2\2\2")
        buf.write("\u0203\u0205\7\60\2\2\u0204\u0206\t\2\2\2\u0205\u0204")
        buf.write("\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0205\3\2\2\2\u0207")
        buf.write("\u0208\3\2\2\2\u0208\u020a\3\2\2\2\u0209\u020b\5\u00a3")
        buf.write("R\2\u020a\u0209\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u00a6")
        buf.write("\3\2\2\2\u020c\u0210\n\5\2\2\u020d\u020e\7^\2\2\u020e")
        buf.write("\u0210\t\6\2\2\u020f\u020c\3\2\2\2\u020f\u020d\3\2\2\2")
        buf.write("\u0210\u00a8\3\2\2\2\u0211\u0214\7)\2\2\u0212\u0215\5")
        buf.write("\u00a7T\2\u0213\u0215\7$\2\2\u0214\u0212\3\2\2\2\u0214")
        buf.write("\u0213\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0217\7)\2\2")
        buf.write("\u0217\u00aa\3\2\2\2\u0218\u021d\7$\2\2\u0219\u021c\5")
        buf.write("\u00a7T\2\u021a\u021c\7)\2\2\u021b\u0219\3\2\2\2\u021b")
        buf.write("\u021a\3\2\2\2\u021c\u021f\3\2\2\2\u021d\u021b\3\2\2\2")
        buf.write("\u021d\u021e\3\2\2\2\u021e\u0220\3\2\2\2\u021f\u021d\3")
        buf.write("\2\2\2\u0220\u0221\7$\2\2\u0221\u00ac\3\2\2\2\u0222\u0226")
        buf.write("\t\7\2\2\u0223\u0225\t\b\2\2\u0224\u0223\3\2\2\2\u0225")
        buf.write("\u0228\3\2\2\2\u0226\u0224\3\2\2\2\u0226\u0227\3\2\2\2")
        buf.write("\u0227\u00ae\3\2\2\2\u0228\u0226\3\2\2\2\u0229\u022a\7")
        buf.write("%\2\2\u022a\u022b\7k\2\2\u022b\u022c\7p\2\2\u022c\u022d")
        buf.write("\7e\2\2\u022d\u022e\7n\2\2\u022e\u022f\7w\2\2\u022f\u0230")
        buf.write("\7f\2\2\u0230\u0231\7g\2\2\u0231\u00b0\3\2\2\2\u0232\u0234")
        buf.write("\t\t\2\2\u0233\u0232\3\2\2\2\u0234\u0235\3\2\2\2\u0235")
        buf.write("\u0233\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u00b2\3\2\2\2")
        buf.write("\u0237\u0238\7\61\2\2\u0238\u0239\7,\2\2\u0239\u023d\3")
        buf.write("\2\2\2\u023a\u023c\13\2\2\2\u023b\u023a\3\2\2\2\u023c")
        buf.write("\u023f\3\2\2\2\u023d\u023e\3\2\2\2\u023d\u023b\3\2\2\2")
        buf.write("\u023e\u0240\3\2\2\2\u023f\u023d\3\2\2\2\u0240\u0241\7")
        buf.write(",\2\2\u0241\u0242\7\61\2\2\u0242\u0243\3\2\2\2\u0243\u0244")
        buf.write("\bZ\2\2\u0244\u00b4\3\2\2\2\u0245\u0246\7\61\2\2\u0246")
        buf.write("\u0247\7\61\2\2\u0247\u024b\3\2\2\2\u0248\u024a\13\2\2")
        buf.write("\2\u0249\u0248\3\2\2\2\u024a\u024d\3\2\2\2\u024b\u024c")
        buf.write("\3\2\2\2\u024b\u0249\3\2\2\2\u024c\u024e\3\2\2\2\u024d")
        buf.write("\u024b\3\2\2\2\u024e\u024f\7\f\2\2\u024f\u0250\3\2\2\2")
        buf.write("\u0250\u0251\b[\2\2\u0251\u00b6\3\2\2\2\u0252\u0254\t")
        buf.write("\n\2\2\u0253\u0252\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u0253")
        buf.write("\3\2\2\2\u0255\u0256\3\2\2\2\u0256\u0257\3\2\2\2\u0257")
        buf.write("\u0258\b\\\3\2\u0258\u00b8\3\2\2\2\21\2\u01f3\u01f9\u0200")
        buf.write("\u0207\u020a\u020f\u0214\u021b\u021d\u0226\u0235\u023d")
        buf.write("\u024b\u0255\4\2\4\2\b\2\2")
        return buf.getvalue()


class CLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    CASE = 3
    CHAR = 4
    CONST = 5
    CONTINUE = 6
    DEFAULT = 7
    DO = 8
    DOUBLE = 9
    ELSE = 10
    ENUM = 11
    EXTERN = 12
    FLOAT = 13
    FOR = 14
    GOTO = 15
    IF = 16
    INT = 17
    LONG = 18
    REGISTER = 19
    RETURN = 20
    SHORT = 21
    SIGNED = 22
    SIZEOF = 23
    STATIC = 24
    STRUCT = 25
    SWITCH = 26
    TYPEDEF = 27
    UNION = 28
    UNSIGNED = 29
    VOID = 30
    VOLATILE = 31
    WHILE = 32
    ASSIGN_OP = 33
    PLUS_ASSIGN_OP = 34
    MINUS_ASSIGN_OP = 35
    STAR_ASSIGN_OP = 36
    SLASH_ASSIGN_OP = 37
    PERCENT_ASSIGN_OP = 38
    AMPERSAND_ASSIGN_OP = 39
    BAR_ASSIGN_OP = 40
    CARET_ASSIGN_OP = 41
    SHIFTL_ASSIGN_OP = 42
    SHIFTR_ASSING_OP = 43
    INCREMENT_OP = 44
    DECREMENT_OP = 45
    PLUS_OP = 46
    MINUS_OP = 47
    STAR_OP = 48
    SLASH_OP = 49
    PERCENT_OP = 50
    TILDE_OP = 51
    AMPERSAND_OP = 52
    BAR_OP = 53
    CARET_OP = 54
    SHIFTL_OP = 55
    SHIFTR_OP = 56
    NOT_OP = 57
    AND_OP = 58
    OR_OP = 59
    EQ_OP = 60
    NEQ_OP = 61
    LT_OP = 62
    LE_OP = 63
    GT_OP = 64
    GE_OP = 65
    DOT_OP = 66
    ARROW_OP = 67
    QUESTION_OP = 68
    LPAREN = 69
    RPAREN = 70
    LBRACKET = 71
    RBRACKET = 72
    LBRACE = 73
    RBRACE = 74
    COLON = 75
    SEMICOLON = 76
    COMMA = 77
    INT_LITERAL = 78
    REAL_LITERAL = 79
    CHAR_LITERAL = 80
    STRING_LITERAL = 81
    IDENTIFIER = 82
    INCLUDE = 83
    PATH = 84
    COMMENT = 85
    LINE_COMMENT = 86
    WS = 87

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'case'", "'char'", "'const'", "'continue'", 
            "'default'", "'do'", "'double'", "'else'", "'enum'", "'extern'", 
            "'float'", "'for'", "'goto'", "'if'", "'int'", "'long'", "'register'", 
            "'return'", "'short'", "'signed'", "'sizeof'", "'static'", "'struct'", 
            "'switch'", "'typedef'", "'union'", "'unsigned'", "'void'", 
            "'volatile'", "'while'", "'='", "'+='", "'-='", "'*='", "'/='", 
            "'%='", "'&='", "'|='", "'^='", "'<<='", "'>>='", "'++'", "'--'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'~'", "'&'", "'|'", "'^'", 
            "'<<'", "'>>'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'.'", "'->'", "'?'", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "':'", "';'", "','", "'#include'" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "CASE", "CHAR", "CONST", "CONTINUE", "DEFAULT", 
            "DO", "DOUBLE", "ELSE", "ENUM", "EXTERN", "FLOAT", "FOR", "GOTO", 
            "IF", "INT", "LONG", "REGISTER", "RETURN", "SHORT", "SIGNED", 
            "SIZEOF", "STATIC", "STRUCT", "SWITCH", "TYPEDEF", "UNION", 
            "UNSIGNED", "VOID", "VOLATILE", "WHILE", "ASSIGN_OP", "PLUS_ASSIGN_OP", 
            "MINUS_ASSIGN_OP", "STAR_ASSIGN_OP", "SLASH_ASSIGN_OP", "PERCENT_ASSIGN_OP", 
            "AMPERSAND_ASSIGN_OP", "BAR_ASSIGN_OP", "CARET_ASSIGN_OP", "SHIFTL_ASSIGN_OP", 
            "SHIFTR_ASSING_OP", "INCREMENT_OP", "DECREMENT_OP", "PLUS_OP", 
            "MINUS_OP", "STAR_OP", "SLASH_OP", "PERCENT_OP", "TILDE_OP", 
            "AMPERSAND_OP", "BAR_OP", "CARET_OP", "SHIFTL_OP", "SHIFTR_OP", 
            "NOT_OP", "AND_OP", "OR_OP", "EQ_OP", "NEQ_OP", "LT_OP", "LE_OP", 
            "GT_OP", "GE_OP", "DOT_OP", "ARROW_OP", "QUESTION_OP", "LPAREN", 
            "RPAREN", "LBRACKET", "RBRACKET", "LBRACE", "RBRACE", "COLON", 
            "SEMICOLON", "COMMA", "INT_LITERAL", "REAL_LITERAL", "CHAR_LITERAL", 
            "STRING_LITERAL", "IDENTIFIER", "INCLUDE", "PATH", "COMMENT", 
            "LINE_COMMENT", "WS" ]

    ruleNames = [ "AUTO", "BREAK", "CASE", "CHAR", "CONST", "CONTINUE", 
                  "DEFAULT", "DO", "DOUBLE", "ELSE", "ENUM", "EXTERN", "FLOAT", 
                  "FOR", "GOTO", "IF", "INT", "LONG", "REGISTER", "RETURN", 
                  "SHORT", "SIGNED", "SIZEOF", "STATIC", "STRUCT", "SWITCH", 
                  "TYPEDEF", "UNION", "UNSIGNED", "VOID", "VOLATILE", "WHILE", 
                  "ASSIGN_OP", "PLUS_ASSIGN_OP", "MINUS_ASSIGN_OP", "STAR_ASSIGN_OP", 
                  "SLASH_ASSIGN_OP", "PERCENT_ASSIGN_OP", "AMPERSAND_ASSIGN_OP", 
                  "BAR_ASSIGN_OP", "CARET_ASSIGN_OP", "SHIFTL_ASSIGN_OP", 
                  "SHIFTR_ASSING_OP", "INCREMENT_OP", "DECREMENT_OP", "PLUS_OP", 
                  "MINUS_OP", "STAR_OP", "SLASH_OP", "PERCENT_OP", "TILDE_OP", 
                  "AMPERSAND_OP", "BAR_OP", "CARET_OP", "SHIFTL_OP", "SHIFTR_OP", 
                  "NOT_OP", "AND_OP", "OR_OP", "EQ_OP", "NEQ_OP", "LT_OP", 
                  "LE_OP", "GT_OP", "GE_OP", "DOT_OP", "ARROW_OP", "QUESTION_OP", 
                  "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", "LBRACE", 
                  "RBRACE", "COLON", "SEMICOLON", "COMMA", "DEC_LIT", "INT_SUFFIX", 
                  "INT_LITERAL", "REAL_SUFFIX", "REAL_LITERAL", "CCHAR", 
                  "CHAR_LITERAL", "STRING_LITERAL", "IDENTIFIER", "INCLUDE", 
                  "PATH", "COMMENT", "LINE_COMMENT", "WS" ]

    grammarFileName = "C.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


