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
        buf.write("\u01a4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\6\3C\n\3\r\3\16\3D\3\4\3\4\3\4")
        buf.write("\3\4\5\4K\n\4\3\4\3\4\3\4\3\4\5\4Q\n\4\3\4\7\4T\n\4\f")
        buf.write("\4\16\4W\13\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\5\6g\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\5\7r\n\7\3\b\6\bu\n\b\r\b\16\bv\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\5\t\177\n\t\3\t\3\t\5\t\u0083\n\t\3\t\3\t\3")
        buf.write("\t\5\t\u0088\n\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\7\13\u0096\n\13\f\13\16\13\u0099\13")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u00a2\n\f\f\f\16\f")
        buf.write("\u00a5\13\f\3\r\3\r\3\r\3\r\3\r\5\r\u00ac\n\r\3\r\7\r")
        buf.write("\u00af\n\r\f\r\16\r\u00b2\13\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00c1\n")
        buf.write("\16\3\16\5\16\u00c4\n\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u00cc\n\17\3\17\3\17\3\17\7\17\u00d1\n\17\f\17\16")
        buf.write("\17\u00d4\13\17\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00dc")
        buf.write("\n\20\3\20\3\20\3\20\7\20\u00e1\n\20\f\20\16\20\u00e4")
        buf.write("\13\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21")
        buf.write("\u0104\n\21\f\21\16\21\u0107\13\21\5\21\u0109\n\21\3\21")
        buf.write("\3\21\5\21\u010d\n\21\5\21\u010f\n\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\7\22\u0119\n\22\f\22\16\22\u011c")
        buf.write("\13\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\5\23\u012c\n\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u0139\n")
        buf.write("\24\f\24\16\24\u013c\13\24\5\24\u013e\n\24\3\24\3\24\3")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0156")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\27\7\27\u015d\n\27\f\27\16")
        buf.write("\27\u0160\13\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u0169\n\30\3\30\3\30\3\30\5\30\u016e\n\30\7\30\u0170")
        buf.write("\n\30\f\30\16\30\u0173\13\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u0185\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\2\2\35\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\66\2\5\3\2-\61\4\2-\61\67\67\3\2\31\33")
        buf.write("\2\u01be\28\3\2\2\2\4@\3\2\2\2\6F\3\2\2\2\bZ\3\2\2\2\n")
        buf.write("f\3\2\2\2\fq\3\2\2\2\16t\3\2\2\2\20x\3\2\2\2\22\u008b")
        buf.write("\3\2\2\2\24\u008d\3\2\2\2\26\u009a\3\2\2\2\30\u00a6\3")
        buf.write("\2\2\2\32\u00b3\3\2\2\2\34\u00c5\3\2\2\2\36\u00d5\3\2")
        buf.write("\2\2 \u010e\3\2\2\2\"\u011a\3\2\2\2$\u011d\3\2\2\2&\u0132")
        buf.write("\3\2\2\2(\u0142\3\2\2\2*\u0148\3\2\2\2,\u0157\3\2\2\2")
        buf.write(".\u0164\3\2\2\2\60\u0177\3\2\2\2\62\u0186\3\2\2\2\64\u018f")
        buf.write("\3\2\2\2\66\u019a\3\2\2\289\7\37\2\29:\78\2\2:;\7\36\2")
        buf.write("\2;<\5\4\3\2<=\b\2\1\2=>\5\16\b\2>?\5\66\34\2?\3\3\2\2")
        buf.write("\2@B\7,\2\2AC\5\6\4\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE")
        buf.write("\3\2\2\2E\5\3\2\2\2FG\5\b\5\2GH\7\35\2\2HJ\78\2\2IK\5")
        buf.write("\f\7\2JI\3\2\2\2JK\3\2\2\2KL\3\2\2\2LU\b\4\1\2MN\7\34")
        buf.write("\2\2NP\78\2\2OQ\5\f\7\2PO\3\2\2\2PQ\3\2\2\2QR\3\2\2\2")
        buf.write("RT\b\4\1\2SM\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2VX\3")
        buf.write("\2\2\2WU\3\2\2\2XY\7\36\2\2Y\7\3\2\2\2Z[\t\2\2\2[\t\3")
        buf.write("\2\2\2\\]\7\62\2\2]g\b\6\1\2^_\7\63\2\2_g\b\6\1\2`a\7")
        buf.write("\64\2\2ag\b\6\1\2bc\7\65\2\2cg\b\6\1\2de\7\66\2\2eg\b")
        buf.write("\6\1\2f\\\3\2\2\2f^\3\2\2\2f`\3\2\2\2fb\3\2\2\2fd\3\2")
        buf.write("\2\2g\13\3\2\2\2hi\7\25\2\2ij\7\64\2\2jr\7\26\2\2kl\7")
        buf.write("\25\2\2lm\7\64\2\2mn\7\26\2\2no\7\25\2\2op\7\64\2\2pr")
        buf.write("\7\26\2\2qh\3\2\2\2qk\3\2\2\2r\r\3\2\2\2su\5\20\t\2ts")
        buf.write("\3\2\2\2uv\3\2\2\2vt\3\2\2\2vw\3\2\2\2w\17\3\2\2\2xy\7")
        buf.write("!\2\2yz\5\22\n\2z{\78\2\2{|\b\t\1\2|~\7\23\2\2}\177\5")
        buf.write("\24\13\2~}\3\2\2\2~\177\3\2\2\2\177\u0080\3\2\2\2\u0080")
        buf.write("\u0082\7\24\2\2\u0081\u0083\5\4\3\2\u0082\u0081\3\2\2")
        buf.write("\2\u0082\u0083\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0085")
        buf.write("\b\t\1\2\u0085\u0087\7\27\2\2\u0086\u0088\5\"\22\2\u0087")
        buf.write("\u0086\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\3\2\2\2")
        buf.write("\u0089\u008a\7\30\2\2\u008a\21\3\2\2\2\u008b\u008c\t\3")
        buf.write("\2\2\u008c\23\3\2\2\2\u008d\u008e\5\b\5\2\u008e\u008f")
        buf.write("\78\2\2\u008f\u0097\b\13\1\2\u0090\u0091\7\34\2\2\u0091")
        buf.write("\u0092\5\b\5\2\u0092\u0093\78\2\2\u0093\u0094\b\13\1\2")
        buf.write("\u0094\u0096\3\2\2\2\u0095\u0090\3\2\2\2\u0096\u0099\3")
        buf.write("\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\25")
        buf.write("\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u009b\5\30\r\2\u009b")
        buf.write("\u00a3\b\f\1\2\u009c\u009d\7\f\2\2\u009d\u009e\b\f\1\2")
        buf.write("\u009e\u009f\5\30\r\2\u009f\u00a0\b\f\1\2\u00a0\u00a2")
        buf.write("\3\2\2\2\u00a1\u009c\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3")
        buf.write("\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\27\3\2\2\2\u00a5")
        buf.write("\u00a3\3\2\2\2\u00a6\u00b0\5\32\16\2\u00a7\u00a8\7\r\2")
        buf.write("\2\u00a8\u00ac\b\r\1\2\u00a9\u00aa\7\16\2\2\u00aa\u00ac")
        buf.write("\b\r\1\2\u00ab\u00a7\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac")
        buf.write("\u00ad\3\2\2\2\u00ad\u00af\5\30\r\2\u00ae\u00ab\3\2\2")
        buf.write("\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1")
        buf.write("\3\2\2\2\u00b1\31\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00c3")
        buf.write("\5\34\17\2\u00b4\u00b5\7\7\2\2\u00b5\u00c1\b\16\1\2\u00b6")
        buf.write("\u00b7\7\6\2\2\u00b7\u00c1\b\16\1\2\u00b8\u00b9\7\t\2")
        buf.write("\2\u00b9\u00c1\b\16\1\2\u00ba\u00bb\7\b\2\2\u00bb\u00c1")
        buf.write("\b\16\1\2\u00bc\u00bd\7\13\2\2\u00bd\u00c1\b\16\1\2\u00be")
        buf.write("\u00bf\7\n\2\2\u00bf\u00c1\b\16\1\2\u00c0\u00b4\3\2\2")
        buf.write("\2\u00c0\u00b6\3\2\2\2\u00c0\u00b8\3\2\2\2\u00c0\u00ba")
        buf.write("\3\2\2\2\u00c0\u00bc\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1")
        buf.write("\u00c2\3\2\2\2\u00c2\u00c4\5\32\16\2\u00c3\u00c0\3\2\2")
        buf.write("\2\u00c3\u00c4\3\2\2\2\u00c4\33\3\2\2\2\u00c5\u00c6\5")
        buf.write("\36\20\2\u00c6\u00d2\b\17\1\2\u00c7\u00c8\7\17\2\2\u00c8")
        buf.write("\u00cc\b\17\1\2\u00c9\u00ca\7\20\2\2\u00ca\u00cc\b\17")
        buf.write("\1\2\u00cb\u00c7\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00cd")
        buf.write("\3\2\2\2\u00cd\u00ce\5\34\17\2\u00ce\u00cf\b\17\1\2\u00cf")
        buf.write("\u00d1\3\2\2\2\u00d0\u00cb\3\2\2\2\u00d1\u00d4\3\2\2\2")
        buf.write("\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\35\3\2")
        buf.write("\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00d6\5 \21\2\u00d6\u00e2")
        buf.write("\b\20\1\2\u00d7\u00d8\7\21\2\2\u00d8\u00dc\b\20\1\2\u00d9")
        buf.write("\u00da\7\22\2\2\u00da\u00dc\b\20\1\2\u00db\u00d7\3\2\2")
        buf.write("\2\u00db\u00d9\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de")
        buf.write("\5\36\20\2\u00de\u00df\b\20\1\2\u00df\u00e1\3\2\2\2\u00e0")
        buf.write("\u00db\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2")
        buf.write("\u00e2\u00e3\3\2\2\2\u00e3\37\3\2\2\2\u00e4\u00e2\3\2")
        buf.write("\2\2\u00e5\u00e6\5\n\6\2\u00e6\u00e7\b\21\1\2\u00e7\u010f")
        buf.write("\3\2\2\2\u00e8\u00e9\7\23\2\2\u00e9\u00ea\b\21\1\2\u00ea")
        buf.write("\u00eb\5\30\r\2\u00eb\u00ec\7\24\2\2\u00ec\u00ed\b\21")
        buf.write("\1\2\u00ed\u010f\3\2\2\2\u00ee\u00ef\78\2\2\u00ef\u010c")
        buf.write("\b\21\1\2\u00f0\u010d\3\2\2\2\u00f1\u010d\t\4\2\2\u00f2")
        buf.write("\u00f3\7\25\2\2\u00f3\u00f4\5\30\r\2\u00f4\u00f5\7\26")
        buf.write("\2\2\u00f5\u010d\3\2\2\2\u00f6\u00f7\7\25\2\2\u00f7\u00f8")
        buf.write("\5\30\r\2\u00f8\u00f9\7\26\2\2\u00f9\u00fa\7\25\2\2\u00fa")
        buf.write("\u00fb\5\30\r\2\u00fb\u00fc\7\26\2\2\u00fc\u010d\3\2\2")
        buf.write("\2\u00fd\u00fe\7\23\2\2\u00fe\u0108\b\21\1\2\u00ff\u0109")
        buf.write("\3\2\2\2\u0100\u0105\5\30\r\2\u0101\u0102\7\34\2\2\u0102")
        buf.write("\u0104\5\30\r\2\u0103\u0101\3\2\2\2\u0104\u0107\3\2\2")
        buf.write("\2\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0109")
        buf.write("\3\2\2\2\u0107\u0105\3\2\2\2\u0108\u00ff\3\2\2\2\u0108")
        buf.write("\u0100\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b\7\24\2")
        buf.write("\2\u010b\u010d\b\21\1\2\u010c\u00f0\3\2\2\2\u010c\u00f1")
        buf.write("\3\2\2\2\u010c\u00f2\3\2\2\2\u010c\u00f6\3\2\2\2\u010c")
        buf.write("\u00fd\3\2\2\2\u010d\u010f\3\2\2\2\u010e\u00e5\3\2\2\2")
        buf.write("\u010e\u00e8\3\2\2\2\u010e\u00ee\3\2\2\2\u010f!\3\2\2")
        buf.write("\2\u0110\u0119\5$\23\2\u0111\u0119\5&\24\2\u0112\u0119")
        buf.write("\5(\25\2\u0113\u0119\5,\27\2\u0114\u0119\5.\30\2\u0115")
        buf.write("\u0119\5\60\31\2\u0116\u0119\5\62\32\2\u0117\u0119\5\64")
        buf.write("\33\2\u0118\u0110\3\2\2\2\u0118\u0111\3\2\2\2\u0118\u0112")
        buf.write("\3\2\2\2\u0118\u0113\3\2\2\2\u0118\u0114\3\2\2\2\u0118")
        buf.write("\u0115\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0117\3\2\2\2")
        buf.write("\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b\3")
        buf.write("\2\2\2\u011b#\3\2\2\2\u011c\u011a\3\2\2\2\u011d\u011e")
        buf.write("\78\2\2\u011e\u012b\b\23\1\2\u011f\u012c\3\2\2\2\u0120")
        buf.write("\u0121\7\25\2\2\u0121\u0122\5\30\r\2\u0122\u0123\7\26")
        buf.write("\2\2\u0123\u012c\3\2\2\2\u0124\u0125\7\25\2\2\u0125\u0126")
        buf.write("\5\30\r\2\u0126\u0127\7\26\2\2\u0127\u0128\7\25\2\2\u0128")
        buf.write("\u0129\5\30\r\2\u0129\u012a\7\26\2\2\u012a\u012c\3\2\2")
        buf.write("\2\u012b\u011f\3\2\2\2\u012b\u0120\3\2\2\2\u012b\u0124")
        buf.write("\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012e\7\f\2\2\u012e")
        buf.write("\u012f\b\23\1\2\u012f\u0130\5\26\f\2\u0130\u0131\7\36")
        buf.write("\2\2\u0131%\3\2\2\2\u0132\u0133\78\2\2\u0133\u013d\7\23")
        buf.write("\2\2\u0134\u013e\3\2\2\2\u0135\u013a\5\30\r\2\u0136\u0137")
        buf.write("\7\34\2\2\u0137\u0139\5\30\r\2\u0138\u0136\3\2\2\2\u0139")
        buf.write("\u013c\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b\3\2\2\2")
        buf.write("\u013b\u013e\3\2\2\2\u013c\u013a\3\2\2\2\u013d\u0134\3")
        buf.write("\2\2\2\u013d\u0135\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140")
        buf.write("\7\24\2\2\u0140\u0141\7\36\2\2\u0141\'\3\2\2\2\u0142\u0143")
        buf.write("\7\"\2\2\u0143\u0144\7\23\2\2\u0144\u0145\5\30\r\2\u0145")
        buf.write("\u0146\7\24\2\2\u0146\u0147\7\36\2\2\u0147)\3\2\2\2\u0148")
        buf.write("\u0155\78\2\2\u0149\u0156\3\2\2\2\u014a\u014b\7\25\2\2")
        buf.write("\u014b\u014c\5\30\r\2\u014c\u014d\7\26\2\2\u014d\u0156")
        buf.write("\3\2\2\2\u014e\u014f\7\25\2\2\u014f\u0150\5\30\r\2\u0150")
        buf.write("\u0151\7\26\2\2\u0151\u0152\7\25\2\2\u0152\u0153\5\30")
        buf.write("\r\2\u0153\u0154\7\26\2\2\u0154\u0156\3\2\2\2\u0155\u0149")
        buf.write("\3\2\2\2\u0155\u014a\3\2\2\2\u0155\u014e\3\2\2\2\u0156")
        buf.write("+\3\2\2\2\u0157\u0158\7#\2\2\u0158\u0159\7\23\2\2\u0159")
        buf.write("\u015e\5*\26\2\u015a\u015b\7\34\2\2\u015b\u015d\5*\26")
        buf.write("\2\u015c\u015a\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c")
        buf.write("\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0161\3\2\2\2\u0160")
        buf.write("\u015e\3\2\2\2\u0161\u0162\7\24\2\2\u0162\u0163\7\36\2")
        buf.write("\2\u0163-\3\2\2\2\u0164\u0165\7$\2\2\u0165\u0168\7\23")
        buf.write("\2\2\u0166\u0169\5\26\f\2\u0167\u0169\7\66\2\2\u0168\u0166")
        buf.write("\3\2\2\2\u0168\u0167\3\2\2\2\u0169\u0171\3\2\2\2\u016a")
        buf.write("\u016d\7\34\2\2\u016b\u016e\5\26\f\2\u016c\u016e\7\66")
        buf.write("\2\2\u016d\u016b\3\2\2\2\u016d\u016c\3\2\2\2\u016e\u0170")
        buf.write("\3\2\2\2\u016f\u016a\3\2\2\2\u0170\u0173\3\2\2\2\u0171")
        buf.write("\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0174\3\2\2\2")
        buf.write("\u0173\u0171\3\2\2\2\u0174\u0175\7\24\2\2\u0175\u0176")
        buf.write("\7\36\2\2\u0176/\3\2\2\2\u0177\u0178\7%\2\2\u0178\u0179")
        buf.write("\7\23\2\2\u0179\u017a\5\30\r\2\u017a\u017b\7\24\2\2\u017b")
        buf.write("\u017c\7&\2\2\u017c\u017d\7\27\2\2\u017d\u017e\5\"\22")
        buf.write("\2\u017e\u0184\7\30\2\2\u017f\u0180\7\'\2\2\u0180\u0181")
        buf.write("\7\27\2\2\u0181\u0182\5\"\22\2\u0182\u0183\7\30\2\2\u0183")
        buf.write("\u0185\3\2\2\2\u0184\u017f\3\2\2\2\u0184\u0185\3\2\2\2")
        buf.write("\u0185\61\3\2\2\2\u0186\u0187\7(\2\2\u0187\u0188\7\23")
        buf.write("\2\2\u0188\u0189\5\30\r\2\u0189\u018a\7\24\2\2\u018a\u018b")
        buf.write("\7)\2\2\u018b\u018c\7\27\2\2\u018c\u018d\5\"\22\2\u018d")
        buf.write("\u018e\7\30\2\2\u018e\63\3\2\2\2\u018f\u0190\7*\2\2\u0190")
        buf.write("\u0191\5*\26\2\u0191\u0192\7\f\2\2\u0192\u0193\5\30\r")
        buf.write("\2\u0193\u0194\7+\2\2\u0194\u0195\5\30\r\2\u0195\u0196")
        buf.write("\7)\2\2\u0196\u0197\7\27\2\2\u0197\u0198\5\"\22\2\u0198")
        buf.write("\u0199\7\30\2\2\u0199\65\3\2\2\2\u019a\u019b\7 \2\2\u019b")
        buf.write("\u019c\b\34\1\2\u019c\u019d\7\23\2\2\u019d\u019e\7\24")
        buf.write("\2\2\u019e\u019f\b\34\1\2\u019f\u01a0\7\27\2\2\u01a0\u01a1")
        buf.write("\5\"\22\2\u01a1\u01a2\7\30\2\2\u01a2\67\3\2\2\2%DJPUf")
        buf.write("qv~\u0082\u0087\u0097\u00a3\u00ab\u00b0\u00c0\u00c3\u00cb")
        buf.write("\u00d2\u00db\u00e2\u0105\u0108\u010c\u010e\u0118\u011a")
        buf.write("\u012b\u013a\u013d\u0155\u015e\u0168\u016d\u0171\u0184")
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
    RULE_array = 5
    RULE_functions = 6
    RULE_function = 7
    RULE_functiontype = 8
    RULE_parameters = 9
    RULE_hexp = 10
    RULE_mexp = 11
    RULE_sexp = 12
    RULE_exp = 13
    RULE_term = 14
    RULE_factor = 15
    RULE_statute = 16
    RULE_assignation = 17
    RULE_voidcall = 18
    RULE_returncall = 19
    RULE_indexvariable = 20
    RULE_read = 21
    RULE_write = 22
    RULE_conditional = 23
    RULE_whileloop = 24
    RULE_fromloop = 25
    RULE_mainfunc = 26

    ruleNames =  [ "program", "declarevars", "variables", "vartypes", "constant", 
                   "array", "functions", "function", "functiontype", "parameters", 
                   "hexp", "mexp", "sexp", "exp", "term", "factor", "statute", 
                   "assignation", "voidcall", "returncall", "indexvariable", 
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
            self.state = 54
            self.match(patitoParser.PROGRAM)
            self.state = 55
            self.match(patitoParser.ID)
            self.state = 56
            self.match(patitoParser.SEMICOLON)
            self.state = 57
            self.declarevars()
            compiler._add_function(compiler.currentFunction)
            self.state = 59
            self.functions()
            self.state = 60
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
            self.state = 62
            self.match(patitoParser.VAR)
            self.state = 64 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 63
                self.variables()
                self.state = 66 
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

        def array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.ArrayContext)
            else:
                return self.getTypedRuleContext(patitoParser.ArrayContext,i)


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
            self.state = 68
            localctx._vartypes = self.vartypes()
            self.state = 69
            self.match(patitoParser.COLON)
            self.state = 70
            localctx._ID = self.match(patitoParser.ID)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.LEFT_BRACKET:
                self.state = 71
                self.array()


            compiler.currentFunction._update_vars_table((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 75
                self.match(patitoParser.COMMA)
                self.state = 76
                localctx._ID = self.match(patitoParser.ID)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==patitoParser.LEFT_BRACKET:
                    self.state = 77
                    self.array()


                compiler.currentFunction._update_vars_table((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
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
            self.state = 88
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
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [patitoParser.CTE_BOOL]:
                self.state = 90
                self.match(patitoParser.CTE_BOOL)
                compiler.addType("bool")
                pass
            elif token in [patitoParser.CTE_FLOAT]:
                self.state = 92
                self.match(patitoParser.CTE_FLOAT)
                compiler.addType("float")
                pass
            elif token in [patitoParser.CTE_INT]:
                self.state = 94
                self.match(patitoParser.CTE_INT)
                compiler.addType("int")
                pass
            elif token in [patitoParser.CTE_CHAR]:
                self.state = 96
                self.match(patitoParser.CTE_CHAR)
                compiler.addType("char")
                pass
            elif token in [patitoParser.CTE_STRING]:
                self.state = 98
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


    class ArrayContext(ParserRuleContext):

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
            return patitoParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = patitoParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 103
                self.match(patitoParser.CTE_INT)
                self.state = 104
                self.match(patitoParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 106
                self.match(patitoParser.CTE_INT)
                self.state = 107
                self.match(patitoParser.RIGHT_BRACKET)
                self.state = 108
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 109
                self.match(patitoParser.CTE_INT)
                self.state = 110
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
            self.state = 114 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 113
                self.function()
                self.state = 116 
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
            self.state = 118
            self.match(patitoParser.FUNCTION)
            self.state = 119
            localctx._functiontype = self.functiontype()
            self.state = 120
            localctx._ID = self.match(patitoParser.ID)
            compiler.currentFunction=Function((None if localctx._ID is None else localctx._ID.text), (None if localctx._functiontype is None else self._input.getText(localctx._functiontype.start,localctx._functiontype.stop)), {}, {})
            self.state = 122
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.BOOL) | (1 << patitoParser.INT) | (1 << patitoParser.FLOAT) | (1 << patitoParser.STRING) | (1 << patitoParser.CHAR))) != 0):
                self.state = 123
                self.parameters()


            self.state = 126
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.VAR:
                self.state = 127
                self.declarevars()


            compiler._add_function(compiler.currentFunction)
            self.state = 131
            self.match(patitoParser.LEFT_CURLY)
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 132
                self.statute()


            self.state = 135
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
            self.state = 137
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
            self.state = 139
            localctx._vartypes = self.vartypes()
            self.state = 140
            localctx._ID = self.match(patitoParser.ID)
            compiler.currentFunction._update_parameters((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 142
                self.match(patitoParser.COMMA)
                self.state = 143
                localctx._vartypes = self.vartypes()
                self.state = 144
                localctx._ID = self.match(patitoParser.ID)
                compiler.currentFunction._update_parameters((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ASSIGN = None # Token

        def mexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.MexpContext)
            else:
                return self.getTypedRuleContext(patitoParser.MexpContext,i)


        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.ASSIGN)
            else:
                return self.getToken(patitoParser.ASSIGN, i)

        def getRuleIndex(self):
            return patitoParser.RULE_hexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHexp" ):
                listener.enterHexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHexp" ):
                listener.exitHexp(self)




    def hexp(self):

        localctx = patitoParser.HexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_hexp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.mexp()
            compiler.topIsAssignment()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.ASSIGN:
                self.state = 154
                localctx._ASSIGN = self.match(patitoParser.ASSIGN)
                compiler.addOperator((None if localctx._ASSIGN is None else localctx._ASSIGN.text))
                self.state = 156
                self.mexp()
                compiler.topIsAssignment()
                self.state = 163
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
        self.enterRule(localctx, 22, self.RULE_mexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.sexp()
            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 169
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.AND]:
                        self.state = 165
                        localctx._AND = self.match(patitoParser.AND)
                        compiler.addOperator((None if localctx._AND is None else localctx._AND.text))
                        pass
                    elif token in [patitoParser.OR]:
                        self.state = 167
                        localctx._OR = self.match(patitoParser.OR)
                        compiler.addOperator((None if localctx._OR is None else localctx._OR.text))
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 171
                    self.mexp() 
                self.state = 176
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
        self.enterRule(localctx, 24, self.RULE_sexp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.exp()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.LESS) | (1 << patitoParser.GREATER) | (1 << patitoParser.LESS_EQUAL) | (1 << patitoParser.GREATER_EQUAL) | (1 << patitoParser.EQUAL) | (1 << patitoParser.NOT_EQUAL))) != 0):
                self.state = 190
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [patitoParser.GREATER]:
                    self.state = 178
                    localctx._GREATER = self.match(patitoParser.GREATER)
                    compiler.addOperator((None if localctx._GREATER is None else localctx._GREATER.text))
                    pass
                elif token in [patitoParser.LESS]:
                    self.state = 180
                    localctx._LESS = self.match(patitoParser.LESS)
                    compiler.addOperator((None if localctx._LESS is None else localctx._LESS.text))
                    pass
                elif token in [patitoParser.GREATER_EQUAL]:
                    self.state = 182
                    localctx._GREATER_EQUAL = self.match(patitoParser.GREATER_EQUAL)
                    compiler.addOperator((None if localctx._GREATER_EQUAL is None else localctx._GREATER_EQUAL.text))
                    pass
                elif token in [patitoParser.LESS_EQUAL]:
                    self.state = 184
                    localctx._LESS_EQUAL = self.match(patitoParser.LESS_EQUAL)
                    compiler.addOperator((None if localctx._LESS_EQUAL is None else localctx._LESS_EQUAL.text))
                    pass
                elif token in [patitoParser.NOT_EQUAL]:
                    self.state = 186
                    localctx._NOT_EQUAL = self.match(patitoParser.NOT_EQUAL)
                    compiler.addOperator((None if localctx._NOT_EQUAL is None else localctx._NOT_EQUAL.text))
                    pass
                elif token in [patitoParser.EQUAL]:
                    self.state = 188
                    localctx._EQUAL = self.match(patitoParser.EQUAL)
                    compiler.addOperator((None if localctx._EQUAL is None else localctx._EQUAL.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 192
                self.sexp()


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
        self.enterRule(localctx, 26, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.term()
            compiler.topIsAddOrSub()
            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 201
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.ADD]:
                        self.state = 197
                        localctx._ADD = self.match(patitoParser.ADD)
                        compiler.addOperator((None if localctx._ADD is None else localctx._ADD.text))
                        pass
                    elif token in [patitoParser.SUB]:
                        self.state = 199
                        localctx._SUB = self.match(patitoParser.SUB)
                        compiler.addOperator((None if localctx._SUB is None else localctx._SUB.text))
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 203
                    self.exp()
                    compiler.topIsAddOrSub() 
                self.state = 210
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
        self.enterRule(localctx, 28, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.factor()
            compiler.topIsMultOrDiv()
            self.state = 224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 217
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.MULT]:
                        self.state = 213
                        localctx._MULT = self.match(patitoParser.MULT)
                        compiler.addOperator((None if localctx._MULT is None else localctx._MULT.text))
                        pass
                    elif token in [patitoParser.DIV]:
                        self.state = 215
                        localctx._DIV = self.match(patitoParser.DIV)
                        compiler.addOperator((None if localctx._DIV is None else localctx._DIV.text))
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 219
                    self.term()
                    compiler.topIsMultOrDiv() 
                self.state = 226
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
        self.enterRule(localctx, 30, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [patitoParser.CTE_BOOL, patitoParser.CTE_FLOAT, patitoParser.CTE_INT, patitoParser.CTE_CHAR, patitoParser.CTE_STRING]:
                self.state = 227
                localctx._constant = self.constant()
                compiler.addOperand((None if localctx._constant is None else self._input.getText(localctx._constant.start,localctx._constant.stop)))
                pass
            elif token in [patitoParser.LEFT_PARENTHESIS]:
                self.state = 230
                self.match(patitoParser.LEFT_PARENTHESIS)
                compiler.addParenthesis()
                self.state = 232
                self.mexp()
                self.state = 233
                self.match(patitoParser.RIGHT_PARENTHESIS)
                compiler.popParenthesis()
                pass
            elif token in [patitoParser.ID]:
                self.state = 236
                localctx._ID = self.match(patitoParser.ID)
                compiler.addOperandAndType((None if localctx._ID is None else localctx._ID.text))
                self.state = 266
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    pass

                elif la_ == 2:
                    self.state = 239
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.DETERMINANT) | (1 << patitoParser.TRANSPOSE) | (1 << patitoParser.INVERSE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass

                elif la_ == 3:
                    self.state = 240
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 241
                    self.mexp()
                    self.state = 242
                    self.match(patitoParser.RIGHT_BRACKET)
                    pass

                elif la_ == 4:
                    self.state = 244
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 245
                    self.mexp()
                    self.state = 246
                    self.match(patitoParser.RIGHT_BRACKET)
                    self.state = 247
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 248
                    self.mexp()
                    self.state = 249
                    self.match(patitoParser.RIGHT_BRACKET)
                    pass

                elif la_ == 5:
                    self.state = 251
                    self.match(patitoParser.LEFT_PARENTHESIS)
                    compiler.addParenthesis()
                    self.state = 262
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.RIGHT_PARENTHESIS]:
                        pass
                    elif token in [patitoParser.LEFT_PARENTHESIS, patitoParser.CTE_BOOL, patitoParser.CTE_FLOAT, patitoParser.CTE_INT, patitoParser.CTE_CHAR, patitoParser.CTE_STRING, patitoParser.ID]:
                        self.state = 254
                        self.mexp()
                        self.state = 259
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==patitoParser.COMMA:
                            self.state = 255
                            self.match(patitoParser.COMMA)
                            self.state = 256
                            self.mexp()
                            self.state = 261
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 264
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
        self.enterRule(localctx, 32, self.RULE_statute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.RETURN) | (1 << patitoParser.INPUT) | (1 << patitoParser.PRINT) | (1 << patitoParser.IF) | (1 << patitoParser.WHILE) | (1 << patitoParser.FROM) | (1 << patitoParser.ID))) != 0):
                self.state = 278
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 270
                    self.assignation()
                    pass

                elif la_ == 2:
                    self.state = 271
                    self.voidcall()
                    pass

                elif la_ == 3:
                    self.state = 272
                    self.returncall()
                    pass

                elif la_ == 4:
                    self.state = 273
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 274
                    self.write()
                    pass

                elif la_ == 6:
                    self.state = 275
                    self.conditional()
                    pass

                elif la_ == 7:
                    self.state = 276
                    self.whileloop()
                    pass

                elif la_ == 8:
                    self.state = 277
                    self.fromloop()
                    pass


                self.state = 282
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

        def ID(self):
            return self.getToken(patitoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(patitoParser.ASSIGN, 0)

        def hexp(self):
            return self.getTypedRuleContext(patitoParser.HexpContext,0)


        def SEMICOLON(self):
            return self.getToken(patitoParser.SEMICOLON, 0)

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
            return patitoParser.RULE_assignation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignation" ):
                listener.enterAssignation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignation" ):
                listener.exitAssignation(self)




    def assignation(self):

        localctx = patitoParser.AssignationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assignation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            localctx._ID = self.match(patitoParser.ID)
            compiler.addOperandAndType((None if localctx._ID is None else localctx._ID.text))
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                self.state = 286
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 287
                self.mexp()
                self.state = 288
                self.match(patitoParser.RIGHT_BRACKET)
                pass

            elif la_ == 3:
                self.state = 290
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 291
                self.mexp()
                self.state = 292
                self.match(patitoParser.RIGHT_BRACKET)
                self.state = 293
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 294
                self.mexp()
                self.state = 295
                self.match(patitoParser.RIGHT_BRACKET)
                pass


            self.state = 299
            localctx._ASSIGN = self.match(patitoParser.ASSIGN)
            compiler.addOperator((None if localctx._ASSIGN is None else localctx._ASSIGN.text))
            self.state = 301
            self.hexp()
            self.state = 302
            self.match(patitoParser.SEMICOLON)
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
        self.enterRule(localctx, 36, self.RULE_voidcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(patitoParser.ID)
            self.state = 305
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [patitoParser.RIGHT_PARENTHESIS]:
                pass
            elif token in [patitoParser.LEFT_PARENTHESIS, patitoParser.CTE_BOOL, patitoParser.CTE_FLOAT, patitoParser.CTE_INT, patitoParser.CTE_CHAR, patitoParser.CTE_STRING, patitoParser.ID]:
                self.state = 307
                self.mexp()
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==patitoParser.COMMA:
                    self.state = 308
                    self.match(patitoParser.COMMA)
                    self.state = 309
                    self.mexp()
                    self.state = 314
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 317
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 318
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
        self.enterRule(localctx, 38, self.RULE_returncall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(patitoParser.RETURN)
            self.state = 321
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 322
            self.mexp()
            self.state = 323
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 324
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

        def ID(self):
            return self.getToken(patitoParser.ID, 0)

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
        self.enterRule(localctx, 40, self.RULE_indexvariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(patitoParser.ID)
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                self.state = 328
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 329
                self.mexp()
                self.state = 330
                self.match(patitoParser.RIGHT_BRACKET)
                pass

            elif la_ == 3:
                self.state = 332
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 333
                self.mexp()
                self.state = 334
                self.match(patitoParser.RIGHT_BRACKET)
                self.state = 335
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 336
                self.mexp()
                self.state = 337
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

        def INPUT(self):
            return self.getToken(patitoParser.INPUT, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(patitoParser.LEFT_PARENTHESIS, 0)

        def indexvariable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.IndexvariableContext)
            else:
                return self.getTypedRuleContext(patitoParser.IndexvariableContext,i)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(patitoParser.RIGHT_PARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(patitoParser.SEMICOLON, 0)

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
        self.enterRule(localctx, 42, self.RULE_read)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(patitoParser.INPUT)
            self.state = 342
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 343
            self.indexvariable()
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 344
                self.match(patitoParser.COMMA)
                self.state = 345
                self.indexvariable()
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 351
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 352
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

        def hexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.HexpContext)
            else:
                return self.getTypedRuleContext(patitoParser.HexpContext,i)


        def CTE_STRING(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.CTE_STRING)
            else:
                return self.getToken(patitoParser.CTE_STRING, i)

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
        self.enterRule(localctx, 44, self.RULE_write)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(patitoParser.PRINT)
            self.state = 355
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 356
                self.hexp()
                pass

            elif la_ == 2:
                self.state = 357
                self.match(patitoParser.CTE_STRING)
                pass


            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 360
                self.match(patitoParser.COMMA)
                self.state = 363
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 361
                    self.hexp()
                    pass

                elif la_ == 2:
                    self.state = 362
                    self.match(patitoParser.CTE_STRING)
                    pass


                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 370
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 371
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
        self.enterRule(localctx, 46, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(patitoParser.IF)
            self.state = 374
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 375
            self.mexp()
            self.state = 376
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 377
            self.match(patitoParser.THEN)
            self.state = 378
            self.match(patitoParser.LEFT_CURLY)
            self.state = 379
            self.statute()
            self.state = 380
            self.match(patitoParser.RIGHT_CURLY)
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.ELSE:
                self.state = 381
                self.match(patitoParser.ELSE)
                self.state = 382
                self.match(patitoParser.LEFT_CURLY)
                self.state = 383
                self.statute()
                self.state = 384
                self.match(patitoParser.RIGHT_CURLY)


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
        self.enterRule(localctx, 48, self.RULE_whileloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(patitoParser.WHILE)
            self.state = 389
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 390
            self.mexp()
            self.state = 391
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 392
            self.match(patitoParser.DO)
            self.state = 393
            self.match(patitoParser.LEFT_CURLY)
            self.state = 394
            self.statute()
            self.state = 395
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

        def indexvariable(self):
            return self.getTypedRuleContext(patitoParser.IndexvariableContext,0)


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
        self.enterRule(localctx, 50, self.RULE_fromloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(patitoParser.FROM)
            self.state = 398
            self.indexvariable()
            self.state = 399
            self.match(patitoParser.ASSIGN)
            self.state = 400
            self.mexp()
            self.state = 401
            self.match(patitoParser.TO)
            self.state = 402
            self.mexp()
            self.state = 403
            self.match(patitoParser.DO)
            self.state = 404
            self.match(patitoParser.LEFT_CURLY)
            self.state = 405
            self.statute()
            self.state = 406
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
        self.enterRule(localctx, 52, self.RULE_mainfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(patitoParser.MAIN)
            compiler.currentFunction=Function("main", "void", {}, {})
            self.state = 410
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 411
            self.match(patitoParser.RIGHT_PARENTHESIS)
            compiler._add_function(compiler.currentFunction)
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





