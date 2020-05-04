# Generated from patito.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from Compiler.compiler import *
from Compiler.function import *
from Compiler.variable import *
from Compiler.quadruple import *
compiler = Compiler()


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38")
        buf.write("\u01ad\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\6\3A\n\3\r\3\16\3B\3\4\3\4\3\4\3\4\5\4I\n")
        buf.write("\4\3\4\3\4\3\4\3\4\5\4O\n\4\3\4\7\4R\n\4\f\4\16\4U\13")
        buf.write("\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\5\6e\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7")
        buf.write("p\n\7\3\b\6\bs\n\b\r\b\16\bt\3\t\3\t\3\t\3\t\3\t\3\t\5")
        buf.write("\t}\n\t\3\t\3\t\5\t\u0081\n\t\3\t\3\t\3\t\5\t\u0086\n")
        buf.write("\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\7\13\u0094\n\13\f\13\16\13\u0097\13\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\5\f\u009f\n\f\3\f\3\f\3\f\7\f\u00a4\n\f")
        buf.write("\f\f\16\f\u00a7\13\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\5\r\u00b7\n\r\3\r\3\r\3\r\5\r\u00bc")
        buf.write("\n\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00c4\n\16\3\16")
        buf.write("\3\16\3\16\7\16\u00c9\n\16\f\16\16\16\u00cc\13\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u00d4\n\17\3\17\3\17\3")
        buf.write("\17\7\17\u00d9\n\17\f\17\16\17\u00dc\13\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00fc\n\20\f\20\16")
        buf.write("\20\u00ff\13\20\5\20\u0101\n\20\3\20\3\20\5\20\u0105\n")
        buf.write("\20\5\20\u0107\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\7\21\u0111\n\21\f\21\16\21\u0114\13\21\3\22\3\22")
        buf.write("\3\22\5\22\u0119\n\22\3\22\3\22\3\22\3\22\3\22\5\22\u0120")
        buf.write("\n\22\3\22\3\22\7\22\u0124\n\22\f\22\16\22\u0127\13\22")
        buf.write("\3\22\3\22\3\22\5\22\u012c\n\22\3\22\3\22\3\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\7\23\u0137\n\23\f\23\16\23\u013a")
        buf.write("\13\23\5\23\u013c\n\23\3\23\3\23\3\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\5\25\u0152\n\25\3\26\3\26\3\26\3\26\5")
        buf.write("\26\u0158\n\26\3\26\3\26\3\26\3\26\5\26\u015e\n\26\3\26")
        buf.write("\7\26\u0161\n\26\f\26\16\26\u0164\13\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0172")
        buf.write("\n\27\f\27\16\27\u0175\13\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\5\30\u0189\n\30\3\30\3\30\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\5\32\u0199")
        buf.write("\n\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\2\2\34\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\2\5\3\2-\61\4\2-\61\67\67\3\2\31\33\2\u01c9\2\66\3\2")
        buf.write("\2\2\4>\3\2\2\2\6D\3\2\2\2\bX\3\2\2\2\nd\3\2\2\2\fo\3")
        buf.write("\2\2\2\16r\3\2\2\2\20v\3\2\2\2\22\u0089\3\2\2\2\24\u008b")
        buf.write("\3\2\2\2\26\u0098\3\2\2\2\30\u00a8\3\2\2\2\32\u00bd\3")
        buf.write("\2\2\2\34\u00cd\3\2\2\2\36\u0106\3\2\2\2 \u0112\3\2\2")
        buf.write("\2\"\u0115\3\2\2\2$\u0130\3\2\2\2&\u0140\3\2\2\2(\u0151")
        buf.write("\3\2\2\2*\u0153\3\2\2\2,\u0168\3\2\2\2.\u0179\3\2\2\2")
        buf.write("\60\u018c\3\2\2\2\62\u0195\3\2\2\2\64\u01a3\3\2\2\2\66")
        buf.write("\67\7\37\2\2\678\78\2\289\7\36\2\29:\5\4\3\2:;\b\2\1\2")
        buf.write(";<\5\16\b\2<=\5\64\33\2=\3\3\2\2\2>@\7,\2\2?A\5\6\4\2")
        buf.write("@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2BC\3\2\2\2C\5\3\2\2\2DE")
        buf.write("\5\b\5\2EF\7\35\2\2FH\78\2\2GI\5\f\7\2HG\3\2\2\2HI\3\2")
        buf.write("\2\2IJ\3\2\2\2JS\b\4\1\2KL\7\34\2\2LN\78\2\2MO\5\f\7\2")
        buf.write("NM\3\2\2\2NO\3\2\2\2OP\3\2\2\2PR\b\4\1\2QK\3\2\2\2RU\3")
        buf.write("\2\2\2SQ\3\2\2\2ST\3\2\2\2TV\3\2\2\2US\3\2\2\2VW\7\36")
        buf.write("\2\2W\7\3\2\2\2XY\t\2\2\2Y\t\3\2\2\2Z[\7\62\2\2[e\b\6")
        buf.write("\1\2\\]\7\63\2\2]e\b\6\1\2^_\7\64\2\2_e\b\6\1\2`a\7\65")
        buf.write("\2\2ae\b\6\1\2bc\7\66\2\2ce\b\6\1\2dZ\3\2\2\2d\\\3\2\2")
        buf.write("\2d^\3\2\2\2d`\3\2\2\2db\3\2\2\2e\13\3\2\2\2fg\7\25\2")
        buf.write("\2gh\7\64\2\2hp\7\26\2\2ij\7\25\2\2jk\7\64\2\2kl\7\26")
        buf.write("\2\2lm\7\25\2\2mn\7\64\2\2np\7\26\2\2of\3\2\2\2oi\3\2")
        buf.write("\2\2p\r\3\2\2\2qs\5\20\t\2rq\3\2\2\2st\3\2\2\2tr\3\2\2")
        buf.write("\2tu\3\2\2\2u\17\3\2\2\2vw\7!\2\2wx\5\22\n\2xy\78\2\2")
        buf.write("yz\b\t\1\2z|\7\23\2\2{}\5\24\13\2|{\3\2\2\2|}\3\2\2\2")
        buf.write("}~\3\2\2\2~\u0080\7\24\2\2\177\u0081\5\4\3\2\u0080\177")
        buf.write("\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082\3\2\2\2\u0082")
        buf.write("\u0083\b\t\1\2\u0083\u0085\7\27\2\2\u0084\u0086\5 \21")
        buf.write("\2\u0085\u0084\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087")
        buf.write("\3\2\2\2\u0087\u0088\7\30\2\2\u0088\21\3\2\2\2\u0089\u008a")
        buf.write("\t\3\2\2\u008a\23\3\2\2\2\u008b\u008c\5\b\5\2\u008c\u008d")
        buf.write("\78\2\2\u008d\u0095\b\13\1\2\u008e\u008f\7\34\2\2\u008f")
        buf.write("\u0090\5\b\5\2\u0090\u0091\78\2\2\u0091\u0092\b\13\1\2")
        buf.write("\u0092\u0094\3\2\2\2\u0093\u008e\3\2\2\2\u0094\u0097\3")
        buf.write("\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\25")
        buf.write("\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u0099\5\30\r\2\u0099")
        buf.write("\u00a5\b\f\1\2\u009a\u009b\7\r\2\2\u009b\u009f\b\f\1\2")
        buf.write("\u009c\u009d\7\16\2\2\u009d\u009f\b\f\1\2\u009e\u009a")
        buf.write("\3\2\2\2\u009e\u009c\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0")
        buf.write("\u00a1\5\26\f\2\u00a1\u00a2\b\f\1\2\u00a2\u00a4\3\2\2")
        buf.write("\2\u00a3\u009e\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3")
        buf.write("\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\27\3\2\2\2\u00a7\u00a5")
        buf.write("\3\2\2\2\u00a8\u00a9\5\32\16\2\u00a9\u00bb\b\r\1\2\u00aa")
        buf.write("\u00ab\7\7\2\2\u00ab\u00b7\b\r\1\2\u00ac\u00ad\7\6\2\2")
        buf.write("\u00ad\u00b7\b\r\1\2\u00ae\u00af\7\t\2\2\u00af\u00b7\b")
        buf.write("\r\1\2\u00b0\u00b1\7\b\2\2\u00b1\u00b7\b\r\1\2\u00b2\u00b3")
        buf.write("\7\13\2\2\u00b3\u00b7\b\r\1\2\u00b4\u00b5\7\n\2\2\u00b5")
        buf.write("\u00b7\b\r\1\2\u00b6\u00aa\3\2\2\2\u00b6\u00ac\3\2\2\2")
        buf.write("\u00b6\u00ae\3\2\2\2\u00b6\u00b0\3\2\2\2\u00b6\u00b2\3")
        buf.write("\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9")
        buf.write("\5\30\r\2\u00b9\u00ba\b\r\1\2\u00ba\u00bc\3\2\2\2\u00bb")
        buf.write("\u00b6\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\31\3\2\2\2\u00bd")
        buf.write("\u00be\5\34\17\2\u00be\u00ca\b\16\1\2\u00bf\u00c0\7\17")
        buf.write("\2\2\u00c0\u00c4\b\16\1\2\u00c1\u00c2\7\20\2\2\u00c2\u00c4")
        buf.write("\b\16\1\2\u00c3\u00bf\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4")
        buf.write("\u00c5\3\2\2\2\u00c5\u00c6\5\32\16\2\u00c6\u00c7\b\16")
        buf.write("\1\2\u00c7\u00c9\3\2\2\2\u00c8\u00c3\3\2\2\2\u00c9\u00cc")
        buf.write("\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb")
        buf.write("\33\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce\5\36\20\2")
        buf.write("\u00ce\u00da\b\17\1\2\u00cf\u00d0\7\21\2\2\u00d0\u00d4")
        buf.write("\b\17\1\2\u00d1\u00d2\7\22\2\2\u00d2\u00d4\b\17\1\2\u00d3")
        buf.write("\u00cf\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00d5\3\2\2\2")
        buf.write("\u00d5\u00d6\5\34\17\2\u00d6\u00d7\b\17\1\2\u00d7\u00d9")
        buf.write("\3\2\2\2\u00d8\u00d3\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da")
        buf.write("\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db\35\3\2\2\2\u00dc")
        buf.write("\u00da\3\2\2\2\u00dd\u00de\5\n\6\2\u00de\u00df\b\20\1")
        buf.write("\2\u00df\u0107\3\2\2\2\u00e0\u00e1\7\23\2\2\u00e1\u00e2")
        buf.write("\b\20\1\2\u00e2\u00e3\5\26\f\2\u00e3\u00e4\7\24\2\2\u00e4")
        buf.write("\u00e5\b\20\1\2\u00e5\u0107\3\2\2\2\u00e6\u00e7\78\2\2")
        buf.write("\u00e7\u0104\b\20\1\2\u00e8\u0105\3\2\2\2\u00e9\u0105")
        buf.write("\t\4\2\2\u00ea\u00eb\7\25\2\2\u00eb\u00ec\5\26\f\2\u00ec")
        buf.write("\u00ed\7\26\2\2\u00ed\u0105\3\2\2\2\u00ee\u00ef\7\25\2")
        buf.write("\2\u00ef\u00f0\5\26\f\2\u00f0\u00f1\7\26\2\2\u00f1\u00f2")
        buf.write("\7\25\2\2\u00f2\u00f3\5\26\f\2\u00f3\u00f4\7\26\2\2\u00f4")
        buf.write("\u0105\3\2\2\2\u00f5\u00f6\7\23\2\2\u00f6\u0100\b\20\1")
        buf.write("\2\u00f7\u0101\3\2\2\2\u00f8\u00fd\5\26\f\2\u00f9\u00fa")
        buf.write("\7\34\2\2\u00fa\u00fc\5\26\f\2\u00fb\u00f9\3\2\2\2\u00fc")
        buf.write("\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2")
        buf.write("\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100\u00f7\3")
        buf.write("\2\2\2\u0100\u00f8\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0103")
        buf.write("\7\24\2\2\u0103\u0105\b\20\1\2\u0104\u00e8\3\2\2\2\u0104")
        buf.write("\u00e9\3\2\2\2\u0104\u00ea\3\2\2\2\u0104\u00ee\3\2\2\2")
        buf.write("\u0104\u00f5\3\2\2\2\u0105\u0107\3\2\2\2\u0106\u00dd\3")
        buf.write("\2\2\2\u0106\u00e0\3\2\2\2\u0106\u00e6\3\2\2\2\u0107\37")
        buf.write("\3\2\2\2\u0108\u0111\5\"\22\2\u0109\u0111\5$\23\2\u010a")
        buf.write("\u0111\5&\24\2\u010b\u0111\5*\26\2\u010c\u0111\5,\27\2")
        buf.write("\u010d\u0111\5.\30\2\u010e\u0111\5\60\31\2\u010f\u0111")
        buf.write("\5\62\32\2\u0110\u0108\3\2\2\2\u0110\u0109\3\2\2\2\u0110")
        buf.write("\u010a\3\2\2\2\u0110\u010b\3\2\2\2\u0110\u010c\3\2\2\2")
        buf.write("\u0110\u010d\3\2\2\2\u0110\u010e\3\2\2\2\u0110\u010f\3")
        buf.write("\2\2\2\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113")
        buf.write("\3\2\2\2\u0113!\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0116")
        buf.write("\78\2\2\u0116\u0118\b\22\1\2\u0117\u0119\5(\25\2\u0118")
        buf.write("\u0117\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011a\3\2\2\2")
        buf.write("\u011a\u011b\7\f\2\2\u011b\u0125\b\22\1\2\u011c\u011d")
        buf.write("\78\2\2\u011d\u011f\b\22\1\2\u011e\u0120\5(\25\2\u011f")
        buf.write("\u011e\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0121\3\2\2\2")
        buf.write("\u0121\u0122\7\f\2\2\u0122\u0124\b\22\1\2\u0123\u011c")
        buf.write("\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125")
        buf.write("\u0126\3\2\2\2\u0126\u012b\3\2\2\2\u0127\u0125\3\2\2\2")
        buf.write("\u0128\u0129\78\2\2\u0129\u012c\b\22\1\2\u012a\u012c\5")
        buf.write("\26\f\2\u012b\u0128\3\2\2\2\u012b\u012a\3\2\2\2\u012c")
        buf.write("\u012d\3\2\2\2\u012d\u012e\7\36\2\2\u012e\u012f\b\22\1")
        buf.write("\2\u012f#\3\2\2\2\u0130\u0131\78\2\2\u0131\u013b\7\23")
        buf.write("\2\2\u0132\u013c\3\2\2\2\u0133\u0138\5\26\f\2\u0134\u0135")
        buf.write("\7\34\2\2\u0135\u0137\5\26\f\2\u0136\u0134\3\2\2\2\u0137")
        buf.write("\u013a\3\2\2\2\u0138\u0136\3\2\2\2\u0138\u0139\3\2\2\2")
        buf.write("\u0139\u013c\3\2\2\2\u013a\u0138\3\2\2\2\u013b\u0132\3")
        buf.write("\2\2\2\u013b\u0133\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013e")
        buf.write("\7\24\2\2\u013e\u013f\7\36\2\2\u013f%\3\2\2\2\u0140\u0141")
        buf.write("\7\"\2\2\u0141\u0142\7\23\2\2\u0142\u0143\5\26\f\2\u0143")
        buf.write("\u0144\7\24\2\2\u0144\u0145\7\36\2\2\u0145\'\3\2\2\2\u0146")
        buf.write("\u0147\7\25\2\2\u0147\u0148\5\26\f\2\u0148\u0149\7\26")
        buf.write("\2\2\u0149\u0152\3\2\2\2\u014a\u014b\7\25\2\2\u014b\u014c")
        buf.write("\5\26\f\2\u014c\u014d\7\26\2\2\u014d\u014e\7\25\2\2\u014e")
        buf.write("\u014f\5\26\f\2\u014f\u0150\7\26\2\2\u0150\u0152\3\2\2")
        buf.write("\2\u0151\u0146\3\2\2\2\u0151\u014a\3\2\2\2\u0152)\3\2")
        buf.write("\2\2\u0153\u0154\7#\2\2\u0154\u0155\7\23\2\2\u0155\u0157")
        buf.write("\78\2\2\u0156\u0158\5(\25\2\u0157\u0156\3\2\2\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u0162\b\26\1")
        buf.write("\2\u015a\u015b\7\34\2\2\u015b\u015d\78\2\2\u015c\u015e")
        buf.write("\5(\25\2\u015d\u015c\3\2\2\2\u015d\u015e\3\2\2\2\u015e")
        buf.write("\u015f\3\2\2\2\u015f\u0161\b\26\1\2\u0160\u015a\3\2\2")
        buf.write("\2\u0161\u0164\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163")
        buf.write("\3\2\2\2\u0163\u0165\3\2\2\2\u0164\u0162\3\2\2\2\u0165")
        buf.write("\u0166\7\24\2\2\u0166\u0167\7\36\2\2\u0167+\3\2\2\2\u0168")
        buf.write("\u0169\7$\2\2\u0169\u016a\7\23\2\2\u016a\u016b\5\26\f")
        buf.write("\2\u016b\u016c\b\27\1\2\u016c\u0173\3\2\2\2\u016d\u016e")
        buf.write("\7\34\2\2\u016e\u016f\5\26\f\2\u016f\u0170\b\27\1\2\u0170")
        buf.write("\u0172\3\2\2\2\u0171\u016d\3\2\2\2\u0172\u0175\3\2\2\2")
        buf.write("\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0176\3")
        buf.write("\2\2\2\u0175\u0173\3\2\2\2\u0176\u0177\7\24\2\2\u0177")
        buf.write("\u0178\7\36\2\2\u0178-\3\2\2\2\u0179\u017a\7%\2\2\u017a")
        buf.write("\u017b\7\23\2\2\u017b\u017c\5\26\f\2\u017c\u017d\7\24")
        buf.write("\2\2\u017d\u017e\b\30\1\2\u017e\u017f\7&\2\2\u017f\u0180")
        buf.write("\7\27\2\2\u0180\u0181\5 \21\2\u0181\u0188\7\30\2\2\u0182")
        buf.write("\u0183\7\'\2\2\u0183\u0184\b\30\1\2\u0184\u0185\7\27\2")
        buf.write("\2\u0185\u0186\5 \21\2\u0186\u0187\7\30\2\2\u0187\u0189")
        buf.write("\3\2\2\2\u0188\u0182\3\2\2\2\u0188\u0189\3\2\2\2\u0189")
        buf.write("\u018a\3\2\2\2\u018a\u018b\b\30\1\2\u018b/\3\2\2\2\u018c")
        buf.write("\u018d\7(\2\2\u018d\u018e\7\23\2\2\u018e\u018f\5\26\f")
        buf.write("\2\u018f\u0190\7\24\2\2\u0190\u0191\7)\2\2\u0191\u0192")
        buf.write("\7\27\2\2\u0192\u0193\5 \21\2\u0193\u0194\7\30\2\2\u0194")
        buf.write("\61\3\2\2\2\u0195\u0196\7*\2\2\u0196\u0198\78\2\2\u0197")
        buf.write("\u0199\5(\25\2\u0198\u0197\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199\u019a\3\2\2\2\u019a\u019b\7\f\2\2\u019b\u019c\5")
        buf.write("\26\f\2\u019c\u019d\7+\2\2\u019d\u019e\5\26\f\2\u019e")
        buf.write("\u019f\7)\2\2\u019f\u01a0\7\27\2\2\u01a0\u01a1\5 \21\2")
        buf.write("\u01a1\u01a2\7\30\2\2\u01a2\63\3\2\2\2\u01a3\u01a4\7 ")
        buf.write("\2\2\u01a4\u01a5\b\33\1\2\u01a5\u01a6\7\23\2\2\u01a6\u01a7")
        buf.write("\7\24\2\2\u01a7\u01a8\b\33\1\2\u01a8\u01a9\7\27\2\2\u01a9")
        buf.write("\u01aa\5 \21\2\u01aa\u01ab\7\30\2\2\u01ab\65\3\2\2\2(")
        buf.write("BHNSdot|\u0080\u0085\u0095\u009e\u00a5\u00b6\u00bb\u00c3")
        buf.write("\u00ca\u00d3\u00da\u00fd\u0100\u0104\u0106\u0110\u0112")
        buf.write("\u0118\u011f\u0125\u012b\u0138\u013b\u0151\u0157\u015d")
        buf.write("\u0162\u0173\u0188\u0198")
        return buf.getvalue()


class patitoParser ( Parser ):

    grammarFileName = "patito.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", "'='", 
                     "'&&'", "'||'", "'+'", "'-'", "'*'", "'/'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "'$'", "'\u00A1'", 
                     "'?'", "','", "':'", "';'", "'program'", "'main'", 
                     "'function'", "'return'", "'input'", "'print'", "'if'", 
                     "'then'", "'else'", "'while'", "'do'", "'from'", "'to'", 
                     "'var'", "'bool'", "'int'", "'float'", "'string'", 
                     "'char'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'void'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "LINE_COMMENT", "WS", "LESS", 
                      "GREATER", "LESS_EQUAL", "GREATER_EQUAL", "EQUAL", 
                      "NOT_EQUAL", "ASSIGN", "AND", "OR", "ADD", "SUB", 
                      "MULT", "DIV", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", 
                      "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_CURLY", "RIGHT_CURLY", 
                      "DETERMINANT", "TRANSPOSE", "INVERSE", "COMMA", "COLON", 
                      "SEMICOLON", "PROGRAM", "MAIN", "FUNCTION", "RETURN", 
                      "INPUT", "PRINT", "IF", "THEN", "ELSE", "WHILE", "DO", 
                      "FROM", "TO", "VAR", "BOOL", "INT", "FLOAT", "STRING", 
                      "CHAR", "CTE_BOOL", "CTE_FLOAT", "CTE_INT", "CTE_CHAR", 
                      "CTE_STRING", "VOID", "ID" ]

    RULE_program = 0
    RULE_declarevars = 1
    RULE_variables = 2
    RULE_vartypes = 3
    RULE_constant = 4
    RULE_arrayconstant = 5
    RULE_functions = 6
    RULE_function = 7
    RULE_functiontype = 8
    RULE_parameters = 9
    RULE_mexp = 10
    RULE_sexp = 11
    RULE_exp = 12
    RULE_term = 13
    RULE_factor = 14
    RULE_statute = 15
    RULE_assignation = 16
    RULE_voidcall = 17
    RULE_returncall = 18
    RULE_indexvariable = 19
    RULE_read = 20
    RULE_write = 21
    RULE_conditional = 22
    RULE_whileloop = 23
    RULE_fromloop = 24
    RULE_mainfunc = 25

    ruleNames =  [ "program", "declarevars", "variables", "vartypes", "constant", 
                   "arrayconstant", "functions", "function", "functiontype", 
                   "parameters", "mexp", "sexp", "exp", "term", "factor", 
                   "statute", "assignation", "voidcall", "returncall", "indexvariable", 
                   "read", "write", "conditional", "whileloop", "fromloop", 
                   "mainfunc" ]

    EOF = Token.EOF
    COMMENT=1
    LINE_COMMENT=2
    WS=3
    LESS=4
    GREATER=5
    LESS_EQUAL=6
    GREATER_EQUAL=7
    EQUAL=8
    NOT_EQUAL=9
    ASSIGN=10
    AND=11
    OR=12
    ADD=13
    SUB=14
    MULT=15
    DIV=16
    LEFT_PARENTHESIS=17
    RIGHT_PARENTHESIS=18
    LEFT_BRACKET=19
    RIGHT_BRACKET=20
    LEFT_CURLY=21
    RIGHT_CURLY=22
    DETERMINANT=23
    TRANSPOSE=24
    INVERSE=25
    COMMA=26
    COLON=27
    SEMICOLON=28
    PROGRAM=29
    MAIN=30
    FUNCTION=31
    RETURN=32
    INPUT=33
    PRINT=34
    IF=35
    THEN=36
    ELSE=37
    WHILE=38
    DO=39
    FROM=40
    TO=41
    VAR=42
    BOOL=43
    INT=44
    FLOAT=45
    STRING=46
    CHAR=47
    CTE_BOOL=48
    CTE_FLOAT=49
    CTE_INT=50
    CTE_CHAR=51
    CTE_STRING=52
    VOID=53
    ID=54

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(patitoParser.PROGRAM, 0)

        def ID(self):
            return self.getToken(patitoParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(patitoParser.SEMICOLON, 0)

        def declarevars(self):
            return self.getTypedRuleContext(patitoParser.DeclarevarsContext,0)


        def functions(self):
            return self.getTypedRuleContext(patitoParser.FunctionsContext,0)


        def mainfunc(self):
            return self.getTypedRuleContext(patitoParser.MainfuncContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = patitoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(patitoParser.PROGRAM)
            self.state = 53
            self.match(patitoParser.ID)
            self.state = 54
            self.match(patitoParser.SEMICOLON)
            self.state = 55
            self.declarevars()
            compiler._add_function(compiler.currentFunction)
            self.state = 57
            self.functions()
            self.state = 58
            self.mainfunc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarevarsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(patitoParser.VAR, 0)

        def variables(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.VariablesContext)
            else:
                return self.getTypedRuleContext(patitoParser.VariablesContext,i)


        def getRuleIndex(self):
            return patitoParser.RULE_declarevars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarevars" ):
                listener.enterDeclarevars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarevars" ):
                listener.exitDeclarevars(self)




    def declarevars(self):

        localctx = patitoParser.DeclarevarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declarevars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(patitoParser.VAR)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                self.variables()
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.BOOL) | (1 << patitoParser.INT) | (1 << patitoParser.FLOAT) | (1 << patitoParser.STRING) | (1 << patitoParser.CHAR))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._vartypes = None # VartypesContext
            self._ID = None # Token

        def vartypes(self):
            return self.getTypedRuleContext(patitoParser.VartypesContext,0)


        def COLON(self):
            return self.getToken(patitoParser.COLON, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.ID)
            else:
                return self.getToken(patitoParser.ID, i)

        def SEMICOLON(self):
            return self.getToken(patitoParser.SEMICOLON, 0)

        def arrayconstant(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.ArrayconstantContext)
            else:
                return self.getTypedRuleContext(patitoParser.ArrayconstantContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.COMMA)
            else:
                return self.getToken(patitoParser.COMMA, i)

        def getRuleIndex(self):
            return patitoParser.RULE_variables

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariables" ):
                listener.enterVariables(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariables" ):
                listener.exitVariables(self)




    def variables(self):

        localctx = patitoParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            localctx._vartypes = self.vartypes()
            self.state = 67
            self.match(patitoParser.COLON)
            self.state = 68
            localctx._ID = self.match(patitoParser.ID)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.LEFT_BRACKET:
                self.state = 69
                self.arrayconstant()


            compiler.currentFunction._update_vars_table((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 73
                self.match(patitoParser.COMMA)
                self.state = 74
                localctx._ID = self.match(patitoParser.ID)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==patitoParser.LEFT_BRACKET:
                    self.state = 75
                    self.arrayconstant()


                compiler.currentFunction._update_vars_table((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(patitoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(patitoParser.INT, 0)

        def BOOL(self):
            return self.getToken(patitoParser.BOOL, 0)

        def FLOAT(self):
            return self.getToken(patitoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(patitoParser.STRING, 0)

        def CHAR(self):
            return self.getToken(patitoParser.CHAR, 0)

        def getRuleIndex(self):
            return patitoParser.RULE_vartypes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVartypes" ):
                listener.enterVartypes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVartypes" ):
                listener.exitVartypes(self)




    def vartypes(self):

        localctx = patitoParser.VartypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vartypes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.BOOL) | (1 << patitoParser.INT) | (1 << patitoParser.FLOAT) | (1 << patitoParser.STRING) | (1 << patitoParser.CHAR))) != 0)):
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


    class ConstantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CTE_BOOL(self):
            return self.getToken(patitoParser.CTE_BOOL, 0)

        def CTE_FLOAT(self):
            return self.getToken(patitoParser.CTE_FLOAT, 0)

        def CTE_INT(self):
            return self.getToken(patitoParser.CTE_INT, 0)

        def CTE_CHAR(self):
            return self.getToken(patitoParser.CTE_CHAR, 0)

        def CTE_STRING(self):
            return self.getToken(patitoParser.CTE_STRING, 0)

        def getRuleIndex(self):
            return patitoParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = patitoParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [patitoParser.CTE_BOOL]:
                self.state = 88
                self.match(patitoParser.CTE_BOOL)
                compiler.addType("bool")
                pass
            elif token in [patitoParser.CTE_FLOAT]:
                self.state = 90
                self.match(patitoParser.CTE_FLOAT)
                compiler.addType("float")
                pass
            elif token in [patitoParser.CTE_INT]:
                self.state = 92
                self.match(patitoParser.CTE_INT)
                compiler.addType("int")
                pass
            elif token in [patitoParser.CTE_CHAR]:
                self.state = 94
                self.match(patitoParser.CTE_CHAR)
                compiler.addType("char")
                pass
            elif token in [patitoParser.CTE_STRING]:
                self.state = 96
                self.match(patitoParser.CTE_STRING)
                compiler.addType("string")
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


    class ArrayconstantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.LEFT_BRACKET)
            else:
                return self.getToken(patitoParser.LEFT_BRACKET, i)

        def CTE_INT(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.CTE_INT)
            else:
                return self.getToken(patitoParser.CTE_INT, i)

        def RIGHT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.RIGHT_BRACKET)
            else:
                return self.getToken(patitoParser.RIGHT_BRACKET, i)

        def getRuleIndex(self):
            return patitoParser.RULE_arrayconstant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayconstant" ):
                listener.enterArrayconstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayconstant" ):
                listener.exitArrayconstant(self)




    def arrayconstant(self):

        localctx = patitoParser.ArrayconstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arrayconstant)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 101
                self.match(patitoParser.CTE_INT)
                self.state = 102
                self.match(patitoParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 104
                self.match(patitoParser.CTE_INT)
                self.state = 105
                self.match(patitoParser.RIGHT_BRACKET)
                self.state = 106
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 107
                self.match(patitoParser.CTE_INT)
                self.state = 108
                self.match(patitoParser.RIGHT_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.FunctionContext)
            else:
                return self.getTypedRuleContext(patitoParser.FunctionContext,i)


        def getRuleIndex(self):
            return patitoParser.RULE_functions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctions" ):
                listener.enterFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctions" ):
                listener.exitFunctions(self)




    def functions(self):

        localctx = patitoParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 111
                self.function()
                self.state = 114 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==patitoParser.FUNCTION):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._functiontype = None # FunctiontypeContext
            self._ID = None # Token

        def FUNCTION(self):
            return self.getToken(patitoParser.FUNCTION, 0)

        def functiontype(self):
            return self.getTypedRuleContext(patitoParser.FunctiontypeContext,0)


        def ID(self):
            return self.getToken(patitoParser.ID, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(patitoParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(patitoParser.RIGHT_PARENTHESIS, 0)

        def LEFT_CURLY(self):
            return self.getToken(patitoParser.LEFT_CURLY, 0)

        def RIGHT_CURLY(self):
            return self.getToken(patitoParser.RIGHT_CURLY, 0)

        def parameters(self):
            return self.getTypedRuleContext(patitoParser.ParametersContext,0)


        def declarevars(self):
            return self.getTypedRuleContext(patitoParser.DeclarevarsContext,0)


        def statute(self):
            return self.getTypedRuleContext(patitoParser.StatuteContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = patitoParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(patitoParser.FUNCTION)
            self.state = 117
            localctx._functiontype = self.functiontype()
            self.state = 118
            localctx._ID = self.match(patitoParser.ID)
            compiler.currentFunction=Function((None if localctx._ID is None else localctx._ID.text), (None if localctx._functiontype is None else self._input.getText(localctx._functiontype.start,localctx._functiontype.stop)), {}, {})
            self.state = 120
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.BOOL) | (1 << patitoParser.INT) | (1 << patitoParser.FLOAT) | (1 << patitoParser.STRING) | (1 << patitoParser.CHAR))) != 0):
                self.state = 121
                self.parameters()


            self.state = 124
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.VAR:
                self.state = 125
                self.declarevars()


            compiler._add_function(compiler.currentFunction)
            self.state = 129
            self.match(patitoParser.LEFT_CURLY)
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 130
                self.statute()


            self.state = 133
            self.match(patitoParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctiontypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(patitoParser.INT, 0)

        def BOOL(self):
            return self.getToken(patitoParser.BOOL, 0)

        def FLOAT(self):
            return self.getToken(patitoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(patitoParser.STRING, 0)

        def CHAR(self):
            return self.getToken(patitoParser.CHAR, 0)

        def VOID(self):
            return self.getToken(patitoParser.VOID, 0)

        def getRuleIndex(self):
            return patitoParser.RULE_functiontype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctiontype" ):
                listener.enterFunctiontype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctiontype" ):
                listener.exitFunctiontype(self)




    def functiontype(self):

        localctx = patitoParser.FunctiontypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functiontype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.BOOL) | (1 << patitoParser.INT) | (1 << patitoParser.FLOAT) | (1 << patitoParser.STRING) | (1 << patitoParser.CHAR) | (1 << patitoParser.VOID))) != 0)):
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


    class ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._vartypes = None # VartypesContext
            self._ID = None # Token

        def vartypes(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.VartypesContext)
            else:
                return self.getTypedRuleContext(patitoParser.VartypesContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.ID)
            else:
                return self.getToken(patitoParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.COMMA)
            else:
                return self.getToken(patitoParser.COMMA, i)

        def getRuleIndex(self):
            return patitoParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = patitoParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            localctx._vartypes = self.vartypes()
            self.state = 138
            localctx._ID = self.match(patitoParser.ID)
            compiler.currentFunction._update_parameters((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 140
                self.match(patitoParser.COMMA)
                self.state = 141
                localctx._vartypes = self.vartypes()
                self.state = 142
                localctx._ID = self.match(patitoParser.ID)
                compiler.currentFunction._update_parameters((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._AND = None # Token
            self._OR = None # Token

        def sexp(self):
            return self.getTypedRuleContext(patitoParser.SexpContext,0)


        def mexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.MexpContext)
            else:
                return self.getTypedRuleContext(patitoParser.MexpContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.AND)
            else:
                return self.getToken(patitoParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.OR)
            else:
                return self.getToken(patitoParser.OR, i)

        def getRuleIndex(self):
            return patitoParser.RULE_mexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMexp" ):
                listener.enterMexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMexp" ):
                listener.exitMexp(self)




    def mexp(self):

        localctx = patitoParser.MexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_mexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.sexp()
            compiler.topIsLogicOperator()
            self.state = 163
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 156
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.AND]:
                        self.state = 152
                        localctx._AND = self.match(patitoParser.AND)
                        compiler.addOperator((None if localctx._AND is None else localctx._AND.text))
                        pass
                    elif token in [patitoParser.OR]:
                        self.state = 154
                        localctx._OR = self.match(patitoParser.OR)
                        compiler.addOperator((None if localctx._OR is None else localctx._OR.text))
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 158
                    self.mexp()
                    compiler.topIsLogicOperator() 
                self.state = 165
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._GREATER = None # Token
            self._LESS = None # Token
            self._GREATER_EQUAL = None # Token
            self._LESS_EQUAL = None # Token
            self._NOT_EQUAL = None # Token
            self._EQUAL = None # Token

        def exp(self):
            return self.getTypedRuleContext(patitoParser.ExpContext,0)


        def sexp(self):
            return self.getTypedRuleContext(patitoParser.SexpContext,0)


        def GREATER(self):
            return self.getToken(patitoParser.GREATER, 0)

        def LESS(self):
            return self.getToken(patitoParser.LESS, 0)

        def GREATER_EQUAL(self):
            return self.getToken(patitoParser.GREATER_EQUAL, 0)

        def LESS_EQUAL(self):
            return self.getToken(patitoParser.LESS_EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(patitoParser.NOT_EQUAL, 0)

        def EQUAL(self):
            return self.getToken(patitoParser.EQUAL, 0)

        def getRuleIndex(self):
            return patitoParser.RULE_sexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSexp" ):
                listener.enterSexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSexp" ):
                listener.exitSexp(self)




    def sexp(self):

        localctx = patitoParser.SexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_sexp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.exp()
            compiler.topIsComparison()
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.LESS) | (1 << patitoParser.GREATER) | (1 << patitoParser.LESS_EQUAL) | (1 << patitoParser.GREATER_EQUAL) | (1 << patitoParser.EQUAL) | (1 << patitoParser.NOT_EQUAL))) != 0):
                self.state = 180
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [patitoParser.GREATER]:
                    self.state = 168
                    localctx._GREATER = self.match(patitoParser.GREATER)
                    compiler.addOperator((None if localctx._GREATER is None else localctx._GREATER.text))
                    pass
                elif token in [patitoParser.LESS]:
                    self.state = 170
                    localctx._LESS = self.match(patitoParser.LESS)
                    compiler.addOperator((None if localctx._LESS is None else localctx._LESS.text))
                    pass
                elif token in [patitoParser.GREATER_EQUAL]:
                    self.state = 172
                    localctx._GREATER_EQUAL = self.match(patitoParser.GREATER_EQUAL)
                    compiler.addOperator((None if localctx._GREATER_EQUAL is None else localctx._GREATER_EQUAL.text))
                    pass
                elif token in [patitoParser.LESS_EQUAL]:
                    self.state = 174
                    localctx._LESS_EQUAL = self.match(patitoParser.LESS_EQUAL)
                    compiler.addOperator((None if localctx._LESS_EQUAL is None else localctx._LESS_EQUAL.text))
                    pass
                elif token in [patitoParser.NOT_EQUAL]:
                    self.state = 176
                    localctx._NOT_EQUAL = self.match(patitoParser.NOT_EQUAL)
                    compiler.addOperator((None if localctx._NOT_EQUAL is None else localctx._NOT_EQUAL.text))
                    pass
                elif token in [patitoParser.EQUAL]:
                    self.state = 178
                    localctx._EQUAL = self.match(patitoParser.EQUAL)
                    compiler.addOperator((None if localctx._EQUAL is None else localctx._EQUAL.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 182
                self.sexp()
                compiler.topIsComparison()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ADD = None # Token
            self._SUB = None # Token

        def term(self):
            return self.getTypedRuleContext(patitoParser.TermContext,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.ExpContext)
            else:
                return self.getTypedRuleContext(patitoParser.ExpContext,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.ADD)
            else:
                return self.getToken(patitoParser.ADD, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.SUB)
            else:
                return self.getToken(patitoParser.SUB, i)

        def getRuleIndex(self):
            return patitoParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = patitoParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.term()
            compiler.topIsAddOrSub()
            self.state = 200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 193
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.ADD]:
                        self.state = 189
                        localctx._ADD = self.match(patitoParser.ADD)
                        compiler.addOperator((None if localctx._ADD is None else localctx._ADD.text))
                        pass
                    elif token in [patitoParser.SUB]:
                        self.state = 191
                        localctx._SUB = self.match(patitoParser.SUB)
                        compiler.addOperator((None if localctx._SUB is None else localctx._SUB.text))
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 195
                    self.exp()
                    compiler.topIsAddOrSub() 
                self.state = 202
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._MULT = None # Token
            self._DIV = None # Token

        def factor(self):
            return self.getTypedRuleContext(patitoParser.FactorContext,0)


        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.TermContext)
            else:
                return self.getTypedRuleContext(patitoParser.TermContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.MULT)
            else:
                return self.getToken(patitoParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.DIV)
            else:
                return self.getToken(patitoParser.DIV, i)

        def getRuleIndex(self):
            return patitoParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = patitoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.factor()
            compiler.topIsMultOrDiv()
            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 209
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.MULT]:
                        self.state = 205
                        localctx._MULT = self.match(patitoParser.MULT)
                        compiler.addOperator((None if localctx._MULT is None else localctx._MULT.text))
                        pass
                    elif token in [patitoParser.DIV]:
                        self.state = 207
                        localctx._DIV = self.match(patitoParser.DIV)
                        compiler.addOperator((None if localctx._DIV is None else localctx._DIV.text))
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 211
                    self.term()
                    compiler.topIsMultOrDiv() 
                self.state = 218
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._constant = None # ConstantContext
            self._ID = None # Token

        def constant(self):
            return self.getTypedRuleContext(patitoParser.ConstantContext,0)


        def LEFT_PARENTHESIS(self):
            return self.getToken(patitoParser.LEFT_PARENTHESIS, 0)

        def mexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.MexpContext)
            else:
                return self.getTypedRuleContext(patitoParser.MexpContext,i)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(patitoParser.RIGHT_PARENTHESIS, 0)

        def ID(self):
            return self.getToken(patitoParser.ID, 0)

        def LEFT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.LEFT_BRACKET)
            else:
                return self.getToken(patitoParser.LEFT_BRACKET, i)

        def RIGHT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.RIGHT_BRACKET)
            else:
                return self.getToken(patitoParser.RIGHT_BRACKET, i)

        def DETERMINANT(self):
            return self.getToken(patitoParser.DETERMINANT, 0)

        def TRANSPOSE(self):
            return self.getToken(patitoParser.TRANSPOSE, 0)

        def INVERSE(self):
            return self.getToken(patitoParser.INVERSE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.COMMA)
            else:
                return self.getToken(patitoParser.COMMA, i)

        def getRuleIndex(self):
            return patitoParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = patitoParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [patitoParser.CTE_BOOL, patitoParser.CTE_FLOAT, patitoParser.CTE_INT, patitoParser.CTE_CHAR, patitoParser.CTE_STRING]:
                self.state = 219
                localctx._constant = self.constant()
                compiler.addOperand((None if localctx._constant is None else self._input.getText(localctx._constant.start,localctx._constant.stop)))
                pass
            elif token in [patitoParser.LEFT_PARENTHESIS]:
                self.state = 222
                self.match(patitoParser.LEFT_PARENTHESIS)
                compiler.addParenthesis()
                self.state = 224
                self.mexp()
                self.state = 225
                self.match(patitoParser.RIGHT_PARENTHESIS)
                compiler.popParenthesis()
                pass
            elif token in [patitoParser.ID]:
                self.state = 228
                localctx._ID = self.match(patitoParser.ID)
                compiler.addOperandAndType((None if localctx._ID is None else localctx._ID.text))
                self.state = 258
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    pass

                elif la_ == 2:
                    self.state = 231
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.DETERMINANT) | (1 << patitoParser.TRANSPOSE) | (1 << patitoParser.INVERSE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass

                elif la_ == 3:
                    self.state = 232
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 233
                    self.mexp()
                    self.state = 234
                    self.match(patitoParser.RIGHT_BRACKET)
                    pass

                elif la_ == 4:
                    self.state = 236
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 237
                    self.mexp()
                    self.state = 238
                    self.match(patitoParser.RIGHT_BRACKET)
                    self.state = 239
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 240
                    self.mexp()
                    self.state = 241
                    self.match(patitoParser.RIGHT_BRACKET)
                    pass

                elif la_ == 5:
                    self.state = 243
                    self.match(patitoParser.LEFT_PARENTHESIS)
                    compiler.addParenthesis()
                    self.state = 254
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.RIGHT_PARENTHESIS]:
                        pass
                    elif token in [patitoParser.LEFT_PARENTHESIS, patitoParser.CTE_BOOL, patitoParser.CTE_FLOAT, patitoParser.CTE_INT, patitoParser.CTE_CHAR, patitoParser.CTE_STRING, patitoParser.ID]:
                        self.state = 246
                        self.mexp()
                        self.state = 251
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==patitoParser.COMMA:
                            self.state = 247
                            self.match(patitoParser.COMMA)
                            self.state = 248
                            self.mexp()
                            self.state = 253
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 256
                    self.match(patitoParser.RIGHT_PARENTHESIS)
                    compiler.popParenthesis()
                    pass


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


    class StatuteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.AssignationContext)
            else:
                return self.getTypedRuleContext(patitoParser.AssignationContext,i)


        def voidcall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.VoidcallContext)
            else:
                return self.getTypedRuleContext(patitoParser.VoidcallContext,i)


        def returncall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.ReturncallContext)
            else:
                return self.getTypedRuleContext(patitoParser.ReturncallContext,i)


        def read(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.ReadContext)
            else:
                return self.getTypedRuleContext(patitoParser.ReadContext,i)


        def write(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.WriteContext)
            else:
                return self.getTypedRuleContext(patitoParser.WriteContext,i)


        def conditional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.ConditionalContext)
            else:
                return self.getTypedRuleContext(patitoParser.ConditionalContext,i)


        def whileloop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.WhileloopContext)
            else:
                return self.getTypedRuleContext(patitoParser.WhileloopContext,i)


        def fromloop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.FromloopContext)
            else:
                return self.getTypedRuleContext(patitoParser.FromloopContext,i)


        def getRuleIndex(self):
            return patitoParser.RULE_statute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatute" ):
                listener.enterStatute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatute" ):
                listener.exitStatute(self)




    def statute(self):

        localctx = patitoParser.StatuteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.RETURN) | (1 << patitoParser.INPUT) | (1 << patitoParser.PRINT) | (1 << patitoParser.IF) | (1 << patitoParser.WHILE) | (1 << patitoParser.FROM) | (1 << patitoParser.ID))) != 0):
                self.state = 270
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 262
                    self.assignation()
                    pass

                elif la_ == 2:
                    self.state = 263
                    self.voidcall()
                    pass

                elif la_ == 3:
                    self.state = 264
                    self.returncall()
                    pass

                elif la_ == 4:
                    self.state = 265
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 266
                    self.write()
                    pass

                elif la_ == 6:
                    self.state = 267
                    self.conditional()
                    pass

                elif la_ == 7:
                    self.state = 268
                    self.whileloop()
                    pass

                elif la_ == 8:
                    self.state = 269
                    self.fromloop()
                    pass


                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._ASSIGN = None # Token

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.ID)
            else:
                return self.getToken(patitoParser.ID, i)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.ASSIGN)
            else:
                return self.getToken(patitoParser.ASSIGN, i)

        def SEMICOLON(self):
            return self.getToken(patitoParser.SEMICOLON, 0)

        def mexp(self):
            return self.getTypedRuleContext(patitoParser.MexpContext,0)


        def indexvariable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.IndexvariableContext)
            else:
                return self.getTypedRuleContext(patitoParser.IndexvariableContext,i)


        def getRuleIndex(self):
            return patitoParser.RULE_assignation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignation" ):
                listener.enterAssignation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignation" ):
                listener.exitAssignation(self)




    def assignation(self):

        localctx = patitoParser.AssignationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assignation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            localctx._ID = self.match(patitoParser.ID)
            compiler.addOperandAndType((None if localctx._ID is None else localctx._ID.text))
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.LEFT_BRACKET:
                self.state = 277
                self.indexvariable()


            self.state = 280
            localctx._ASSIGN = self.match(patitoParser.ASSIGN)
            compiler.addOperator((None if localctx._ASSIGN is None else localctx._ASSIGN.text))
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 282
                    localctx._ID = self.match(patitoParser.ID)
                    compiler.addOperandAndType((None if localctx._ID is None else localctx._ID.text))
                    self.state = 285
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==patitoParser.LEFT_BRACKET:
                        self.state = 284
                        self.indexvariable()


                    self.state = 287
                    localctx._ASSIGN = self.match(patitoParser.ASSIGN)
                    compiler.addOperator((None if localctx._ASSIGN is None else localctx._ASSIGN.text)) 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 294
                localctx._ID = self.match(patitoParser.ID)
                compiler.addOperandAndType((None if localctx._ID is None else localctx._ID.text))
                pass

            elif la_ == 2:
                self.state = 296
                self.mexp()
                pass


            self.state = 299
            self.match(patitoParser.SEMICOLON)
            compiler.generateAssignQuads()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidcallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(patitoParser.ID, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(patitoParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(patitoParser.RIGHT_PARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(patitoParser.SEMICOLON, 0)

        def mexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.MexpContext)
            else:
                return self.getTypedRuleContext(patitoParser.MexpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.COMMA)
            else:
                return self.getToken(patitoParser.COMMA, i)

        def getRuleIndex(self):
            return patitoParser.RULE_voidcall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoidcall" ):
                listener.enterVoidcall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoidcall" ):
                listener.exitVoidcall(self)




    def voidcall(self):

        localctx = patitoParser.VoidcallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_voidcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(patitoParser.ID)
            self.state = 303
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [patitoParser.RIGHT_PARENTHESIS]:
                pass
            elif token in [patitoParser.LEFT_PARENTHESIS, patitoParser.CTE_BOOL, patitoParser.CTE_FLOAT, patitoParser.CTE_INT, patitoParser.CTE_CHAR, patitoParser.CTE_STRING, patitoParser.ID]:
                self.state = 305
                self.mexp()
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==patitoParser.COMMA:
                    self.state = 306
                    self.match(patitoParser.COMMA)
                    self.state = 307
                    self.mexp()
                    self.state = 312
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 315
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 316
            self.match(patitoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(patitoParser.RETURN, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(patitoParser.LEFT_PARENTHESIS, 0)

        def mexp(self):
            return self.getTypedRuleContext(patitoParser.MexpContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(patitoParser.RIGHT_PARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(patitoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return patitoParser.RULE_returncall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturncall" ):
                listener.enterReturncall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturncall" ):
                listener.exitReturncall(self)




    def returncall(self):

        localctx = patitoParser.ReturncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_returncall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(patitoParser.RETURN)
            self.state = 319
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 320
            self.mexp()
            self.state = 321
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 322
            self.match(patitoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexvariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.LEFT_BRACKET)
            else:
                return self.getToken(patitoParser.LEFT_BRACKET, i)

        def mexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.MexpContext)
            else:
                return self.getTypedRuleContext(patitoParser.MexpContext,i)


        def RIGHT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.RIGHT_BRACKET)
            else:
                return self.getToken(patitoParser.RIGHT_BRACKET, i)

        def getRuleIndex(self):
            return patitoParser.RULE_indexvariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexvariable" ):
                listener.enterIndexvariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexvariable" ):
                listener.exitIndexvariable(self)




    def indexvariable(self):

        localctx = patitoParser.IndexvariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_indexvariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 324
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 325
                self.mexp()
                self.state = 326
                self.match(patitoParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.state = 328
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 329
                self.mexp()
                self.state = 330
                self.match(patitoParser.RIGHT_BRACKET)
                self.state = 331
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 332
                self.mexp()
                self.state = 333
                self.match(patitoParser.RIGHT_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.var_id = None # Token
            self.var_id2 = None # Token

        def INPUT(self):
            return self.getToken(patitoParser.INPUT, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(patitoParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(patitoParser.RIGHT_PARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(patitoParser.SEMICOLON, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.ID)
            else:
                return self.getToken(patitoParser.ID, i)

        def indexvariable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.IndexvariableContext)
            else:
                return self.getTypedRuleContext(patitoParser.IndexvariableContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.COMMA)
            else:
                return self.getToken(patitoParser.COMMA, i)

        def getRuleIndex(self):
            return patitoParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)




    def read(self):

        localctx = patitoParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_read)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(patitoParser.INPUT)
            self.state = 338
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 339
            localctx.var_id = self.match(patitoParser.ID)
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.LEFT_BRACKET:
                self.state = 340
                self.indexvariable()


            compiler.generateReadQuad((None if localctx.var_id is None else localctx.var_id.text))
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 344
                self.match(patitoParser.COMMA)
                self.state = 345
                localctx.var_id2 = self.match(patitoParser.ID)
                self.state = 347
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==patitoParser.LEFT_BRACKET:
                    self.state = 346
                    self.indexvariable()


                compiler.generateReadQuad((None if localctx.var_id2 is None else localctx.var_id2.text))
                self.state = 354
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 355
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 356
            self.match(patitoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(patitoParser.PRINT, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(patitoParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(patitoParser.RIGHT_PARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(patitoParser.SEMICOLON, 0)

        def mexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.MexpContext)
            else:
                return self.getTypedRuleContext(patitoParser.MexpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.COMMA)
            else:
                return self.getToken(patitoParser.COMMA, i)

        def getRuleIndex(self):
            return patitoParser.RULE_write

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)




    def write(self):

        localctx = patitoParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_write)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(patitoParser.PRINT)
            self.state = 359
            self.match(patitoParser.LEFT_PARENTHESIS)

            self.state = 360
            self.mexp()
            compiler.generateWriteQuad()
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 363
                self.match(patitoParser.COMMA)

                self.state = 364
                self.mexp()
                compiler.generateWriteQuad()
                self.state = 371
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 372
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 373
            self.match(patitoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(patitoParser.IF, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(patitoParser.LEFT_PARENTHESIS, 0)

        def mexp(self):
            return self.getTypedRuleContext(patitoParser.MexpContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(patitoParser.RIGHT_PARENTHESIS, 0)

        def THEN(self):
            return self.getToken(patitoParser.THEN, 0)

        def LEFT_CURLY(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.LEFT_CURLY)
            else:
                return self.getToken(patitoParser.LEFT_CURLY, i)

        def statute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.StatuteContext)
            else:
                return self.getTypedRuleContext(patitoParser.StatuteContext,i)


        def RIGHT_CURLY(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.RIGHT_CURLY)
            else:
                return self.getToken(patitoParser.RIGHT_CURLY, i)

        def ELSE(self):
            return self.getToken(patitoParser.ELSE, 0)

        def getRuleIndex(self):
            return patitoParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)




    def conditional(self):

        localctx = patitoParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(patitoParser.IF)
            self.state = 376
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 377
            self.mexp()
            self.state = 378
            self.match(patitoParser.RIGHT_PARENTHESIS)
            compiler.generateIfQuad()
            self.state = 380
            self.match(patitoParser.THEN)
            self.state = 381
            self.match(patitoParser.LEFT_CURLY)
            self.state = 382
            self.statute()
            self.state = 383
            self.match(patitoParser.RIGHT_CURLY)
            self.state = 390
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.ELSE:
                self.state = 384
                self.match(patitoParser.ELSE)
                compiler.generateGoToQuad()
                self.state = 386
                self.match(patitoParser.LEFT_CURLY)
                self.state = 387
                self.statute()
                self.state = 388
                self.match(patitoParser.RIGHT_CURLY)


            compiler.generateEndIfQuad()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileloopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(patitoParser.WHILE, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(patitoParser.LEFT_PARENTHESIS, 0)

        def mexp(self):
            return self.getTypedRuleContext(patitoParser.MexpContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(patitoParser.RIGHT_PARENTHESIS, 0)

        def DO(self):
            return self.getToken(patitoParser.DO, 0)

        def LEFT_CURLY(self):
            return self.getToken(patitoParser.LEFT_CURLY, 0)

        def statute(self):
            return self.getTypedRuleContext(patitoParser.StatuteContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(patitoParser.RIGHT_CURLY, 0)

        def getRuleIndex(self):
            return patitoParser.RULE_whileloop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileloop" ):
                listener.enterWhileloop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileloop" ):
                listener.exitWhileloop(self)




    def whileloop(self):

        localctx = patitoParser.WhileloopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_whileloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(patitoParser.WHILE)
            self.state = 395
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 396
            self.mexp()
            self.state = 397
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 398
            self.match(patitoParser.DO)
            self.state = 399
            self.match(patitoParser.LEFT_CURLY)
            self.state = 400
            self.statute()
            self.state = 401
            self.match(patitoParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FromloopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(patitoParser.FROM, 0)

        def ID(self):
            return self.getToken(patitoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(patitoParser.ASSIGN, 0)

        def mexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.MexpContext)
            else:
                return self.getTypedRuleContext(patitoParser.MexpContext,i)


        def TO(self):
            return self.getToken(patitoParser.TO, 0)

        def DO(self):
            return self.getToken(patitoParser.DO, 0)

        def LEFT_CURLY(self):
            return self.getToken(patitoParser.LEFT_CURLY, 0)

        def statute(self):
            return self.getTypedRuleContext(patitoParser.StatuteContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(patitoParser.RIGHT_CURLY, 0)

        def indexvariable(self):
            return self.getTypedRuleContext(patitoParser.IndexvariableContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_fromloop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFromloop" ):
                listener.enterFromloop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFromloop" ):
                listener.exitFromloop(self)




    def fromloop(self):

        localctx = patitoParser.FromloopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_fromloop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(patitoParser.FROM)
            self.state = 404
            self.match(patitoParser.ID)
            self.state = 406
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.LEFT_BRACKET:
                self.state = 405
                self.indexvariable()


            self.state = 408
            self.match(patitoParser.ASSIGN)
            self.state = 409
            self.mexp()
            self.state = 410
            self.match(patitoParser.TO)
            self.state = 411
            self.mexp()
            self.state = 412
            self.match(patitoParser.DO)
            self.state = 413
            self.match(patitoParser.LEFT_CURLY)
            self.state = 414
            self.statute()
            self.state = 415
            self.match(patitoParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainfuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(patitoParser.MAIN, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(patitoParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(patitoParser.RIGHT_PARENTHESIS, 0)

        def LEFT_CURLY(self):
            return self.getToken(patitoParser.LEFT_CURLY, 0)

        def statute(self):
            return self.getTypedRuleContext(patitoParser.StatuteContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(patitoParser.RIGHT_CURLY, 0)

        def getRuleIndex(self):
            return patitoParser.RULE_mainfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainfunc" ):
                listener.enterMainfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainfunc" ):
                listener.exitMainfunc(self)




    def mainfunc(self):

        localctx = patitoParser.MainfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_mainfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(patitoParser.MAIN)
            compiler.currentFunction=Function("main", "void", {}, {})
            self.state = 419
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 420
            self.match(patitoParser.RIGHT_PARENTHESIS)
            compiler._add_function(compiler.currentFunction)
            self.state = 422
            self.match(patitoParser.LEFT_CURLY)
            self.state = 423
            self.statute()
            self.state = 424
            self.match(patitoParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





