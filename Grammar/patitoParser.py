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
        buf.write("\u01df\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2<\n\2\3")
        buf.write("\2\3\2\3\3\3\3\6\3B\n\3\r\3\16\3C\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4U\n\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4e\n\4\7\4g\n\4\f\4\16\4j\13\4\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0087\n\6\3\7\6\7")
        buf.write("\u008a\n\7\r\7\16\7\u008b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\5\b\u0095\n\b\3\b\3\b\5\b\u0099\n\b\3\b\3\b\3\b\5\b\u009e")
        buf.write("\n\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\7\n\u00ad\n\n\f\n\16\n\u00b0\13\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\5\13\u00b8\n\13\3\13\3\13\3\13\7\13\u00bd")
        buf.write("\n\13\f\13\16\13\u00c0\13\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00d0\n\f\3\f\3\f\3")
        buf.write("\f\5\f\u00d5\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00dd\n\r")
        buf.write("\3\r\3\r\3\r\7\r\u00e2\n\r\f\r\16\r\u00e5\13\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\5\16\u00ed\n\16\3\16\3\16\3\16")
        buf.write("\7\16\u00f2\n\16\f\16\16\16\u00f5\13\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u0107\n\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u0117")
        buf.write("\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\7\17\u0125\n\17\f\17\16\17\u0128\13\17\5\17")
        buf.write("\u012a\n\17\3\17\3\17\3\17\3\17\3\17\5\17\u0131\n\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u013b\n\20")
        buf.write("\f\20\16\20\u013e\13\20\3\21\3\21\3\21\5\21\u0143\n\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\5\21\u014a\n\21\3\21\3\21\7")
        buf.write("\21\u014e\n\21\f\21\16\21\u0151\13\21\3\21\3\21\3\21\3")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u015e\n\22")
        buf.write("\f\22\16\22\u0161\13\22\5\22\u0163\n\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u017a\n\24\3")
        buf.write("\25\3\25\3\25\3\25\5\25\u0180\n\25\3\25\3\25\3\25\3\25")
        buf.write("\5\25\u0186\n\25\3\25\7\25\u0189\n\25\f\25\16\25\u018c")
        buf.write("\13\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\7\26\u019a\n\26\f\26\16\26\u019d\13\26\3")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u01b1\n\27\3")
        buf.write("\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\5\31\u01c5\n\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\2\2\33\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\2\4\3\2-\61\4\2-\61\67\67\2\u0201")
        buf.write("\2\64\3\2\2\2\4?\3\2\2\2\6E\3\2\2\2\bm\3\2\2\2\n\u0086")
        buf.write("\3\2\2\2\f\u0089\3\2\2\2\16\u008d\3\2\2\2\20\u00a2\3\2")
        buf.write("\2\2\22\u00a4\3\2\2\2\24\u00b1\3\2\2\2\26\u00c1\3\2\2")
        buf.write("\2\30\u00d6\3\2\2\2\32\u00e6\3\2\2\2\34\u0130\3\2\2\2")
        buf.write("\36\u013c\3\2\2\2 \u013f\3\2\2\2\"\u0156\3\2\2\2$\u0167")
        buf.write("\3\2\2\2&\u0179\3\2\2\2(\u017b\3\2\2\2*\u0190\3\2\2\2")
        buf.write(",\u01a1\3\2\2\2.\u01b4\3\2\2\2\60\u01c0\3\2\2\2\62\u01d4")
        buf.write("\3\2\2\2\64\65\7\37\2\2\65\66\78\2\2\66\67\b\2\1\2\67")
        buf.write("8\7\36\2\289\5\4\3\29;\b\2\1\2:<\5\f\7\2;:\3\2\2\2;<\3")
        buf.write("\2\2\2<=\3\2\2\2=>\5\62\32\2>\3\3\2\2\2?A\7,\2\2@B\5\6")
        buf.write("\4\2A@\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2D\5\3\2\2")
        buf.write("\2EF\5\b\5\2FG\7\35\2\2GH\78\2\2HT\b\4\1\2IJ\7\25\2\2")
        buf.write("JK\7\64\2\2KL\7\26\2\2LU\b\4\1\2MN\7\25\2\2NO\7\64\2\2")
        buf.write("OP\7\26\2\2PQ\7\25\2\2QR\7\64\2\2RS\7\26\2\2SU\b\4\1\2")
        buf.write("TI\3\2\2\2TM\3\2\2\2TU\3\2\2\2Uh\3\2\2\2VW\7\34\2\2WX")
        buf.write("\78\2\2Xd\b\4\1\2YZ\7\25\2\2Z[\7\64\2\2[\\\7\26\2\2\\")
        buf.write("e\b\4\1\2]^\7\25\2\2^_\7\64\2\2_`\7\26\2\2`a\7\25\2\2")
        buf.write("ab\7\64\2\2bc\7\26\2\2ce\b\4\1\2dY\3\2\2\2d]\3\2\2\2d")
        buf.write("e\3\2\2\2eg\3\2\2\2fV\3\2\2\2gj\3\2\2\2hf\3\2\2\2hi\3")
        buf.write("\2\2\2ik\3\2\2\2jh\3\2\2\2kl\7\36\2\2l\7\3\2\2\2mn\t\2")
        buf.write("\2\2n\t\3\2\2\2op\7\62\2\2pq\b\6\1\2q\u0087\b\6\1\2rs")
        buf.write("\7\20\2\2st\7\63\2\2tu\b\6\1\2u\u0087\b\6\1\2vw\7\63\2")
        buf.write("\2wx\b\6\1\2x\u0087\b\6\1\2yz\7\20\2\2z{\7\64\2\2{|\b")
        buf.write("\6\1\2|\u0087\b\6\1\2}~\7\64\2\2~\177\b\6\1\2\177\u0087")
        buf.write("\b\6\1\2\u0080\u0081\7\65\2\2\u0081\u0082\b\6\1\2\u0082")
        buf.write("\u0087\b\6\1\2\u0083\u0084\7\66\2\2\u0084\u0085\b\6\1")
        buf.write("\2\u0085\u0087\b\6\1\2\u0086o\3\2\2\2\u0086r\3\2\2\2\u0086")
        buf.write("v\3\2\2\2\u0086y\3\2\2\2\u0086}\3\2\2\2\u0086\u0080\3")
        buf.write("\2\2\2\u0086\u0083\3\2\2\2\u0087\13\3\2\2\2\u0088\u008a")
        buf.write("\5\16\b\2\u0089\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b")
        buf.write("\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\r\3\2\2\2\u008d")
        buf.write("\u008e\7!\2\2\u008e\u008f\5\20\t\2\u008f\u0090\78\2\2")
        buf.write("\u0090\u0091\b\b\1\2\u0091\u0092\b\b\1\2\u0092\u0094\7")
        buf.write("\23\2\2\u0093\u0095\5\22\n\2\u0094\u0093\3\2\2\2\u0094")
        buf.write("\u0095\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098\7\24\2")
        buf.write("\2\u0097\u0099\5\4\3\2\u0098\u0097\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\b\b\1\2\u009b")
        buf.write("\u009d\7\27\2\2\u009c\u009e\5\36\20\2\u009d\u009c\3\2")
        buf.write("\2\2\u009d\u009e\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0")
        buf.write("\7\30\2\2\u00a0\u00a1\b\b\1\2\u00a1\17\3\2\2\2\u00a2\u00a3")
        buf.write("\t\3\2\2\u00a3\21\3\2\2\2\u00a4\u00a5\5\b\5\2\u00a5\u00a6")
        buf.write("\78\2\2\u00a6\u00ae\b\n\1\2\u00a7\u00a8\7\34\2\2\u00a8")
        buf.write("\u00a9\5\b\5\2\u00a9\u00aa\78\2\2\u00aa\u00ab\b\n\1\2")
        buf.write("\u00ab\u00ad\3\2\2\2\u00ac\u00a7\3\2\2\2\u00ad\u00b0\3")
        buf.write("\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\23")
        buf.write("\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b2\5\26\f\2\u00b2")
        buf.write("\u00be\b\13\1\2\u00b3\u00b4\7\r\2\2\u00b4\u00b8\b\13\1")
        buf.write("\2\u00b5\u00b6\7\16\2\2\u00b6\u00b8\b\13\1\2\u00b7\u00b3")
        buf.write("\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9")
        buf.write("\u00ba\5\24\13\2\u00ba\u00bb\b\13\1\2\u00bb\u00bd\3\2")
        buf.write("\2\2\u00bc\u00b7\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc")
        buf.write("\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\25\3\2\2\2\u00c0\u00be")
        buf.write("\3\2\2\2\u00c1\u00c2\5\30\r\2\u00c2\u00d4\b\f\1\2\u00c3")
        buf.write("\u00c4\7\7\2\2\u00c4\u00d0\b\f\1\2\u00c5\u00c6\7\6\2\2")
        buf.write("\u00c6\u00d0\b\f\1\2\u00c7\u00c8\7\t\2\2\u00c8\u00d0\b")
        buf.write("\f\1\2\u00c9\u00ca\7\b\2\2\u00ca\u00d0\b\f\1\2\u00cb\u00cc")
        buf.write("\7\13\2\2\u00cc\u00d0\b\f\1\2\u00cd\u00ce\7\n\2\2\u00ce")
        buf.write("\u00d0\b\f\1\2\u00cf\u00c3\3\2\2\2\u00cf\u00c5\3\2\2\2")
        buf.write("\u00cf\u00c7\3\2\2\2\u00cf\u00c9\3\2\2\2\u00cf\u00cb\3")
        buf.write("\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2")
        buf.write("\5\26\f\2\u00d2\u00d3\b\f\1\2\u00d3\u00d5\3\2\2\2\u00d4")
        buf.write("\u00cf\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\27\3\2\2\2\u00d6")
        buf.write("\u00d7\5\32\16\2\u00d7\u00e3\b\r\1\2\u00d8\u00d9\7\17")
        buf.write("\2\2\u00d9\u00dd\b\r\1\2\u00da\u00db\7\20\2\2\u00db\u00dd")
        buf.write("\b\r\1\2\u00dc\u00d8\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd")
        buf.write("\u00de\3\2\2\2\u00de\u00df\5\30\r\2\u00df\u00e0\b\r\1")
        buf.write("\2\u00e0\u00e2\3\2\2\2\u00e1\u00dc\3\2\2\2\u00e2\u00e5")
        buf.write("\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4")
        buf.write("\31\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6\u00e7\5\34\17\2")
        buf.write("\u00e7\u00f3\b\16\1\2\u00e8\u00e9\7\21\2\2\u00e9\u00ed")
        buf.write("\b\16\1\2\u00ea\u00eb\7\22\2\2\u00eb\u00ed\b\16\1\2\u00ec")
        buf.write("\u00e8\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee\u00ef\5\32\16\2\u00ef\u00f0\b\16\1\2\u00f0\u00f2")
        buf.write("\3\2\2\2\u00f1\u00ec\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\33\3\2\2\2\u00f5")
        buf.write("\u00f3\3\2\2\2\u00f6\u0131\5\n\6\2\u00f7\u00f8\7\23\2")
        buf.write("\2\u00f8\u00f9\b\17\1\2\u00f9\u00fa\5\24\13\2\u00fa\u00fb")
        buf.write("\7\24\2\2\u00fb\u00fc\b\17\1\2\u00fc\u0131\3\2\2\2\u00fd")
        buf.write("\u00fe\78\2\2\u00fe\u0116\b\17\1\2\u00ff\u0117\3\2\2\2")
        buf.write("\u0100\u0101\7\31\2\2\u0101\u0107\b\17\1\2\u0102\u0103")
        buf.write("\7\32\2\2\u0103\u0107\b\17\1\2\u0104\u0105\7\33\2\2\u0105")
        buf.write("\u0107\b\17\1\2\u0106\u0100\3\2\2\2\u0106\u0102\3\2\2")
        buf.write("\2\u0106\u0104\3\2\2\2\u0107\u0117\3\2\2\2\u0108\u0109")
        buf.write("\7\25\2\2\u0109\u010a\5\24\13\2\u010a\u010b\b\17\1\2\u010b")
        buf.write("\u010c\7\26\2\2\u010c\u0117\3\2\2\2\u010d\u010e\7\25\2")
        buf.write("\2\u010e\u010f\5\24\13\2\u010f\u0110\b\17\1\2\u0110\u0111")
        buf.write("\7\26\2\2\u0111\u0112\7\25\2\2\u0112\u0113\5\24\13\2\u0113")
        buf.write("\u0114\b\17\1\2\u0114\u0115\7\26\2\2\u0115\u0117\3\2\2")
        buf.write("\2\u0116\u00ff\3\2\2\2\u0116\u0106\3\2\2\2\u0116\u0108")
        buf.write("\3\2\2\2\u0116\u010d\3\2\2\2\u0117\u0131\3\2\2\2\u0118")
        buf.write("\u0119\78\2\2\u0119\u011a\b\17\1\2\u011a\u011b\7\23\2")
        buf.write("\2\u011b\u011c\b\17\1\2\u011c\u0129\b\17\1\2\u011d\u012a")
        buf.write("\3\2\2\2\u011e\u011f\5\24\13\2\u011f\u0126\b\17\1\2\u0120")
        buf.write("\u0121\7\34\2\2\u0121\u0122\5\24\13\2\u0122\u0123\b\17")
        buf.write("\1\2\u0123\u0125\3\2\2\2\u0124\u0120\3\2\2\2\u0125\u0128")
        buf.write("\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127")
        buf.write("\u012a\3\2\2\2\u0128\u0126\3\2\2\2\u0129\u011d\3\2\2\2")
        buf.write("\u0129\u011e\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\b")
        buf.write("\17\1\2\u012c\u012d\b\17\1\2\u012d\u012e\b\17\1\2\u012e")
        buf.write("\u012f\7\24\2\2\u012f\u0131\b\17\1\2\u0130\u00f6\3\2\2")
        buf.write("\2\u0130\u00f7\3\2\2\2\u0130\u00fd\3\2\2\2\u0130\u0118")
        buf.write("\3\2\2\2\u0131\35\3\2\2\2\u0132\u013b\5 \21\2\u0133\u013b")
        buf.write("\5\"\22\2\u0134\u013b\5$\23\2\u0135\u013b\5(\25\2\u0136")
        buf.write("\u013b\5*\26\2\u0137\u013b\5,\27\2\u0138\u013b\5.\30\2")
        buf.write("\u0139\u013b\5\60\31\2\u013a\u0132\3\2\2\2\u013a\u0133")
        buf.write("\3\2\2\2\u013a\u0134\3\2\2\2\u013a\u0135\3\2\2\2\u013a")
        buf.write("\u0136\3\2\2\2\u013a\u0137\3\2\2\2\u013a\u0138\3\2\2\2")
        buf.write("\u013a\u0139\3\2\2\2\u013b\u013e\3\2\2\2\u013c\u013a\3")
        buf.write("\2\2\2\u013c\u013d\3\2\2\2\u013d\37\3\2\2\2\u013e\u013c")
        buf.write("\3\2\2\2\u013f\u0140\78\2\2\u0140\u0142\b\21\1\2\u0141")
        buf.write("\u0143\5&\24\2\u0142\u0141\3\2\2\2\u0142\u0143\3\2\2\2")
        buf.write("\u0143\u0144\3\2\2\2\u0144\u0145\7\f\2\2\u0145\u014f\b")
        buf.write("\21\1\2\u0146\u0147\78\2\2\u0147\u0149\b\21\1\2\u0148")
        buf.write("\u014a\5&\24\2\u0149\u0148\3\2\2\2\u0149\u014a\3\2\2\2")
        buf.write("\u014a\u014b\3\2\2\2\u014b\u014c\7\f\2\2\u014c\u014e\b")
        buf.write("\21\1\2\u014d\u0146\3\2\2\2\u014e\u0151\3\2\2\2\u014f")
        buf.write("\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0152\3\2\2\2")
        buf.write("\u0151\u014f\3\2\2\2\u0152\u0153\5\24\13\2\u0153\u0154")
        buf.write("\7\36\2\2\u0154\u0155\b\21\1\2\u0155!\3\2\2\2\u0156\u0157")
        buf.write("\78\2\2\u0157\u0158\b\22\1\2\u0158\u0162\7\23\2\2\u0159")
        buf.write("\u0163\3\2\2\2\u015a\u015f\5\24\13\2\u015b\u015c\7\34")
        buf.write("\2\2\u015c\u015e\5\24\13\2\u015d\u015b\3\2\2\2\u015e\u0161")
        buf.write("\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160")
        buf.write("\u0163\3\2\2\2\u0161\u015f\3\2\2\2\u0162\u0159\3\2\2\2")
        buf.write("\u0162\u015a\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\7")
        buf.write("\24\2\2\u0165\u0166\7\36\2\2\u0166#\3\2\2\2\u0167\u0168")
        buf.write("\7\"\2\2\u0168\u0169\7\23\2\2\u0169\u016a\5\24\13\2\u016a")
        buf.write("\u016b\7\24\2\2\u016b\u016c\7\36\2\2\u016c\u016d\b\23")
        buf.write("\1\2\u016d%\3\2\2\2\u016e\u016f\7\25\2\2\u016f\u0170\5")
        buf.write("\24\13\2\u0170\u0171\7\26\2\2\u0171\u017a\3\2\2\2\u0172")
        buf.write("\u0173\7\25\2\2\u0173\u0174\5\24\13\2\u0174\u0175\7\26")
        buf.write("\2\2\u0175\u0176\7\25\2\2\u0176\u0177\5\24\13\2\u0177")
        buf.write("\u0178\7\26\2\2\u0178\u017a\3\2\2\2\u0179\u016e\3\2\2")
        buf.write("\2\u0179\u0172\3\2\2\2\u017a\'\3\2\2\2\u017b\u017c\7#")
        buf.write("\2\2\u017c\u017d\7\23\2\2\u017d\u017f\78\2\2\u017e\u0180")
        buf.write("\5&\24\2\u017f\u017e\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("\u0181\3\2\2\2\u0181\u018a\b\25\1\2\u0182\u0183\7\34\2")
        buf.write("\2\u0183\u0185\78\2\2\u0184\u0186\5&\24\2\u0185\u0184")
        buf.write("\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0187\3\2\2\2\u0187")
        buf.write("\u0189\b\25\1\2\u0188\u0182\3\2\2\2\u0189\u018c\3\2\2")
        buf.write("\2\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018d")
        buf.write("\3\2\2\2\u018c\u018a\3\2\2\2\u018d\u018e\7\24\2\2\u018e")
        buf.write("\u018f\7\36\2\2\u018f)\3\2\2\2\u0190\u0191\7$\2\2\u0191")
        buf.write("\u0192\7\23\2\2\u0192\u0193\5\24\13\2\u0193\u0194\b\26")
        buf.write("\1\2\u0194\u019b\3\2\2\2\u0195\u0196\7\34\2\2\u0196\u0197")
        buf.write("\5\24\13\2\u0197\u0198\b\26\1\2\u0198\u019a\3\2\2\2\u0199")
        buf.write("\u0195\3\2\2\2\u019a\u019d\3\2\2\2\u019b\u0199\3\2\2\2")
        buf.write("\u019b\u019c\3\2\2\2\u019c\u019e\3\2\2\2\u019d\u019b\3")
        buf.write("\2\2\2\u019e\u019f\7\24\2\2\u019f\u01a0\7\36\2\2\u01a0")
        buf.write("+\3\2\2\2\u01a1\u01a2\7%\2\2\u01a2\u01a3\7\23\2\2\u01a3")
        buf.write("\u01a4\5\24\13\2\u01a4\u01a5\7\24\2\2\u01a5\u01a6\b\27")
        buf.write("\1\2\u01a6\u01a7\7&\2\2\u01a7\u01a8\7\27\2\2\u01a8\u01a9")
        buf.write("\5\36\20\2\u01a9\u01b0\7\30\2\2\u01aa\u01ab\7\'\2\2\u01ab")
        buf.write("\u01ac\b\27\1\2\u01ac\u01ad\7\27\2\2\u01ad\u01ae\5\36")
        buf.write("\20\2\u01ae\u01af\7\30\2\2\u01af\u01b1\3\2\2\2\u01b0\u01aa")
        buf.write("\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2")
        buf.write("\u01b3\b\27\1\2\u01b3-\3\2\2\2\u01b4\u01b5\7(\2\2\u01b5")
        buf.write("\u01b6\7\23\2\2\u01b6\u01b7\b\30\1\2\u01b7\u01b8\5\24")
        buf.write("\13\2\u01b8\u01b9\7\24\2\2\u01b9\u01ba\b\30\1\2\u01ba")
        buf.write("\u01bb\7)\2\2\u01bb\u01bc\7\27\2\2\u01bc\u01bd\5\36\20")
        buf.write("\2\u01bd\u01be\b\30\1\2\u01be\u01bf\7\30\2\2\u01bf/\3")
        buf.write("\2\2\2\u01c0\u01c1\7*\2\2\u01c1\u01c2\78\2\2\u01c2\u01c4")
        buf.write("\b\31\1\2\u01c3\u01c5\5&\24\2\u01c4\u01c3\3\2\2\2\u01c4")
        buf.write("\u01c5\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7\7\f\2\2")
        buf.write("\u01c7\u01c8\b\31\1\2\u01c8\u01c9\5\24\13\2\u01c9\u01ca")
        buf.write("\b\31\1\2\u01ca\u01cb\7+\2\2\u01cb\u01cc\b\31\1\2\u01cc")
        buf.write("\u01cd\5\24\13\2\u01cd\u01ce\b\31\1\2\u01ce\u01cf\7)\2")
        buf.write("\2\u01cf\u01d0\7\27\2\2\u01d0\u01d1\5\36\20\2\u01d1\u01d2")
        buf.write("\7\30\2\2\u01d2\u01d3\b\31\1\2\u01d3\61\3\2\2\2\u01d4")
        buf.write("\u01d5\7 \2\2\u01d5\u01d6\b\32\1\2\u01d6\u01d7\7\23\2")
        buf.write("\2\u01d7\u01d8\7\24\2\2\u01d8\u01d9\b\32\1\2\u01d9\u01da")
        buf.write("\7\27\2\2\u01da\u01db\b\32\1\2\u01db\u01dc\5\36\20\2\u01dc")
        buf.write("\u01dd\7\30\2\2\u01dd\63\3\2\2\2(;CTdh\u0086\u008b\u0094")
        buf.write("\u0098\u009d\u00ae\u00b7\u00be\u00cf\u00d4\u00dc\u00e3")
        buf.write("\u00ec\u00f3\u0106\u0116\u0126\u0129\u0130\u013a\u013c")
        buf.write("\u0142\u0149\u014f\u015f\u0162\u0179\u017f\u0185\u018a")
        buf.write("\u019b\u01b0\u01c4")
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

        def declarevars(self):
            return self.getTypedRuleContext(patitoParser.DeclarevarsContext,0)


        def mainfunc(self):
            return self.getTypedRuleContext(patitoParser.MainfuncContext,0)


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
            self.state = 54
            self.declarevars()
            self.compiler.goto_main_quad()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.FUNCTION:
                self.state = 56
                self.functions()


            self.state = 59
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
            self.state = 61
            self.match(patitoParser.VAR)
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self.variables()
                self.state = 65 
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
            self.state = 67
            localctx._vartypes = self.vartypes()
            self.state = 68
            self.match(patitoParser.COLON)
            self.state = 69
            localctx._ID = self.match(patitoParser.ID)
            self.compiler.update_vars_table((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 71
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 72
                localctx._CTE_INT = self.match(patitoParser.CTE_INT)
                self.state = 73
                self.match(patitoParser.RIGHT_BRACKET)
                self.compiler.update_array_variable((None if localctx._ID is None else localctx._ID.text), (None if localctx._CTE_INT is None else localctx._CTE_INT.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))

            elif la_ == 2:
                self.state = 75
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 76
                localctx.first_index = self.match(patitoParser.CTE_INT)
                self.state = 77
                self.match(patitoParser.RIGHT_BRACKET)
                self.state = 78
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 79
                localctx.second_index = self.match(patitoParser.CTE_INT)
                self.state = 80
                self.match(patitoParser.RIGHT_BRACKET)
                self.compiler.update_matrix_variable((None if localctx._ID is None else localctx._ID.text), (None if localctx.first_index is None else localctx.first_index.text), (None if localctx.second_index is None else localctx.second_index.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))


            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 84
                self.match(patitoParser.COMMA)
                self.state = 85
                localctx._ID = self.match(patitoParser.ID)
                self.compiler.update_vars_table((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
                self.state = 98
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 87
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 88
                    localctx._CTE_INT = self.match(patitoParser.CTE_INT)
                    self.state = 89
                    self.match(patitoParser.RIGHT_BRACKET)
                    self.compiler.update_array_variable((None if localctx._ID is None else localctx._ID.text), (None if localctx._CTE_INT is None else localctx._CTE_INT.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))

                elif la_ == 2:
                    self.state = 91
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 92
                    localctx.first_index = self.match(patitoParser.CTE_INT)
                    self.state = 93
                    self.match(patitoParser.RIGHT_BRACKET)
                    self.state = 94
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 95
                    localctx.second_index = self.match(patitoParser.CTE_INT)
                    self.state = 96
                    self.match(patitoParser.RIGHT_BRACKET)
                    self.compiler.update_matrix_variable((None if localctx._ID is None else localctx._ID.text), (None if localctx.first_index is None else localctx.first_index.text), (None if localctx.second_index is None else localctx.second_index.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))


                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
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
            self.state = 107
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
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 109
                localctx._CTE_BOOL = self.match(patitoParser.CTE_BOOL)
                self.compiler.addOperand((None if localctx._CTE_BOOL is None else localctx._CTE_BOOL.text))
                self.compiler.addConstantToTypeStackAndTable("bool")
                pass

            elif la_ == 2:
                self.state = 112
                self.match(patitoParser.SUB)
                self.state = 113
                localctx._CTE_FLOAT = self.match(patitoParser.CTE_FLOAT)
                self.compiler.addOperand("-" + (None if localctx._CTE_FLOAT is None else localctx._CTE_FLOAT.text))
                self.compiler.addConstantToTypeStackAndTable("float")
                pass

            elif la_ == 3:
                self.state = 116
                localctx._CTE_FLOAT = self.match(patitoParser.CTE_FLOAT)
                self.compiler.addOperand((None if localctx._CTE_FLOAT is None else localctx._CTE_FLOAT.text))
                self.compiler.addConstantToTypeStackAndTable("float")
                pass

            elif la_ == 4:
                self.state = 119
                self.match(patitoParser.SUB)
                self.state = 120
                localctx._CTE_INT = self.match(patitoParser.CTE_INT)
                self.compiler.addOperand("-" + (None if localctx._CTE_INT is None else localctx._CTE_INT.text))
                self.compiler.addConstantToTypeStackAndTable("int")
                pass

            elif la_ == 5:
                self.state = 123
                localctx._CTE_INT = self.match(patitoParser.CTE_INT)
                self.compiler.addOperand((None if localctx._CTE_INT is None else localctx._CTE_INT.text))
                self.compiler.addConstantToTypeStackAndTable("int")
                pass

            elif la_ == 6:
                self.state = 126
                localctx._CTE_CHAR = self.match(patitoParser.CTE_CHAR)
                self.compiler.addOperand((None if localctx._CTE_CHAR is None else localctx._CTE_CHAR.text))
                self.compiler.addConstantToTypeStackAndTable("char")
                pass

            elif la_ == 7:
                self.state = 129
                localctx._CTE_STRING = self.match(patitoParser.CTE_STRING)
                self.compiler.addOperand((None if localctx._CTE_STRING is None else localctx._CTE_STRING.text))
                self.compiler.addConstantToTypeStackAndTable("string")
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
            self.state = 135 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 134
                self.function()
                self.state = 137 
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
            self.state = 139
            self.match(patitoParser.FUNCTION)
            self.state = 140
            localctx._functiontype = self.functiontype()
            self.state = 141
            localctx._ID = self.match(patitoParser.ID)
            self.compiler.currentFunction=Function((None if localctx._ID is None else localctx._ID.text), (None if localctx._functiontype is None else self._input.getText(localctx._functiontype.start,localctx._functiontype.stop)), [], {})
            self.compiler.clear_local_memory()
            self.state = 144
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.BOOL) | (1 << patitoParser.INT) | (1 << patitoParser.FLOAT) | (1 << patitoParser.STRING) | (1 << patitoParser.CHAR))) != 0):
                self.state = 145
                self.parameters()


            self.state = 148
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.VAR:
                self.state = 149
                self.declarevars()


            self.compiler._add_function(self.compiler.currentFunction)
            self.state = 153
            self.match(patitoParser.LEFT_CURLY)
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 154
                self.statute()


            self.state = 157
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
            self.state = 160
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
            self.state = 162
            localctx._vartypes = self.vartypes()
            self.state = 163
            localctx._ID = self.match(patitoParser.ID)
            self.compiler.update_parameters((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 165
                self.match(patitoParser.COMMA)
                self.state = 166
                localctx._vartypes = self.vartypes()
                self.state = 167
                localctx._ID = self.match(patitoParser.ID)
                self.compiler.update_parameters((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
                self.state = 174
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
            self.state = 175
            self.sexp()
            self.compiler.topIsLogicOperator()
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 181
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.AND]:
                        self.state = 177
                        localctx._AND = self.match(patitoParser.AND)
                        self.compiler.addOperator((None if localctx._AND is None else localctx._AND.text))
                        pass
                    elif token in [patitoParser.OR]:
                        self.state = 179
                        localctx._OR = self.match(patitoParser.OR)
                        self.compiler.addOperator((None if localctx._OR is None else localctx._OR.text))
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 183
                    self.mexp()
                    self.compiler.topIsLogicOperator()
                self.state = 190
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
        self.enterRule(localctx, 20, self.RULE_sexp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.exp()
            self.compiler.topIsComparison()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.LESS) | (1 << patitoParser.GREATER) | (1 << patitoParser.LESS_EQUAL) | (1 << patitoParser.GREATER_EQUAL) | (1 << patitoParser.EQUAL) | (1 << patitoParser.NOT_EQUAL))) != 0):
                self.state = 205
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [patitoParser.GREATER]:
                    self.state = 193
                    localctx._GREATER = self.match(patitoParser.GREATER)
                    self.compiler.addOperator((None if localctx._GREATER is None else localctx._GREATER.text))
                    pass
                elif token in [patitoParser.LESS]:
                    self.state = 195
                    localctx._LESS = self.match(patitoParser.LESS)
                    self.compiler.addOperator((None if localctx._LESS is None else localctx._LESS.text))
                    pass
                elif token in [patitoParser.GREATER_EQUAL]:
                    self.state = 197
                    localctx._GREATER_EQUAL = self.match(patitoParser.GREATER_EQUAL)
                    self.compiler.addOperator((None if localctx._GREATER_EQUAL is None else localctx._GREATER_EQUAL.text))
                    pass
                elif token in [patitoParser.LESS_EQUAL]:
                    self.state = 199
                    localctx._LESS_EQUAL = self.match(patitoParser.LESS_EQUAL)
                    self.compiler.addOperator((None if localctx._LESS_EQUAL is None else localctx._LESS_EQUAL.text))
                    pass
                elif token in [patitoParser.NOT_EQUAL]:
                    self.state = 201
                    localctx._NOT_EQUAL = self.match(patitoParser.NOT_EQUAL)
                    self.compiler.addOperator((None if localctx._NOT_EQUAL is None else localctx._NOT_EQUAL.text))
                    pass
                elif token in [patitoParser.EQUAL]:
                    self.state = 203
                    localctx._EQUAL = self.match(patitoParser.EQUAL)
                    self.compiler.addOperator((None if localctx._EQUAL is None else localctx._EQUAL.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 207
                self.sexp()
                self.compiler.topIsComparison()


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
            self.state = 212
            self.term()
            self.compiler.topIsAddOrSub()
            self.state = 225
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 218
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.ADD]:
                        self.state = 214
                        localctx._ADD = self.match(patitoParser.ADD)
                        self.compiler.addOperator((None if localctx._ADD is None else localctx._ADD.text))
                        pass
                    elif token in [patitoParser.SUB]:
                        self.state = 216
                        localctx._SUB = self.match(patitoParser.SUB)
                        self.compiler.addOperator((None if localctx._SUB is None else localctx._SUB.text))
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 220
                    self.exp()
                    self.compiler.topIsAddOrSub()
                self.state = 227
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
        self.enterRule(localctx, 24, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.factor()
            self.compiler.topIsMultOrDiv()
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 234
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.MULT]:
                        self.state = 230
                        localctx._MULT = self.match(patitoParser.MULT)
                        self.compiler.addOperator((None if localctx._MULT is None else localctx._MULT.text))
                        pass
                    elif token in [patitoParser.DIV]:
                        self.state = 232
                        localctx._DIV = self.match(patitoParser.DIV)
                        self.compiler.addOperator((None if localctx._DIV is None else localctx._DIV.text))
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 236
                    self.term()
                    self.compiler.topIsMultOrDiv()
                self.state = 243
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
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 244
                self.constant()
                pass

            elif la_ == 2:
                self.state = 245
                self.match(patitoParser.LEFT_PARENTHESIS)
                self.compiler.addParenthesis()
                self.state = 247
                self.mexp()
                self.state = 248
                self.match(patitoParser.RIGHT_PARENTHESIS)
                self.compiler.popParenthesis()
                pass

            elif la_ == 3:
                self.state = 251
                localctx._ID = self.match(patitoParser.ID)
                self.compiler.addOperandAndType((None if localctx._ID is None else localctx._ID.text))
                self.state = 276
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    pass

                elif la_ == 2:
                    self.state = 260
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.DETERMINANT]:
                        self.state = 254
                        localctx._DETERMINANT = self.match(patitoParser.DETERMINANT)
                        self.compiler.generate_matrix_operation_quad((None if localctx._DETERMINANT is None else localctx._DETERMINANT.text))
                        pass
                    elif token in [patitoParser.TRANSPOSE]:
                        self.state = 256
                        localctx._TRANSPOSE = self.match(patitoParser.TRANSPOSE)
                        self.compiler.generate_matrix_operation_quad((None if localctx._TRANSPOSE is None else localctx._TRANSPOSE.text))
                        pass
                    elif token in [patitoParser.INVERSE]:
                        self.state = 258
                        localctx._INVERSE = self.match(patitoParser.INVERSE)
                        self.compiler.generate_matrix_operation_quad((None if localctx._INVERSE is None else localctx._INVERSE.text))
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 3:
                    self.state = 262
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 263
                    self.mexp()
                    self.compiler.verify_first_index((None if localctx._ID is None else localctx._ID.text))
                    self.state = 265
                    self.match(patitoParser.RIGHT_BRACKET)
                    pass

                elif la_ == 4:
                    self.state = 267
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 268
                    self.mexp()
                    self.compiler.verify_first_index((None if localctx._ID is None else localctx._ID.text))
                    self.state = 270
                    self.match(patitoParser.RIGHT_BRACKET)
                    self.state = 271
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 272
                    self.mexp()
                    self.compiler.verify_second_index((None if localctx._ID is None else localctx._ID.text))
                    self.state = 274
                    self.match(patitoParser.RIGHT_BRACKET)
                    pass


                pass

            elif la_ == 4:
                self.state = 278
                localctx._ID = self.match(patitoParser.ID)
                self.compiler.validate_function_expression((None if localctx._ID is None else localctx._ID.text))
                self.state = 280
                self.match(patitoParser.LEFT_PARENTHESIS)
                self.compiler.addParenthesis()
                currentCounter=0
                self.state = 295
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [patitoParser.RIGHT_PARENTHESIS]:
                    pass
                elif token in [patitoParser.SUB, patitoParser.LEFT_PARENTHESIS, patitoParser.CTE_BOOL, patitoParser.CTE_FLOAT, patitoParser.CTE_INT, patitoParser.CTE_CHAR, patitoParser.CTE_STRING, patitoParser.ID]:
                    self.state = 284
                    self.mexp()
                    currentCounter += 1
                    self.state = 292
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==patitoParser.COMMA:
                        self.state = 286
                        self.match(patitoParser.COMMA)
                        self.state = 287
                        self.mexp()
                        currentCounter += 1
                        self.state = 294
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                else:
                    raise NoViableAltException(self)

                self.compiler.validate_parameters((None if localctx._ID is None else localctx._ID.text), currentCounter)
                self.compiler.add_func_operand_and_type((None if localctx._ID is None else localctx._ID.text))
                self.compiler.goto_function_quad((None if localctx._ID is None else localctx._ID.text))
                self.state = 300
                self.match(patitoParser.RIGHT_PARENTHESIS)
                self.compiler.popParenthesis()
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
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.RETURN) | (1 << patitoParser.INPUT) | (1 << patitoParser.PRINT) | (1 << patitoParser.IF) | (1 << patitoParser.WHILE) | (1 << patitoParser.FROM) | (1 << patitoParser.ID))) != 0):
                self.state = 312
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 304
                    self.assignation()
                    pass

                elif la_ == 2:
                    self.state = 305
                    self.funccall()
                    pass

                elif la_ == 3:
                    self.state = 306
                    self.returncall()
                    pass

                elif la_ == 4:
                    self.state = 307
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 308
                    self.write()
                    pass

                elif la_ == 6:
                    self.state = 309
                    self.conditional()
                    pass

                elif la_ == 7:
                    self.state = 310
                    self.whileloop()
                    pass

                elif la_ == 8:
                    self.state = 311
                    self.fromloop()
                    pass


                self.state = 316
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
            self.state = 317
            localctx._ID = self.match(patitoParser.ID)
            self.compiler.addOperandAndType((None if localctx._ID is None else localctx._ID.text))
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.LEFT_BRACKET:
                self.state = 319
                self.indexvariable()


            self.state = 322
            localctx._ASSIGN = self.match(patitoParser.ASSIGN)
            self.compiler.addOperator((None if localctx._ASSIGN is None else localctx._ASSIGN.text))
            self.state = 333
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 324
                    localctx._ID = self.match(patitoParser.ID)
                    self.compiler.addOperandAndType((None if localctx._ID is None else localctx._ID.text))
                    self.state = 327
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==patitoParser.LEFT_BRACKET:
                        self.state = 326
                        self.indexvariable()


                    self.state = 329
                    localctx._ASSIGN = self.match(patitoParser.ASSIGN)
                    self.compiler.addOperator((None if localctx._ASSIGN is None else localctx._ASSIGN.text))
                self.state = 335
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

            self.state = 336
            self.mexp()
            self.state = 337
            self.match(patitoParser.SEMICOLON)
            self.compiler.generateAssignQuads()
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
            self.state = 340
            localctx._ID = self.match(patitoParser.ID)
            self.compiler.validate_void_function((None if localctx._ID is None else localctx._ID.text))
            self.state = 342
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 352
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [patitoParser.RIGHT_PARENTHESIS]:
                pass
            elif token in [patitoParser.SUB, patitoParser.LEFT_PARENTHESIS, patitoParser.CTE_BOOL, patitoParser.CTE_FLOAT, patitoParser.CTE_INT, patitoParser.CTE_CHAR, patitoParser.CTE_STRING, patitoParser.ID]:
                self.state = 344
                self.mexp()
                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==patitoParser.COMMA:
                    self.state = 345
                    self.match(patitoParser.COMMA)
                    self.state = 346
                    self.mexp()
                    self.state = 351
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 354
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 355
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
        self.enterRule(localctx, 34, self.RULE_returncall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(patitoParser.RETURN)
            self.state = 358
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 359
            self.mexp()
            self.state = 360
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 361
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
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 364
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 365
                self.mexp()
                self.state = 366
                self.match(patitoParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.state = 368
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 369
                self.mexp()
                self.state = 370
                self.match(patitoParser.RIGHT_BRACKET)
                self.state = 371
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 372
                self.mexp()
                self.state = 373
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
        self.enterRule(localctx, 38, self.RULE_read)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(patitoParser.INPUT)
            self.state = 378
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 379
            localctx.var_id = self.match(patitoParser.ID)
            self.state = 381
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.LEFT_BRACKET:
                self.state = 380
                self.indexvariable()


            self.compiler.generateReadQuad((None if localctx.var_id is None else localctx.var_id.text))
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 384
                self.match(patitoParser.COMMA)
                self.state = 385
                localctx.var_id2 = self.match(patitoParser.ID)
                self.state = 387
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==patitoParser.LEFT_BRACKET:
                    self.state = 386
                    self.indexvariable()


                self.compiler.generateReadQuad((None if localctx.var_id2 is None else localctx.var_id2.text))
                self.state = 394
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 395
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 396
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
            self.state = 398
            self.match(patitoParser.PRINT)
            self.state = 399
            self.match(patitoParser.LEFT_PARENTHESIS)

            self.state = 400
            self.mexp()
            self.compiler.generateWriteQuad()
            self.state = 409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 403
                self.match(patitoParser.COMMA)

                self.state = 404
                self.mexp()
                self.compiler.generateWriteQuad()
                self.state = 411
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 412
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 413
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
            self.state = 415
            self.match(patitoParser.IF)
            self.state = 416
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 417
            self.mexp()
            self.state = 418
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.compiler.generateIfQuad()
            self.state = 420
            self.match(patitoParser.THEN)
            self.state = 421
            self.match(patitoParser.LEFT_CURLY)
            self.state = 422
            self.statute()
            self.state = 423
            self.match(patitoParser.RIGHT_CURLY)
            self.state = 430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.ELSE:
                self.state = 424
                self.match(patitoParser.ELSE)
                self.compiler.generateGoToQuad()
                self.state = 426
                self.match(patitoParser.LEFT_CURLY)
                self.state = 427
                self.statute()
                self.state = 428
                self.match(patitoParser.RIGHT_CURLY)


            self.compiler.generateEndIfQuad()
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
            self.state = 434
            self.match(patitoParser.WHILE)
            self.state = 435
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.compiler.generateWhileBeforeCheck()
            self.state = 437
            self.mexp()
            self.state = 438
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.compiler.generateWhileAfterCheck()
            self.state = 440
            self.match(patitoParser.DO)
            self.state = 441
            self.match(patitoParser.LEFT_CURLY)
            self.state = 442
            self.statute()
            self.compiler.generateWhileEnd()
            self.state = 444
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
            self.state = 446
            self.match(patitoParser.FROM)
            self.state = 447
            localctx._ID = self.match(patitoParser.ID)
            self.compiler.addFromVarOperand((None if localctx._ID is None else localctx._ID.text))
            self.state = 450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.LEFT_BRACKET:
                self.state = 449
                self.indexvariable()


            self.state = 452
            localctx._ASSIGN = self.match(patitoParser.ASSIGN)
            self.compiler.addOperator((None if localctx._ASSIGN is None else localctx._ASSIGN.text))
            self.state = 454
            self.mexp()
            self.compiler.generateAssignQuads()
            self.state = 456
            self.match(patitoParser.TO)
            self.compiler.generateFromBeforeCheck()
            self.state = 458
            self.mexp()
            self.compiler.generateFromAfterCheck()
            self.state = 460
            self.match(patitoParser.DO)
            self.state = 461
            self.match(patitoParser.LEFT_CURLY)
            self.state = 462
            self.statute()
            self.state = 463
            self.match(patitoParser.RIGHT_CURLY)
            self.compiler.generateEndFromQuad()
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
            self.state = 466
            self.match(patitoParser.MAIN)
            self.compiler.currentFunction=Function("main", "void", [], {})
            self.state = 468
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 469
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.compiler._add_function(self.compiler.currentFunction)
            self.state = 471
            self.match(patitoParser.LEFT_CURLY)
            self.compiler.fill_goto_main_quad()
            self.state = 473
            self.statute()
            self.state = 474
            self.match(patitoParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





