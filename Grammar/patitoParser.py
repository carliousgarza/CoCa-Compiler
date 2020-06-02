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


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38")
        buf.write("\u01f9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\3\2\3\2\3\2\3\2\3\2\5\2:\n\2\3\2\3\2\5")
        buf.write("\2>\n\2\3\2\3\2\3\3\3\3\6\3D\n\3\r\3\16\3E\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4W")
        buf.write("\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\5\4g\n\4\7\4i\n\4\f\4\16\4l\13\4\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0089\n\6")
        buf.write("\3\7\6\7\u008c\n\7\r\7\16\7\u008d\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\5\b\u0097\n\b\3\b\3\b\5\b\u009b\n\b\3\b\3\b\3")
        buf.write("\b\5\b\u00a0\n\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\7\n\u00af\n\n\f\n\16\n\u00b2\13\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\5\13\u00ba\n\13\3\13\3\13\3")
        buf.write("\13\7\13\u00bf\n\13\f\13\16\13\u00c2\13\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00d2")
        buf.write("\n\f\3\f\3\f\3\f\5\f\u00d7\n\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00df\n\r\3\r\3\r\3\r\7\r\u00e4\n\r\f\r\16\r\u00e7")
        buf.write("\13\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00ef\n\16\3")
        buf.write("\16\3\16\3\16\7\16\u00f4\n\16\f\16\16\16\u00f7\13\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u0109\n\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u011e\n\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\7\17\u012c\n\17\f\17\16\17\u012f\13\17\5\17\u0131\n\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u0138\n\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\7\20\u0142\n\20\f\20\16\20")
        buf.write("\u0145\13\20\3\21\3\21\3\21\5\21\u014a\n\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u0151\n\21\3\21\3\21\7\21\u0155\n")
        buf.write("\21\f\21\16\21\u0158\13\21\3\21\3\21\3\21\3\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\7\22\u016a\n\22\f\22\16\22\u016d\13\22\5\22\u016f\n\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24")
        buf.write("\u0191\n\24\3\25\3\25\3\25\3\25\3\25\5\25\u0198\n\25\3")
        buf.write("\25\3\25\3\25\3\25\5\25\u019e\n\25\3\25\3\25\7\25\u01a2")
        buf.write("\n\25\f\25\16\25\u01a5\13\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u01b3\n\26\f")
        buf.write("\26\16\26\u01b6\13\26\3\26\3\26\3\26\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u01ca\n\27\3\27\3\27\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u01de\n\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\2\2\33\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\2")
        buf.write("\4\3\2-\61\4\2-\61\67\67\2\u021c\2\64\3\2\2\2\4A\3\2\2")
        buf.write("\2\6G\3\2\2\2\bo\3\2\2\2\n\u0088\3\2\2\2\f\u008b\3\2\2")
        buf.write("\2\16\u008f\3\2\2\2\20\u00a4\3\2\2\2\22\u00a6\3\2\2\2")
        buf.write("\24\u00b3\3\2\2\2\26\u00c3\3\2\2\2\30\u00d8\3\2\2\2\32")
        buf.write("\u00e8\3\2\2\2\34\u0137\3\2\2\2\36\u0143\3\2\2\2 \u0146")
        buf.write("\3\2\2\2\"\u015d\3\2\2\2$\u0176\3\2\2\2&\u0190\3\2\2\2")
        buf.write("(\u0192\3\2\2\2*\u01a9\3\2\2\2,\u01ba\3\2\2\2.\u01cd\3")
        buf.write("\2\2\2\60\u01d9\3\2\2\2\62\u01ed\3\2\2\2\64\65\7\37\2")
        buf.write("\2\65\66\78\2\2\66\67\b\2\1\2\679\7\36\2\28:\5\4\3\29")
        buf.write("8\3\2\2\29:\3\2\2\2:;\3\2\2\2;=\b\2\1\2<>\5\f\7\2=<\3")
        buf.write("\2\2\2=>\3\2\2\2>?\3\2\2\2?@\5\62\32\2@\3\3\2\2\2AC\7")
        buf.write(",\2\2BD\5\6\4\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2")
        buf.write("\2F\5\3\2\2\2GH\5\b\5\2HI\7\35\2\2IJ\78\2\2JV\b\4\1\2")
        buf.write("KL\7\25\2\2LM\7\64\2\2MN\7\26\2\2NW\b\4\1\2OP\7\25\2\2")
        buf.write("PQ\7\64\2\2QR\7\26\2\2RS\7\25\2\2ST\7\64\2\2TU\7\26\2")
        buf.write("\2UW\b\4\1\2VK\3\2\2\2VO\3\2\2\2VW\3\2\2\2Wj\3\2\2\2X")
        buf.write("Y\7\34\2\2YZ\78\2\2Zf\b\4\1\2[\\\7\25\2\2\\]\7\64\2\2")
        buf.write("]^\7\26\2\2^g\b\4\1\2_`\7\25\2\2`a\7\64\2\2ab\7\26\2\2")
        buf.write("bc\7\25\2\2cd\7\64\2\2de\7\26\2\2eg\b\4\1\2f[\3\2\2\2")
        buf.write("f_\3\2\2\2fg\3\2\2\2gi\3\2\2\2hX\3\2\2\2il\3\2\2\2jh\3")
        buf.write("\2\2\2jk\3\2\2\2km\3\2\2\2lj\3\2\2\2mn\7\36\2\2n\7\3\2")
        buf.write("\2\2op\t\2\2\2p\t\3\2\2\2qr\7\62\2\2rs\b\6\1\2s\u0089")
        buf.write("\b\6\1\2tu\7\20\2\2uv\7\63\2\2vw\b\6\1\2w\u0089\b\6\1")
        buf.write("\2xy\7\63\2\2yz\b\6\1\2z\u0089\b\6\1\2{|\7\20\2\2|}\7")
        buf.write("\64\2\2}~\b\6\1\2~\u0089\b\6\1\2\177\u0080\7\64\2\2\u0080")
        buf.write("\u0081\b\6\1\2\u0081\u0089\b\6\1\2\u0082\u0083\7\65\2")
        buf.write("\2\u0083\u0084\b\6\1\2\u0084\u0089\b\6\1\2\u0085\u0086")
        buf.write("\7\66\2\2\u0086\u0087\b\6\1\2\u0087\u0089\b\6\1\2\u0088")
        buf.write("q\3\2\2\2\u0088t\3\2\2\2\u0088x\3\2\2\2\u0088{\3\2\2\2")
        buf.write("\u0088\177\3\2\2\2\u0088\u0082\3\2\2\2\u0088\u0085\3\2")
        buf.write("\2\2\u0089\13\3\2\2\2\u008a\u008c\5\16\b\2\u008b\u008a")
        buf.write("\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008b\3\2\2\2\u008d")
        buf.write("\u008e\3\2\2\2\u008e\r\3\2\2\2\u008f\u0090\7!\2\2\u0090")
        buf.write("\u0091\5\20\t\2\u0091\u0092\78\2\2\u0092\u0093\b\b\1\2")
        buf.write("\u0093\u0094\b\b\1\2\u0094\u0096\7\23\2\2\u0095\u0097")
        buf.write("\5\22\n\2\u0096\u0095\3\2\2\2\u0096\u0097\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098\u009a\7\24\2\2\u0099\u009b\5\4\3")
        buf.write("\2\u009a\u0099\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c")
        buf.write("\3\2\2\2\u009c\u009d\b\b\1\2\u009d\u009f\7\27\2\2\u009e")
        buf.write("\u00a0\5\36\20\2\u009f\u009e\3\2\2\2\u009f\u00a0\3\2\2")
        buf.write("\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\7\30\2\2\u00a2\u00a3")
        buf.write("\b\b\1\2\u00a3\17\3\2\2\2\u00a4\u00a5\t\3\2\2\u00a5\21")
        buf.write("\3\2\2\2\u00a6\u00a7\5\b\5\2\u00a7\u00a8\78\2\2\u00a8")
        buf.write("\u00b0\b\n\1\2\u00a9\u00aa\7\34\2\2\u00aa\u00ab\5\b\5")
        buf.write("\2\u00ab\u00ac\78\2\2\u00ac\u00ad\b\n\1\2\u00ad\u00af")
        buf.write("\3\2\2\2\u00ae\u00a9\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0")
        buf.write("\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\23\3\2\2\2\u00b2")
        buf.write("\u00b0\3\2\2\2\u00b3\u00b4\5\26\f\2\u00b4\u00c0\b\13\1")
        buf.write("\2\u00b5\u00b6\7\r\2\2\u00b6\u00ba\b\13\1\2\u00b7\u00b8")
        buf.write("\7\16\2\2\u00b8\u00ba\b\13\1\2\u00b9\u00b5\3\2\2\2\u00b9")
        buf.write("\u00b7\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\5\24\13")
        buf.write("\2\u00bc\u00bd\b\13\1\2\u00bd\u00bf\3\2\2\2\u00be\u00b9")
        buf.write("\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0")
        buf.write("\u00c1\3\2\2\2\u00c1\25\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3")
        buf.write("\u00c4\5\30\r\2\u00c4\u00d6\b\f\1\2\u00c5\u00c6\7\7\2")
        buf.write("\2\u00c6\u00d2\b\f\1\2\u00c7\u00c8\7\6\2\2\u00c8\u00d2")
        buf.write("\b\f\1\2\u00c9\u00ca\7\t\2\2\u00ca\u00d2\b\f\1\2\u00cb")
        buf.write("\u00cc\7\b\2\2\u00cc\u00d2\b\f\1\2\u00cd\u00ce\7\13\2")
        buf.write("\2\u00ce\u00d2\b\f\1\2\u00cf\u00d0\7\n\2\2\u00d0\u00d2")
        buf.write("\b\f\1\2\u00d1\u00c5\3\2\2\2\u00d1\u00c7\3\2\2\2\u00d1")
        buf.write("\u00c9\3\2\2\2\u00d1\u00cb\3\2\2\2\u00d1\u00cd\3\2\2\2")
        buf.write("\u00d1\u00cf\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\5")
        buf.write("\26\f\2\u00d4\u00d5\b\f\1\2\u00d5\u00d7\3\2\2\2\u00d6")
        buf.write("\u00d1\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\27\3\2\2\2\u00d8")
        buf.write("\u00d9\5\32\16\2\u00d9\u00e5\b\r\1\2\u00da\u00db\7\17")
        buf.write("\2\2\u00db\u00df\b\r\1\2\u00dc\u00dd\7\20\2\2\u00dd\u00df")
        buf.write("\b\r\1\2\u00de\u00da\3\2\2\2\u00de\u00dc\3\2\2\2\u00df")
        buf.write("\u00e0\3\2\2\2\u00e0\u00e1\5\30\r\2\u00e1\u00e2\b\r\1")
        buf.write("\2\u00e2\u00e4\3\2\2\2\u00e3\u00de\3\2\2\2\u00e4\u00e7")
        buf.write("\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6")
        buf.write("\31\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00e9\5\34\17\2")
        buf.write("\u00e9\u00f5\b\16\1\2\u00ea\u00eb\7\21\2\2\u00eb\u00ef")
        buf.write("\b\16\1\2\u00ec\u00ed\7\22\2\2\u00ed\u00ef\b\16\1\2\u00ee")
        buf.write("\u00ea\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f0\3\2\2\2")
        buf.write("\u00f0\u00f1\5\32\16\2\u00f1\u00f2\b\16\1\2\u00f2\u00f4")
        buf.write("\3\2\2\2\u00f3\u00ee\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5")
        buf.write("\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\33\3\2\2\2\u00f7")
        buf.write("\u00f5\3\2\2\2\u00f8\u0138\5\n\6\2\u00f9\u00fa\7\23\2")
        buf.write("\2\u00fa\u00fb\b\17\1\2\u00fb\u00fc\5\24\13\2\u00fc\u00fd")
        buf.write("\7\24\2\2\u00fd\u00fe\b\17\1\2\u00fe\u0138\3\2\2\2\u00ff")
        buf.write("\u0100\78\2\2\u0100\u011d\b\17\1\2\u0101\u011e\3\2\2\2")
        buf.write("\u0102\u0103\7\31\2\2\u0103\u0109\b\17\1\2\u0104\u0105")
        buf.write("\7\32\2\2\u0105\u0109\b\17\1\2\u0106\u0107\7\33\2\2\u0107")
        buf.write("\u0109\b\17\1\2\u0108\u0102\3\2\2\2\u0108\u0104\3\2\2")
        buf.write("\2\u0108\u0106\3\2\2\2\u0109\u011e\3\2\2\2\u010a\u010b")
        buf.write("\7\25\2\2\u010b\u010c\b\17\1\2\u010c\u010d\5\24\13\2\u010d")
        buf.write("\u010e\b\17\1\2\u010e\u010f\b\17\1\2\u010f\u0110\7\26")
        buf.write("\2\2\u0110\u011e\3\2\2\2\u0111\u0112\7\25\2\2\u0112\u0113")
        buf.write("\b\17\1\2\u0113\u0114\5\24\13\2\u0114\u0115\b\17\1\2\u0115")
        buf.write("\u0116\7\26\2\2\u0116\u0117\7\25\2\2\u0117\u0118\b\17")
        buf.write("\1\2\u0118\u0119\5\24\13\2\u0119\u011a\b\17\1\2\u011a")
        buf.write("\u011b\b\17\1\2\u011b\u011c\7\26\2\2\u011c\u011e\3\2\2")
        buf.write("\2\u011d\u0101\3\2\2\2\u011d\u0108\3\2\2\2\u011d\u010a")
        buf.write("\3\2\2\2\u011d\u0111\3\2\2\2\u011e\u0138\3\2\2\2\u011f")
        buf.write("\u0120\78\2\2\u0120\u0121\b\17\1\2\u0121\u0122\7\23\2")
        buf.write("\2\u0122\u0123\b\17\1\2\u0123\u0130\b\17\1\2\u0124\u0131")
        buf.write("\3\2\2\2\u0125\u0126\5\24\13\2\u0126\u012d\b\17\1\2\u0127")
        buf.write("\u0128\7\34\2\2\u0128\u0129\5\24\13\2\u0129\u012a\b\17")
        buf.write("\1\2\u012a\u012c\3\2\2\2\u012b\u0127\3\2\2\2\u012c\u012f")
        buf.write("\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e")
        buf.write("\u0131\3\2\2\2\u012f\u012d\3\2\2\2\u0130\u0124\3\2\2\2")
        buf.write("\u0130\u0125\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0133\b")
        buf.write("\17\1\2\u0133\u0134\b\17\1\2\u0134\u0135\b\17\1\2\u0135")
        buf.write("\u0136\7\24\2\2\u0136\u0138\b\17\1\2\u0137\u00f8\3\2\2")
        buf.write("\2\u0137\u00f9\3\2\2\2\u0137\u00ff\3\2\2\2\u0137\u011f")
        buf.write("\3\2\2\2\u0138\35\3\2\2\2\u0139\u0142\5 \21\2\u013a\u0142")
        buf.write("\5\"\22\2\u013b\u0142\5$\23\2\u013c\u0142\5(\25\2\u013d")
        buf.write("\u0142\5*\26\2\u013e\u0142\5,\27\2\u013f\u0142\5.\30\2")
        buf.write("\u0140\u0142\5\60\31\2\u0141\u0139\3\2\2\2\u0141\u013a")
        buf.write("\3\2\2\2\u0141\u013b\3\2\2\2\u0141\u013c\3\2\2\2\u0141")
        buf.write("\u013d\3\2\2\2\u0141\u013e\3\2\2\2\u0141\u013f\3\2\2\2")
        buf.write("\u0141\u0140\3\2\2\2\u0142\u0145\3\2\2\2\u0143\u0141\3")
        buf.write("\2\2\2\u0143\u0144\3\2\2\2\u0144\37\3\2\2\2\u0145\u0143")
        buf.write("\3\2\2\2\u0146\u0147\78\2\2\u0147\u0149\b\21\1\2\u0148")
        buf.write("\u014a\5&\24\2\u0149\u0148\3\2\2\2\u0149\u014a\3\2\2\2")
        buf.write("\u014a\u014b\3\2\2\2\u014b\u014c\7\f\2\2\u014c\u0156\b")
        buf.write("\21\1\2\u014d\u014e\78\2\2\u014e\u0150\b\21\1\2\u014f")
        buf.write("\u0151\5&\24\2\u0150\u014f\3\2\2\2\u0150\u0151\3\2\2\2")
        buf.write("\u0151\u0152\3\2\2\2\u0152\u0153\7\f\2\2\u0153\u0155\b")
        buf.write("\21\1\2\u0154\u014d\3\2\2\2\u0155\u0158\3\2\2\2\u0156")
        buf.write("\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0159\3\2\2\2")
        buf.write("\u0158\u0156\3\2\2\2\u0159\u015a\5\24\13\2\u015a\u015b")
        buf.write("\7\36\2\2\u015b\u015c\b\21\1\2\u015c!\3\2\2\2\u015d\u015e")
        buf.write("\78\2\2\u015e\u015f\b\22\1\2\u015f\u0160\7\23\2\2\u0160")
        buf.write("\u0161\b\22\1\2\u0161\u016e\b\22\1\2\u0162\u016f\3\2\2")
        buf.write("\2\u0163\u0164\5\24\13\2\u0164\u016b\b\22\1\2\u0165\u0166")
        buf.write("\7\34\2\2\u0166\u0167\5\24\13\2\u0167\u0168\b\22\1\2\u0168")
        buf.write("\u016a\3\2\2\2\u0169\u0165\3\2\2\2\u016a\u016d\3\2\2\2")
        buf.write("\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016f\3")
        buf.write("\2\2\2\u016d\u016b\3\2\2\2\u016e\u0162\3\2\2\2\u016e\u0163")
        buf.write("\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0171\b\22\1\2\u0171")
        buf.write("\u0172\b\22\1\2\u0172\u0173\7\24\2\2\u0173\u0174\7\36")
        buf.write("\2\2\u0174\u0175\b\22\1\2\u0175#\3\2\2\2\u0176\u0177\7")
        buf.write("\"\2\2\u0177\u0178\7\23\2\2\u0178\u0179\5\24\13\2\u0179")
        buf.write("\u017a\7\24\2\2\u017a\u017b\7\36\2\2\u017b\u017c\b\23")
        buf.write("\1\2\u017c%\3\2\2\2\u017d\u017e\7\25\2\2\u017e\u017f\b")
        buf.write("\24\1\2\u017f\u0180\5\24\13\2\u0180\u0181\b\24\1\2\u0181")
        buf.write("\u0182\b\24\1\2\u0182\u0183\7\26\2\2\u0183\u0191\3\2\2")
        buf.write("\2\u0184\u0185\7\25\2\2\u0185\u0186\b\24\1\2\u0186\u0187")
        buf.write("\5\24\13\2\u0187\u0188\b\24\1\2\u0188\u0189\7\26\2\2\u0189")
        buf.write("\u018a\7\25\2\2\u018a\u018b\b\24\1\2\u018b\u018c\5\24")
        buf.write("\13\2\u018c\u018d\b\24\1\2\u018d\u018e\b\24\1\2\u018e")
        buf.write("\u018f\7\26\2\2\u018f\u0191\3\2\2\2\u0190\u017d\3\2\2")
        buf.write("\2\u0190\u0184\3\2\2\2\u0191\'\3\2\2\2\u0192\u0193\7#")
        buf.write("\2\2\u0193\u0194\7\23\2\2\u0194\u0195\78\2\2\u0195\u0197")
        buf.write("\b\25\1\2\u0196\u0198\5&\24\2\u0197\u0196\3\2\2\2\u0197")
        buf.write("\u0198\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u01a3\b\25\1")
        buf.write("\2\u019a\u019b\7\34\2\2\u019b\u019d\78\2\2\u019c\u019e")
        buf.write("\5&\24\2\u019d\u019c\3\2\2\2\u019d\u019e\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f\u01a0\b\25\1\2\u01a0\u01a2\b\25\1")
        buf.write("\2\u01a1\u019a\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1")
        buf.write("\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a6\3\2\2\2\u01a5")
        buf.write("\u01a3\3\2\2\2\u01a6\u01a7\7\24\2\2\u01a7\u01a8\7\36\2")
        buf.write("\2\u01a8)\3\2\2\2\u01a9\u01aa\7$\2\2\u01aa\u01ab\7\23")
        buf.write("\2\2\u01ab\u01ac\5\24\13\2\u01ac\u01ad\b\26\1\2\u01ad")
        buf.write("\u01b4\3\2\2\2\u01ae\u01af\7\34\2\2\u01af\u01b0\5\24\13")
        buf.write("\2\u01b0\u01b1\b\26\1\2\u01b1\u01b3\3\2\2\2\u01b2\u01ae")
        buf.write("\3\2\2\2\u01b3\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4")
        buf.write("\u01b5\3\2\2\2\u01b5\u01b7\3\2\2\2\u01b6\u01b4\3\2\2\2")
        buf.write("\u01b7\u01b8\7\24\2\2\u01b8\u01b9\7\36\2\2\u01b9+\3\2")
        buf.write("\2\2\u01ba\u01bb\7%\2\2\u01bb\u01bc\7\23\2\2\u01bc\u01bd")
        buf.write("\5\24\13\2\u01bd\u01be\7\24\2\2\u01be\u01bf\b\27\1\2\u01bf")
        buf.write("\u01c0\7&\2\2\u01c0\u01c1\7\27\2\2\u01c1\u01c2\5\36\20")
        buf.write("\2\u01c2\u01c9\7\30\2\2\u01c3\u01c4\7\'\2\2\u01c4\u01c5")
        buf.write("\b\27\1\2\u01c5\u01c6\7\27\2\2\u01c6\u01c7\5\36\20\2\u01c7")
        buf.write("\u01c8\7\30\2\2\u01c8\u01ca\3\2\2\2\u01c9\u01c3\3\2\2")
        buf.write("\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cc")
        buf.write("\b\27\1\2\u01cc-\3\2\2\2\u01cd\u01ce\7(\2\2\u01ce\u01cf")
        buf.write("\7\23\2\2\u01cf\u01d0\b\30\1\2\u01d0\u01d1\5\24\13\2\u01d1")
        buf.write("\u01d2\7\24\2\2\u01d2\u01d3\b\30\1\2\u01d3\u01d4\7)\2")
        buf.write("\2\u01d4\u01d5\7\27\2\2\u01d5\u01d6\5\36\20\2\u01d6\u01d7")
        buf.write("\b\30\1\2\u01d7\u01d8\7\30\2\2\u01d8/\3\2\2\2\u01d9\u01da")
        buf.write("\7*\2\2\u01da\u01db\78\2\2\u01db\u01dd\b\31\1\2\u01dc")
        buf.write("\u01de\5&\24\2\u01dd\u01dc\3\2\2\2\u01dd\u01de\3\2\2\2")
        buf.write("\u01de\u01df\3\2\2\2\u01df\u01e0\7\f\2\2\u01e0\u01e1\b")
        buf.write("\31\1\2\u01e1\u01e2\5\24\13\2\u01e2\u01e3\b\31\1\2\u01e3")
        buf.write("\u01e4\7+\2\2\u01e4\u01e5\b\31\1\2\u01e5\u01e6\5\24\13")
        buf.write("\2\u01e6\u01e7\b\31\1\2\u01e7\u01e8\7)\2\2\u01e8\u01e9")
        buf.write("\7\27\2\2\u01e9\u01ea\5\36\20\2\u01ea\u01eb\7\30\2\2\u01eb")
        buf.write("\u01ec\b\31\1\2\u01ec\61\3\2\2\2\u01ed\u01ee\7 \2\2\u01ee")
        buf.write("\u01ef\b\32\1\2\u01ef\u01f0\b\32\1\2\u01f0\u01f1\7\23")
        buf.write("\2\2\u01f1\u01f2\7\24\2\2\u01f2\u01f3\b\32\1\2\u01f3\u01f4")
        buf.write("\7\27\2\2\u01f4\u01f5\b\32\1\2\u01f5\u01f6\5\36\20\2\u01f6")
        buf.write("\u01f7\7\30\2\2\u01f7\63\3\2\2\2)9=EVfj\u0088\u008d\u0096")
        buf.write("\u009a\u009f\u00b0\u00b9\u00c0\u00d1\u00d6\u00de\u00e5")
        buf.write("\u00ee\u00f5\u0108\u011d\u012d\u0130\u0137\u0141\u0143")
        buf.write("\u0149\u0150\u0156\u016b\u016e\u0190\u0197\u019d\u01a3")
        buf.write("\u01b4\u01c9\u01dd")
        return buf.getvalue()


class patitoParser ( Parser ):

    grammarFileName = "patito.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", "'='", 
                     "'&&'", "'||'", "'+'", "'-'", "'*'", "'/'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "'$'", "'#'", "'?'", 
                     "','", "':'", "';'", "'program'", "'main'", "'function'", 
                     "'return'", "'input'", "'print'", "'if'", "'then'", 
                     "'else'", "'while'", "'do'", "'from'", "'to'", "'var'", 
                     "'bool'", "'int'", "'float'", "'string'", "'char'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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
    RULE_functions = 5
    RULE_function = 6
    RULE_functiontype = 7
    RULE_parameters = 8
    RULE_mexp = 9
    RULE_sexp = 10
    RULE_exp = 11
    RULE_term = 12
    RULE_factor = 13
    RULE_statute = 14
    RULE_assignation = 15
    RULE_funccall = 16
    RULE_returncall = 17
    RULE_indexvariable = 18
    RULE_read = 19
    RULE_write = 20
    RULE_conditional = 21
    RULE_whileloop = 22
    RULE_fromloop = 23
    RULE_mainfunc = 24

    ruleNames =  [ "program", "declarevars", "variables", "vartypes", "constant", 
                   "functions", "function", "functiontype", "parameters", 
                   "mexp", "sexp", "exp", "term", "factor", "statute", "assignation", 
                   "funccall", "returncall", "indexvariable", "read", "write", 
                   "conditional", "whileloop", "fromloop", "mainfunc" ]

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

    def __init__(self, compiler, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None
        self.compiler = compiler




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

        def mainfunc(self):
            return self.getTypedRuleContext(patitoParser.MainfuncContext,0)


        def declarevars(self):
            return self.getTypedRuleContext(patitoParser.DeclarevarsContext,0)


        def functions(self):
            return self.getTypedRuleContext(patitoParser.FunctionsContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(patitoParser.PROGRAM)
            self.state = 51
            self.match(patitoParser.ID)
            self.compiler._add_function(self.compiler.currentFunction)
            self.state = 53
            self.match(patitoParser.SEMICOLON)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.VAR:
                self.state = 54
                self.declarevars()


            self.compiler.goto_main_quad()
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.FUNCTION:
                self.state = 58
                self.functions()


            self.state = 61
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
            self.state = 63
            self.match(patitoParser.VAR)
            self.state = 65 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                self.variables()
                self.state = 67 
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
            self._CTE_INT = None # Token
            self.first_index = None # Token
            self.second_index = None # Token

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
            self.state = 69
            localctx._vartypes = self.vartypes()
            self.state = 70
            self.match(patitoParser.COLON)
            self.state = 71
            localctx._ID = self.match(patitoParser.ID)
            self.compiler.update_vars_table((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 73
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 74
                localctx._CTE_INT = self.match(patitoParser.CTE_INT)
                self.state = 75
                self.match(patitoParser.RIGHT_BRACKET)
                self.compiler.update_array_variable((None if localctx._ID is None else localctx._ID.text), (None if localctx._CTE_INT is None else localctx._CTE_INT.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))

            elif la_ == 2:
                self.state = 77
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 78
                localctx.first_index = self.match(patitoParser.CTE_INT)
                self.state = 79
                self.match(patitoParser.RIGHT_BRACKET)
                self.state = 80
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 81
                localctx.second_index = self.match(patitoParser.CTE_INT)
                self.state = 82
                self.match(patitoParser.RIGHT_BRACKET)
                self.compiler.update_matrix_variable((None if localctx._ID is None else localctx._ID.text), (None if localctx.first_index is None else localctx.first_index.text), (None if localctx.second_index is None else localctx.second_index.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))


            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 86
                self.match(patitoParser.COMMA)
                self.state = 87
                localctx._ID = self.match(patitoParser.ID)
                self.compiler.update_vars_table((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
                self.state = 100
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 89
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 90
                    localctx._CTE_INT = self.match(patitoParser.CTE_INT)
                    self.state = 91
                    self.match(patitoParser.RIGHT_BRACKET)
                    self.compiler.update_array_variable((None if localctx._ID is None else localctx._ID.text), (None if localctx._CTE_INT is None else localctx._CTE_INT.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))

                elif la_ == 2:
                    self.state = 93
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 94
                    localctx.first_index = self.match(patitoParser.CTE_INT)
                    self.state = 95
                    self.match(patitoParser.RIGHT_BRACKET)
                    self.state = 96
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 97
                    localctx.second_index = self.match(patitoParser.CTE_INT)
                    self.state = 98
                    self.match(patitoParser.RIGHT_BRACKET)
                    self.compiler.update_matrix_variable((None if localctx._ID is None else localctx._ID.text), (None if localctx.first_index is None else localctx.first_index.text), (None if localctx.second_index is None else localctx.second_index.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))


                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
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
            self.state = 109
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
            self._CTE_BOOL = None # Token
            self._CTE_FLOAT = None # Token
            self._CTE_INT = None # Token
            self._CTE_CHAR = None # Token
            self._CTE_STRING = None # Token

        def CTE_BOOL(self):
            return self.getToken(patitoParser.CTE_BOOL, 0)

        def SUB(self):
            return self.getToken(patitoParser.SUB, 0)

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
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 111
                localctx._CTE_BOOL = self.match(patitoParser.CTE_BOOL)
                self.compiler.add_operand((None if localctx._CTE_BOOL is None else localctx._CTE_BOOL.text))
                self.compiler.add_constant_to_type_stack_and_table("bool")
                pass

            elif la_ == 2:
                self.state = 114
                self.match(patitoParser.SUB)
                self.state = 115
                localctx._CTE_FLOAT = self.match(patitoParser.CTE_FLOAT)
                self.compiler.add_operand("-" + (None if localctx._CTE_FLOAT is None else localctx._CTE_FLOAT.text))
                self.compiler.add_constant_to_type_stack_and_table("float")
                pass

            elif la_ == 3:
                self.state = 118
                localctx._CTE_FLOAT = self.match(patitoParser.CTE_FLOAT)
                self.compiler.add_operand((None if localctx._CTE_FLOAT is None else localctx._CTE_FLOAT.text))
                self.compiler.add_constant_to_type_stack_and_table("float")
                pass

            elif la_ == 4:
                self.state = 121
                self.match(patitoParser.SUB)
                self.state = 122
                localctx._CTE_INT = self.match(patitoParser.CTE_INT)
                self.compiler.add_operand("-" + (None if localctx._CTE_INT is None else localctx._CTE_INT.text))
                self.compiler.add_constant_to_type_stack_and_table("int")
                pass

            elif la_ == 5:
                self.state = 125
                localctx._CTE_INT = self.match(patitoParser.CTE_INT)
                self.compiler.add_operand((None if localctx._CTE_INT is None else localctx._CTE_INT.text))
                self.compiler.add_constant_to_type_stack_and_table("int")
                pass

            elif la_ == 6:
                self.state = 128
                localctx._CTE_CHAR = self.match(patitoParser.CTE_CHAR)
                self.compiler.add_operand((None if localctx._CTE_CHAR is None else localctx._CTE_CHAR.text))
                self.compiler.add_constant_to_type_stack_and_table("char")
                pass

            elif la_ == 7:
                self.state = 131
                localctx._CTE_STRING = self.match(patitoParser.CTE_STRING)
                self.compiler.add_operand((None if localctx._CTE_STRING is None else localctx._CTE_STRING.text))
                self.compiler.add_constant_to_type_stack_and_table("string")
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
        self.enterRule(localctx, 10, self.RULE_functions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 136
                self.function()
                self.state = 139 
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
        self.enterRule(localctx, 12, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(patitoParser.FUNCTION)
            self.state = 142
            localctx._functiontype = self.functiontype()
            self.state = 143
            localctx._ID = self.match(patitoParser.ID)
            self.compiler.currentFunction=Function((None if localctx._ID is None else localctx._ID.text), (None if localctx._functiontype is None else self._input.getText(localctx._functiontype.start,localctx._functiontype.stop)), [], {})
            self.compiler.clear_local_memory()
            self.state = 146
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.BOOL) | (1 << patitoParser.INT) | (1 << patitoParser.FLOAT) | (1 << patitoParser.STRING) | (1 << patitoParser.CHAR))) != 0):
                self.state = 147
                self.parameters()


            self.state = 150
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.VAR:
                self.state = 151
                self.declarevars()


            self.compiler._add_function(self.compiler.currentFunction)
            self.state = 155
            self.match(patitoParser.LEFT_CURLY)
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 156
                self.statute()


            self.state = 159
            self.match(patitoParser.RIGHT_CURLY)
            self.compiler.create_endfunc()
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
        self.enterRule(localctx, 14, self.RULE_functiontype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
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
        self.enterRule(localctx, 16, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            localctx._vartypes = self.vartypes()
            self.state = 165
            localctx._ID = self.match(patitoParser.ID)
            self.compiler.update_parameters((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 167
                self.match(patitoParser.COMMA)
                self.state = 168
                localctx._vartypes = self.vartypes()
                self.state = 169
                localctx._ID = self.match(patitoParser.ID)
                self.compiler.update_parameters((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
                self.state = 176
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
        self.enterRule(localctx, 18, self.RULE_mexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.sexp()
            self.compiler.top_is_logic_operator()
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 183
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.AND]:
                        self.state = 179
                        localctx._AND = self.match(patitoParser.AND)
                        self.compiler.add_operator((None if localctx._AND is None else localctx._AND.text))
                        pass
                    elif token in [patitoParser.OR]:
                        self.state = 181
                        localctx._OR = self.match(patitoParser.OR)
                        self.compiler.add_operator((None if localctx._OR is None else localctx._OR.text))
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 185
                    self.mexp()
                    self.compiler.top_is_logic_operator()
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_sexp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.exp()
            self.compiler.top_is_comparison()
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.LESS) | (1 << patitoParser.GREATER) | (1 << patitoParser.LESS_EQUAL) | (1 << patitoParser.GREATER_EQUAL) | (1 << patitoParser.EQUAL) | (1 << patitoParser.NOT_EQUAL))) != 0):
                self.state = 207
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [patitoParser.GREATER]:
                    self.state = 195
                    localctx._GREATER = self.match(patitoParser.GREATER)
                    self.compiler.add_operator((None if localctx._GREATER is None else localctx._GREATER.text))
                    pass
                elif token in [patitoParser.LESS]:
                    self.state = 197
                    localctx._LESS = self.match(patitoParser.LESS)
                    self.compiler.add_operator((None if localctx._LESS is None else localctx._LESS.text))
                    pass
                elif token in [patitoParser.GREATER_EQUAL]:
                    self.state = 199
                    localctx._GREATER_EQUAL = self.match(patitoParser.GREATER_EQUAL)
                    self.compiler.add_operator((None if localctx._GREATER_EQUAL is None else localctx._GREATER_EQUAL.text))
                    pass
                elif token in [patitoParser.LESS_EQUAL]:
                    self.state = 201
                    localctx._LESS_EQUAL = self.match(patitoParser.LESS_EQUAL)
                    self.compiler.add_operator((None if localctx._LESS_EQUAL is None else localctx._LESS_EQUAL.text))
                    pass
                elif token in [patitoParser.NOT_EQUAL]:
                    self.state = 203
                    localctx._NOT_EQUAL = self.match(patitoParser.NOT_EQUAL)
                    self.compiler.add_operator((None if localctx._NOT_EQUAL is None else localctx._NOT_EQUAL.text))
                    pass
                elif token in [patitoParser.EQUAL]:
                    self.state = 205
                    localctx._EQUAL = self.match(patitoParser.EQUAL)
                    self.compiler.add_operator((None if localctx._EQUAL is None else localctx._EQUAL.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 209
                self.sexp()
                self.compiler.top_is_comparison()


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
        self.enterRule(localctx, 22, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.term()
            self.compiler.top_is_add_or_sub()
            self.state = 227
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 220
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.ADD]:
                        self.state = 216
                        localctx._ADD = self.match(patitoParser.ADD)
                        self.compiler.add_operator((None if localctx._ADD is None else localctx._ADD.text))
                        pass
                    elif token in [patitoParser.SUB]:
                        self.state = 218
                        localctx._SUB = self.match(patitoParser.SUB)
                        self.compiler.add_operator((None if localctx._SUB is None else localctx._SUB.text))
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 222
                    self.exp()
                    self.compiler.top_is_add_or_sub()
                self.state = 229
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        self.enterRule(localctx, 24, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.factor()
            self.compiler.top_is_mult_or_div()
            self.state = 243
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 236
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.MULT]:
                        self.state = 232
                        localctx._MULT = self.match(patitoParser.MULT)
                        self.compiler.add_operator((None if localctx._MULT is None else localctx._MULT.text))
                        pass
                    elif token in [patitoParser.DIV]:
                        self.state = 234
                        localctx._DIV = self.match(patitoParser.DIV)
                        self.compiler.add_operator((None if localctx._DIV is None else localctx._DIV.text))
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 238
                    self.term()
                    self.compiler.top_is_mult_or_div()
                self.state = 245
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
            self._ID = None # Token
            self._DETERMINANT = None # Token
            self._TRANSPOSE = None # Token
            self._INVERSE = None # Token

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
        self.enterRule(localctx, 26, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 246
                self.constant()
                pass

            elif la_ == 2:
                self.state = 247
                self.match(patitoParser.LEFT_PARENTHESIS)
                self.compiler.add_parenthesis()
                self.state = 249
                self.mexp()
                self.state = 250
                self.match(patitoParser.RIGHT_PARENTHESIS)
                self.compiler.pop_parenthesis()
                pass

            elif la_ == 3:
                self.state = 253
                localctx._ID = self.match(patitoParser.ID)
                self.compiler.add_operand_and_type((None if localctx._ID is None else localctx._ID.text))
                self.state = 283
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    pass

                elif la_ == 2:
                    self.state = 262
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.DETERMINANT]:
                        self.state = 256
                        localctx._DETERMINANT = self.match(patitoParser.DETERMINANT)
                        self.compiler.generate_matrix_operation_quad((None if localctx._DETERMINANT is None else localctx._DETERMINANT.text))
                        pass
                    elif token in [patitoParser.TRANSPOSE]:
                        self.state = 258
                        localctx._TRANSPOSE = self.match(patitoParser.TRANSPOSE)
                        self.compiler.generate_matrix_operation_quad((None if localctx._TRANSPOSE is None else localctx._TRANSPOSE.text))
                        pass
                    elif token in [patitoParser.INVERSE]:
                        self.state = 260
                        localctx._INVERSE = self.match(patitoParser.INVERSE)
                        self.compiler.generate_matrix_operation_quad((None if localctx._INVERSE is None else localctx._INVERSE.text))
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 3:
                    self.state = 264
                    self.match(patitoParser.LEFT_BRACKET)
                    self.compiler.add_parenthesis()
                    self.state = 266
                    self.mexp()
                    self.compiler.pop_parenthesis()
                    self.compiler.verify_one_index()
                    self.state = 269
                    self.match(patitoParser.RIGHT_BRACKET)
                    pass

                elif la_ == 4:
                    self.state = 271
                    self.match(patitoParser.LEFT_BRACKET)
                    self.compiler.add_parenthesis()
                    self.state = 273
                    self.mexp()
                    self.compiler.pop_parenthesis()
                    self.state = 275
                    self.match(patitoParser.RIGHT_BRACKET)
                    self.state = 276
                    self.match(patitoParser.LEFT_BRACKET)
                    self.compiler.add_parenthesis()
                    self.state = 278
                    self.mexp()
                    self.compiler.pop_parenthesis()
                    self.compiler.verify_two_indexes()
                    self.state = 281
                    self.match(patitoParser.RIGHT_BRACKET)
                    pass


                pass

            elif la_ == 4:
                self.state = 285
                localctx._ID = self.match(patitoParser.ID)
                self.compiler.validate_function_expression((None if localctx._ID is None else localctx._ID.text))
                self.state = 287
                self.match(patitoParser.LEFT_PARENTHESIS)
                self.compiler.add_parenthesis()
                currentCounter=0
                self.state = 302
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [patitoParser.RIGHT_PARENTHESIS]:
                    pass
                elif token in [patitoParser.SUB, patitoParser.LEFT_PARENTHESIS, patitoParser.CTE_BOOL, patitoParser.CTE_FLOAT, patitoParser.CTE_INT, patitoParser.CTE_CHAR, patitoParser.CTE_STRING, patitoParser.ID]:
                    self.state = 291
                    self.mexp()
                    currentCounter += 1
                    self.state = 299
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==patitoParser.COMMA:
                        self.state = 293
                        self.match(patitoParser.COMMA)
                        self.state = 294
                        self.mexp()
                        currentCounter += 1
                        self.state = 301
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                else:
                    raise NoViableAltException(self)

                self.compiler.validate_parameters((None if localctx._ID is None else localctx._ID.text), currentCounter)
                self.compiler.add_func_operand_and_type((None if localctx._ID is None else localctx._ID.text))
                self.compiler.goto_function_quad((None if localctx._ID is None else localctx._ID.text))
                self.state = 307
                self.match(patitoParser.RIGHT_PARENTHESIS)
                self.compiler.pop_parenthesis()
                pass


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


        def funccall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.FunccallContext)
            else:
                return self.getTypedRuleContext(patitoParser.FunccallContext,i)


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
        self.enterRule(localctx, 28, self.RULE_statute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.RETURN) | (1 << patitoParser.INPUT) | (1 << patitoParser.PRINT) | (1 << patitoParser.IF) | (1 << patitoParser.WHILE) | (1 << patitoParser.FROM) | (1 << patitoParser.ID))) != 0):
                self.state = 319
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 311
                    self.assignation()
                    pass

                elif la_ == 2:
                    self.state = 312
                    self.funccall()
                    pass

                elif la_ == 3:
                    self.state = 313
                    self.returncall()
                    pass

                elif la_ == 4:
                    self.state = 314
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 315
                    self.write()
                    pass

                elif la_ == 6:
                    self.state = 316
                    self.conditional()
                    pass

                elif la_ == 7:
                    self.state = 317
                    self.whileloop()
                    pass

                elif la_ == 8:
                    self.state = 318
                    self.fromloop()
                    pass


                self.state = 323
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
        self.enterRule(localctx, 30, self.RULE_assignation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            localctx._ID = self.match(patitoParser.ID)
            self.compiler.add_operand_and_type((None if localctx._ID is None else localctx._ID.text))
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.LEFT_BRACKET:
                self.state = 326
                self.indexvariable()


            self.state = 329
            localctx._ASSIGN = self.match(patitoParser.ASSIGN)
            self.compiler.add_operator((None if localctx._ASSIGN is None else localctx._ASSIGN.text))
            self.state = 340
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 331
                    localctx._ID = self.match(patitoParser.ID)
                    self.compiler.add_operand_and_type((None if localctx._ID is None else localctx._ID.text))
                    self.state = 334
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==patitoParser.LEFT_BRACKET:
                        self.state = 333
                        self.indexvariable()


                    self.state = 336
                    localctx._ASSIGN = self.match(patitoParser.ASSIGN)
                    self.compiler.add_operator((None if localctx._ASSIGN is None else localctx._ASSIGN.text))
                self.state = 342
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

            self.state = 343
            self.mexp()
            self.state = 344
            self.match(patitoParser.SEMICOLON)
            self.compiler.generate_assign_quads()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

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
            return patitoParser.RULE_funccall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunccall" ):
                listener.enterFunccall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunccall" ):
                listener.exitFunccall(self)




    def funccall(self):

        localctx = patitoParser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_funccall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            localctx._ID = self.match(patitoParser.ID)
            self.compiler.validate_void_function((None if localctx._ID is None else localctx._ID.text))
            self.state = 349
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.compiler.add_parenthesis()
            currentCounter=0
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [patitoParser.RIGHT_PARENTHESIS]:
                pass
            elif token in [patitoParser.SUB, patitoParser.LEFT_PARENTHESIS, patitoParser.CTE_BOOL, patitoParser.CTE_FLOAT, patitoParser.CTE_INT, patitoParser.CTE_CHAR, patitoParser.CTE_STRING, patitoParser.ID]:
                self.state = 353
                self.mexp()
                currentCounter += 1
                self.state = 361
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==patitoParser.COMMA:
                    self.state = 355
                    self.match(patitoParser.COMMA)
                    self.state = 356
                    self.mexp()
                    currentCounter += 1
                    self.state = 363
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.compiler.validate_parameters((None if localctx._ID is None else localctx._ID.text), currentCounter)
            self.compiler.goto_void_function_quad((None if localctx._ID is None else localctx._ID.text))
            self.state = 368
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 369
            self.match(patitoParser.SEMICOLON)
            self.compiler.pop_parenthesis()
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
        self.enterRule(localctx, 34, self.RULE_returncall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(patitoParser.RETURN)
            self.state = 373
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 374
            self.mexp()
            self.state = 375
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 376
            self.match(patitoParser.SEMICOLON)
            self.compiler.create_return_endfunc_goto()
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
        self.enterRule(localctx, 36, self.RULE_indexvariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 379
                self.match(patitoParser.LEFT_BRACKET)
                self.compiler.add_parenthesis()
                self.state = 381
                self.mexp()
                self.compiler.pop_parenthesis()
                self.compiler.verify_one_index()
                self.state = 384
                self.match(patitoParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.state = 386
                self.match(patitoParser.LEFT_BRACKET)
                self.compiler.add_parenthesis()
                self.state = 388
                self.mexp()
                self.compiler.pop_parenthesis()
                self.state = 390
                self.match(patitoParser.RIGHT_BRACKET)
                self.state = 391
                self.match(patitoParser.LEFT_BRACKET)
                self.compiler.add_parenthesis()
                self.state = 393
                self.mexp()
                self.compiler.pop_parenthesis()
                self.compiler.verify_two_indexes()
                self.state = 396
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
            self.varId = None # Token
            self.varId2 = None # Token

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
        self.enterRule(localctx, 38, self.RULE_read)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(patitoParser.INPUT)
            self.state = 401
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 402
            localctx.varId = self.match(patitoParser.ID)
            self.compiler.add_operand_and_type((None if localctx.varId is None else localctx.varId.text))
            self.state = 405
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.LEFT_BRACKET:
                self.state = 404
                self.indexvariable()


            self.compiler.generate_read_quad()
            self.state = 417
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 408
                self.match(patitoParser.COMMA)
                self.state = 409
                localctx.varId2 = self.match(patitoParser.ID)
                self.state = 411
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==patitoParser.LEFT_BRACKET:
                    self.state = 410
                    self.indexvariable()


                self.compiler.add_operand_and_type((None if localctx.varId2 is None else localctx.varId2.text))
                self.compiler.generate_read_quad()
                self.state = 419
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 420
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 421
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
        self.enterRule(localctx, 40, self.RULE_write)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(patitoParser.PRINT)
            self.state = 424
            self.match(patitoParser.LEFT_PARENTHESIS)

            self.state = 425
            self.mexp()
            self.compiler.generate_write_quad()
            self.state = 434
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 428
                self.match(patitoParser.COMMA)

                self.state = 429
                self.mexp()
                self.compiler.generate_write_quad()
                self.state = 436
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 437
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 438
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
        self.enterRule(localctx, 42, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(patitoParser.IF)
            self.state = 441
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 442
            self.mexp()
            self.state = 443
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.compiler.generate_if_quad()
            self.state = 445
            self.match(patitoParser.THEN)
            self.state = 446
            self.match(patitoParser.LEFT_CURLY)
            self.state = 447
            self.statute()
            self.state = 448
            self.match(patitoParser.RIGHT_CURLY)
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.ELSE:
                self.state = 449
                self.match(patitoParser.ELSE)
                self.compiler.generate_go_to_quad()
                self.state = 451
                self.match(patitoParser.LEFT_CURLY)
                self.state = 452
                self.statute()
                self.state = 453
                self.match(patitoParser.RIGHT_CURLY)


            self.compiler.generate_end_if_quad()
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
        self.enterRule(localctx, 44, self.RULE_whileloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(patitoParser.WHILE)
            self.state = 460
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.compiler.generate_while_before_check()
            self.state = 462
            self.mexp()
            self.state = 463
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.compiler.generate_while_after_check()
            self.state = 465
            self.match(patitoParser.DO)
            self.state = 466
            self.match(patitoParser.LEFT_CURLY)
            self.state = 467
            self.statute()
            self.compiler.generate_while_end()
            self.state = 469
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
            self._ID = None # Token
            self._ASSIGN = None # Token

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
        self.enterRule(localctx, 46, self.RULE_fromloop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(patitoParser.FROM)
            self.state = 472
            localctx._ID = self.match(patitoParser.ID)
            self.compiler.add_from_var_operand((None if localctx._ID is None else localctx._ID.text))
            self.state = 475
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.LEFT_BRACKET:
                self.state = 474
                self.indexvariable()


            self.state = 477
            localctx._ASSIGN = self.match(patitoParser.ASSIGN)
            self.compiler.add_operator((None if localctx._ASSIGN is None else localctx._ASSIGN.text))
            self.state = 479
            self.mexp()
            self.compiler.generate_assign_quads()
            self.state = 481
            self.match(patitoParser.TO)
            self.compiler.generate_from_before_check()
            self.state = 483
            self.mexp()
            self.compiler.generate_from_after_check()
            self.state = 485
            self.match(patitoParser.DO)
            self.state = 486
            self.match(patitoParser.LEFT_CURLY)
            self.state = 487
            self.statute()
            self.state = 488
            self.match(patitoParser.RIGHT_CURLY)
            self.compiler.generate_end_from_quad()
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
        self.enterRule(localctx, 48, self.RULE_mainfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(patitoParser.MAIN)
            self.compiler.currentFunction=Function("main", "void", [], {})
            self.compiler.clear_local_memory()
            self.state = 494
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 495
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.compiler._add_function(self.compiler.currentFunction)
            self.state = 497
            self.match(patitoParser.LEFT_CURLY)
            self.compiler.fill_goto_main_quad()
            self.state = 499
            self.statute()
            self.state = 500
            self.match(patitoParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





