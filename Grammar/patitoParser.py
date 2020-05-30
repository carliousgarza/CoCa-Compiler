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
        buf.write("\u01f5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\5\17\u011c\n\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u012a\n\17")
        buf.write("\f\17\16\17\u012d\13\17\5\17\u012f\n\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u0136\n\17\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\7\20\u0140\n\20\f\20\16\20\u0143\13\20\3")
        buf.write("\21\3\21\3\21\5\21\u0148\n\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\5\21\u014f\n\21\3\21\3\21\7\21\u0153\n\21\f\21\16\21")
        buf.write("\u0156\13\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u0168\n\22")
        buf.write("\f\22\16\22\u016b\13\22\5\22\u016d\n\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u018e\n\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\5\25\u0195\n\25\3\25\3\25\3\25\3\25")
        buf.write("\5\25\u019b\n\25\3\25\3\25\7\25\u019f\n\25\f\25\16\25")
        buf.write("\u01a2\13\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\7\26\u01b0\n\26\f\26\16\26\u01b3\13")
        buf.write("\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u01c7\n")
        buf.write("\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\5\31\u01db\n")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\2\2\33\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\2\4\3\2-\61\4\2-\61\67\67")
        buf.write("\2\u0217\2\64\3\2\2\2\4?\3\2\2\2\6E\3\2\2\2\bm\3\2\2\2")
        buf.write("\n\u0086\3\2\2\2\f\u0089\3\2\2\2\16\u008d\3\2\2\2\20\u00a2")
        buf.write("\3\2\2\2\22\u00a4\3\2\2\2\24\u00b1\3\2\2\2\26\u00c1\3")
        buf.write("\2\2\2\30\u00d6\3\2\2\2\32\u00e6\3\2\2\2\34\u0135\3\2")
        buf.write("\2\2\36\u0141\3\2\2\2 \u0144\3\2\2\2\"\u015b\3\2\2\2$")
        buf.write("\u0173\3\2\2\2&\u018d\3\2\2\2(\u018f\3\2\2\2*\u01a6\3")
        buf.write("\2\2\2,\u01b7\3\2\2\2.\u01ca\3\2\2\2\60\u01d6\3\2\2\2")
        buf.write("\62\u01ea\3\2\2\2\64\65\7\37\2\2\65\66\78\2\2\66\67\b")
        buf.write("\2\1\2\678\7\36\2\289\5\4\3\29;\b\2\1\2:<\5\f\7\2;:\3")
        buf.write("\2\2\2;<\3\2\2\2<=\3\2\2\2=>\5\62\32\2>\3\3\2\2\2?A\7")
        buf.write(",\2\2@B\5\6\4\2A@\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2")
        buf.write("\2D\5\3\2\2\2EF\5\b\5\2FG\7\35\2\2GH\78\2\2HT\b\4\1\2")
        buf.write("IJ\7\25\2\2JK\7\64\2\2KL\7\26\2\2LU\b\4\1\2MN\7\25\2\2")
        buf.write("NO\7\64\2\2OP\7\26\2\2PQ\7\25\2\2QR\7\64\2\2RS\7\26\2")
        buf.write("\2SU\b\4\1\2TI\3\2\2\2TM\3\2\2\2TU\3\2\2\2Uh\3\2\2\2V")
        buf.write("W\7\34\2\2WX\78\2\2Xd\b\4\1\2YZ\7\25\2\2Z[\7\64\2\2[\\")
        buf.write("\7\26\2\2\\e\b\4\1\2]^\7\25\2\2^_\7\64\2\2_`\7\26\2\2")
        buf.write("`a\7\25\2\2ab\7\64\2\2bc\7\26\2\2ce\b\4\1\2dY\3\2\2\2")
        buf.write("d]\3\2\2\2de\3\2\2\2eg\3\2\2\2fV\3\2\2\2gj\3\2\2\2hf\3")
        buf.write("\2\2\2hi\3\2\2\2ik\3\2\2\2jh\3\2\2\2kl\7\36\2\2l\7\3\2")
        buf.write("\2\2mn\t\2\2\2n\t\3\2\2\2op\7\62\2\2pq\b\6\1\2q\u0087")
        buf.write("\b\6\1\2rs\7\20\2\2st\7\63\2\2tu\b\6\1\2u\u0087\b\6\1")
        buf.write("\2vw\7\63\2\2wx\b\6\1\2x\u0087\b\6\1\2yz\7\20\2\2z{\7")
        buf.write("\64\2\2{|\b\6\1\2|\u0087\b\6\1\2}~\7\64\2\2~\177\b\6\1")
        buf.write("\2\177\u0087\b\6\1\2\u0080\u0081\7\65\2\2\u0081\u0082")
        buf.write("\b\6\1\2\u0082\u0087\b\6\1\2\u0083\u0084\7\66\2\2\u0084")
        buf.write("\u0085\b\6\1\2\u0085\u0087\b\6\1\2\u0086o\3\2\2\2\u0086")
        buf.write("r\3\2\2\2\u0086v\3\2\2\2\u0086y\3\2\2\2\u0086}\3\2\2\2")
        buf.write("\u0086\u0080\3\2\2\2\u0086\u0083\3\2\2\2\u0087\13\3\2")
        buf.write("\2\2\u0088\u008a\5\16\b\2\u0089\u0088\3\2\2\2\u008a\u008b")
        buf.write("\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c")
        buf.write("\r\3\2\2\2\u008d\u008e\7!\2\2\u008e\u008f\5\20\t\2\u008f")
        buf.write("\u0090\78\2\2\u0090\u0091\b\b\1\2\u0091\u0092\b\b\1\2")
        buf.write("\u0092\u0094\7\23\2\2\u0093\u0095\5\22\n\2\u0094\u0093")
        buf.write("\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0096\3\2\2\2\u0096")
        buf.write("\u0098\7\24\2\2\u0097\u0099\5\4\3\2\u0098\u0097\3\2\2")
        buf.write("\2\u0098\u0099\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b")
        buf.write("\b\b\1\2\u009b\u009d\7\27\2\2\u009c\u009e\5\36\20\2\u009d")
        buf.write("\u009c\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\u00a0\7\30\2\2\u00a0\u00a1\b\b\1\2\u00a1\17\3\2")
        buf.write("\2\2\u00a2\u00a3\t\3\2\2\u00a3\21\3\2\2\2\u00a4\u00a5")
        buf.write("\5\b\5\2\u00a5\u00a6\78\2\2\u00a6\u00ae\b\n\1\2\u00a7")
        buf.write("\u00a8\7\34\2\2\u00a8\u00a9\5\b\5\2\u00a9\u00aa\78\2\2")
        buf.write("\u00aa\u00ab\b\n\1\2\u00ab\u00ad\3\2\2\2\u00ac\u00a7\3")
        buf.write("\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af")
        buf.write("\3\2\2\2\u00af\23\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b2")
        buf.write("\5\26\f\2\u00b2\u00be\b\13\1\2\u00b3\u00b4\7\r\2\2\u00b4")
        buf.write("\u00b8\b\13\1\2\u00b5\u00b6\7\16\2\2\u00b6\u00b8\b\13")
        buf.write("\1\2\u00b7\u00b3\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00b9")
        buf.write("\3\2\2\2\u00b9\u00ba\5\24\13\2\u00ba\u00bb\b\13\1\2\u00bb")
        buf.write("\u00bd\3\2\2\2\u00bc\u00b7\3\2\2\2\u00bd\u00c0\3\2\2\2")
        buf.write("\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\25\3\2")
        buf.write("\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c2\5\30\r\2\u00c2\u00d4")
        buf.write("\b\f\1\2\u00c3\u00c4\7\7\2\2\u00c4\u00d0\b\f\1\2\u00c5")
        buf.write("\u00c6\7\6\2\2\u00c6\u00d0\b\f\1\2\u00c7\u00c8\7\t\2\2")
        buf.write("\u00c8\u00d0\b\f\1\2\u00c9\u00ca\7\b\2\2\u00ca\u00d0\b")
        buf.write("\f\1\2\u00cb\u00cc\7\13\2\2\u00cc\u00d0\b\f\1\2\u00cd")
        buf.write("\u00ce\7\n\2\2\u00ce\u00d0\b\f\1\2\u00cf\u00c3\3\2\2\2")
        buf.write("\u00cf\u00c5\3\2\2\2\u00cf\u00c7\3\2\2\2\u00cf\u00c9\3")
        buf.write("\2\2\2\u00cf\u00cb\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1")
        buf.write("\3\2\2\2\u00d1\u00d2\5\26\f\2\u00d2\u00d3\b\f\1\2\u00d3")
        buf.write("\u00d5\3\2\2\2\u00d4\u00cf\3\2\2\2\u00d4\u00d5\3\2\2\2")
        buf.write("\u00d5\27\3\2\2\2\u00d6\u00d7\5\32\16\2\u00d7\u00e3\b")
        buf.write("\r\1\2\u00d8\u00d9\7\17\2\2\u00d9\u00dd\b\r\1\2\u00da")
        buf.write("\u00db\7\20\2\2\u00db\u00dd\b\r\1\2\u00dc\u00d8\3\2\2")
        buf.write("\2\u00dc\u00da\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df")
        buf.write("\5\30\r\2\u00df\u00e0\b\r\1\2\u00e0\u00e2\3\2\2\2\u00e1")
        buf.write("\u00dc\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3\u00e1\3\2\2\2")
        buf.write("\u00e3\u00e4\3\2\2\2\u00e4\31\3\2\2\2\u00e5\u00e3\3\2")
        buf.write("\2\2\u00e6\u00e7\5\34\17\2\u00e7\u00f3\b\16\1\2\u00e8")
        buf.write("\u00e9\7\21\2\2\u00e9\u00ed\b\16\1\2\u00ea\u00eb\7\22")
        buf.write("\2\2\u00eb\u00ed\b\16\1\2\u00ec\u00e8\3\2\2\2\u00ec\u00ea")
        buf.write("\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00ef\5\32\16\2\u00ef")
        buf.write("\u00f0\b\16\1\2\u00f0\u00f2\3\2\2\2\u00f1\u00ec\3\2\2")
        buf.write("\2\u00f2\u00f5\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f4")
        buf.write("\3\2\2\2\u00f4\33\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f6\u0136")
        buf.write("\5\n\6\2\u00f7\u00f8\7\23\2\2\u00f8\u00f9\b\17\1\2\u00f9")
        buf.write("\u00fa\5\24\13\2\u00fa\u00fb\7\24\2\2\u00fb\u00fc\b\17")
        buf.write("\1\2\u00fc\u0136\3\2\2\2\u00fd\u00fe\78\2\2\u00fe\u011b")
        buf.write("\b\17\1\2\u00ff\u011c\3\2\2\2\u0100\u0101\7\31\2\2\u0101")
        buf.write("\u0107\b\17\1\2\u0102\u0103\7\32\2\2\u0103\u0107\b\17")
        buf.write("\1\2\u0104\u0105\7\33\2\2\u0105\u0107\b\17\1\2\u0106\u0100")
        buf.write("\3\2\2\2\u0106\u0102\3\2\2\2\u0106\u0104\3\2\2\2\u0107")
        buf.write("\u011c\3\2\2\2\u0108\u0109\7\25\2\2\u0109\u010a\b\17\1")
        buf.write("\2\u010a\u010b\5\24\13\2\u010b\u010c\b\17\1\2\u010c\u010d")
        buf.write("\b\17\1\2\u010d\u010e\7\26\2\2\u010e\u011c\3\2\2\2\u010f")
        buf.write("\u0110\7\25\2\2\u0110\u0111\b\17\1\2\u0111\u0112\5\24")
        buf.write("\13\2\u0112\u0113\b\17\1\2\u0113\u0114\7\26\2\2\u0114")
        buf.write("\u0115\7\25\2\2\u0115\u0116\b\17\1\2\u0116\u0117\5\24")
        buf.write("\13\2\u0117\u0118\b\17\1\2\u0118\u0119\b\17\1\2\u0119")
        buf.write("\u011a\7\26\2\2\u011a\u011c\3\2\2\2\u011b\u00ff\3\2\2")
        buf.write("\2\u011b\u0106\3\2\2\2\u011b\u0108\3\2\2\2\u011b\u010f")
        buf.write("\3\2\2\2\u011c\u0136\3\2\2\2\u011d\u011e\78\2\2\u011e")
        buf.write("\u011f\b\17\1\2\u011f\u0120\7\23\2\2\u0120\u0121\b\17")
        buf.write("\1\2\u0121\u012e\b\17\1\2\u0122\u012f\3\2\2\2\u0123\u0124")
        buf.write("\5\24\13\2\u0124\u012b\b\17\1\2\u0125\u0126\7\34\2\2\u0126")
        buf.write("\u0127\5\24\13\2\u0127\u0128\b\17\1\2\u0128\u012a\3\2")
        buf.write("\2\2\u0129\u0125\3\2\2\2\u012a\u012d\3\2\2\2\u012b\u0129")
        buf.write("\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012f\3\2\2\2\u012d")
        buf.write("\u012b\3\2\2\2\u012e\u0122\3\2\2\2\u012e\u0123\3\2\2\2")
        buf.write("\u012f\u0130\3\2\2\2\u0130\u0131\b\17\1\2\u0131\u0132")
        buf.write("\b\17\1\2\u0132\u0133\b\17\1\2\u0133\u0134\7\24\2\2\u0134")
        buf.write("\u0136\b\17\1\2\u0135\u00f6\3\2\2\2\u0135\u00f7\3\2\2")
        buf.write("\2\u0135\u00fd\3\2\2\2\u0135\u011d\3\2\2\2\u0136\35\3")
        buf.write("\2\2\2\u0137\u0140\5 \21\2\u0138\u0140\5\"\22\2\u0139")
        buf.write("\u0140\5$\23\2\u013a\u0140\5(\25\2\u013b\u0140\5*\26\2")
        buf.write("\u013c\u0140\5,\27\2\u013d\u0140\5.\30\2\u013e\u0140\5")
        buf.write("\60\31\2\u013f\u0137\3\2\2\2\u013f\u0138\3\2\2\2\u013f")
        buf.write("\u0139\3\2\2\2\u013f\u013a\3\2\2\2\u013f\u013b\3\2\2\2")
        buf.write("\u013f\u013c\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u013e\3")
        buf.write("\2\2\2\u0140\u0143\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142")
        buf.write("\3\2\2\2\u0142\37\3\2\2\2\u0143\u0141\3\2\2\2\u0144\u0145")
        buf.write("\78\2\2\u0145\u0147\b\21\1\2\u0146\u0148\5&\24\2\u0147")
        buf.write("\u0146\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0149\3\2\2\2")
        buf.write("\u0149\u014a\7\f\2\2\u014a\u0154\b\21\1\2\u014b\u014c")
        buf.write("\78\2\2\u014c\u014e\b\21\1\2\u014d\u014f\5&\24\2\u014e")
        buf.write("\u014d\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150\3\2\2\2")
        buf.write("\u0150\u0151\7\f\2\2\u0151\u0153\b\21\1\2\u0152\u014b")
        buf.write("\3\2\2\2\u0153\u0156\3\2\2\2\u0154\u0152\3\2\2\2\u0154")
        buf.write("\u0155\3\2\2\2\u0155\u0157\3\2\2\2\u0156\u0154\3\2\2\2")
        buf.write("\u0157\u0158\5\24\13\2\u0158\u0159\7\36\2\2\u0159\u015a")
        buf.write("\b\21\1\2\u015a!\3\2\2\2\u015b\u015c\78\2\2\u015c\u015d")
        buf.write("\b\22\1\2\u015d\u015e\7\23\2\2\u015e\u015f\b\22\1\2\u015f")
        buf.write("\u016c\b\22\1\2\u0160\u016d\3\2\2\2\u0161\u0162\5\24\13")
        buf.write("\2\u0162\u0169\b\22\1\2\u0163\u0164\7\34\2\2\u0164\u0165")
        buf.write("\5\24\13\2\u0165\u0166\b\22\1\2\u0166\u0168\3\2\2\2\u0167")
        buf.write("\u0163\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167\3\2\2\2")
        buf.write("\u0169\u016a\3\2\2\2\u016a\u016d\3\2\2\2\u016b\u0169\3")
        buf.write("\2\2\2\u016c\u0160\3\2\2\2\u016c\u0161\3\2\2\2\u016d\u016e")
        buf.write("\3\2\2\2\u016e\u016f\b\22\1\2\u016f\u0170\b\22\1\2\u0170")
        buf.write("\u0171\7\24\2\2\u0171\u0172\7\36\2\2\u0172#\3\2\2\2\u0173")
        buf.write("\u0174\7\"\2\2\u0174\u0175\7\23\2\2\u0175\u0176\5\24\13")
        buf.write("\2\u0176\u0177\7\24\2\2\u0177\u0178\7\36\2\2\u0178\u0179")
        buf.write("\b\23\1\2\u0179%\3\2\2\2\u017a\u017b\7\25\2\2\u017b\u017c")
        buf.write("\b\24\1\2\u017c\u017d\5\24\13\2\u017d\u017e\b\24\1\2\u017e")
        buf.write("\u017f\b\24\1\2\u017f\u0180\7\26\2\2\u0180\u018e\3\2\2")
        buf.write("\2\u0181\u0182\7\25\2\2\u0182\u0183\b\24\1\2\u0183\u0184")
        buf.write("\5\24\13\2\u0184\u0185\b\24\1\2\u0185\u0186\7\26\2\2\u0186")
        buf.write("\u0187\7\25\2\2\u0187\u0188\b\24\1\2\u0188\u0189\5\24")
        buf.write("\13\2\u0189\u018a\b\24\1\2\u018a\u018b\b\24\1\2\u018b")
        buf.write("\u018c\7\26\2\2\u018c\u018e\3\2\2\2\u018d\u017a\3\2\2")
        buf.write("\2\u018d\u0181\3\2\2\2\u018e\'\3\2\2\2\u018f\u0190\7#")
        buf.write("\2\2\u0190\u0191\7\23\2\2\u0191\u0192\78\2\2\u0192\u0194")
        buf.write("\b\25\1\2\u0193\u0195\5&\24\2\u0194\u0193\3\2\2\2\u0194")
        buf.write("\u0195\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u01a0\b\25\1")
        buf.write("\2\u0197\u0198\7\34\2\2\u0198\u019a\78\2\2\u0199\u019b")
        buf.write("\5&\24\2\u019a\u0199\3\2\2\2\u019a\u019b\3\2\2\2\u019b")
        buf.write("\u019c\3\2\2\2\u019c\u019d\b\25\1\2\u019d\u019f\b\25\1")
        buf.write("\2\u019e\u0197\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0\u019e")
        buf.write("\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a3\3\2\2\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a3\u01a4\7\24\2\2\u01a4\u01a5\7\36\2")
        buf.write("\2\u01a5)\3\2\2\2\u01a6\u01a7\7$\2\2\u01a7\u01a8\7\23")
        buf.write("\2\2\u01a8\u01a9\5\24\13\2\u01a9\u01aa\b\26\1\2\u01aa")
        buf.write("\u01b1\3\2\2\2\u01ab\u01ac\7\34\2\2\u01ac\u01ad\5\24\13")
        buf.write("\2\u01ad\u01ae\b\26\1\2\u01ae\u01b0\3\2\2\2\u01af\u01ab")
        buf.write("\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1")
        buf.write("\u01b2\3\2\2\2\u01b2\u01b4\3\2\2\2\u01b3\u01b1\3\2\2\2")
        buf.write("\u01b4\u01b5\7\24\2\2\u01b5\u01b6\7\36\2\2\u01b6+\3\2")
        buf.write("\2\2\u01b7\u01b8\7%\2\2\u01b8\u01b9\7\23\2\2\u01b9\u01ba")
        buf.write("\5\24\13\2\u01ba\u01bb\7\24\2\2\u01bb\u01bc\b\27\1\2\u01bc")
        buf.write("\u01bd\7&\2\2\u01bd\u01be\7\27\2\2\u01be\u01bf\5\36\20")
        buf.write("\2\u01bf\u01c6\7\30\2\2\u01c0\u01c1\7\'\2\2\u01c1\u01c2")
        buf.write("\b\27\1\2\u01c2\u01c3\7\27\2\2\u01c3\u01c4\5\36\20\2\u01c4")
        buf.write("\u01c5\7\30\2\2\u01c5\u01c7\3\2\2\2\u01c6\u01c0\3\2\2")
        buf.write("\2\u01c6\u01c7\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c9")
        buf.write("\b\27\1\2\u01c9-\3\2\2\2\u01ca\u01cb\7(\2\2\u01cb\u01cc")
        buf.write("\7\23\2\2\u01cc\u01cd\b\30\1\2\u01cd\u01ce\5\24\13\2\u01ce")
        buf.write("\u01cf\7\24\2\2\u01cf\u01d0\b\30\1\2\u01d0\u01d1\7)\2")
        buf.write("\2\u01d1\u01d2\7\27\2\2\u01d2\u01d3\5\36\20\2\u01d3\u01d4")
        buf.write("\b\30\1\2\u01d4\u01d5\7\30\2\2\u01d5/\3\2\2\2\u01d6\u01d7")
        buf.write("\7*\2\2\u01d7\u01d8\78\2\2\u01d8\u01da\b\31\1\2\u01d9")
        buf.write("\u01db\5&\24\2\u01da\u01d9\3\2\2\2\u01da\u01db\3\2\2\2")
        buf.write("\u01db\u01dc\3\2\2\2\u01dc\u01dd\7\f\2\2\u01dd\u01de\b")
        buf.write("\31\1\2\u01de\u01df\5\24\13\2\u01df\u01e0\b\31\1\2\u01e0")
        buf.write("\u01e1\7+\2\2\u01e1\u01e2\b\31\1\2\u01e2\u01e3\5\24\13")
        buf.write("\2\u01e3\u01e4\b\31\1\2\u01e4\u01e5\7)\2\2\u01e5\u01e6")
        buf.write("\7\27\2\2\u01e6\u01e7\5\36\20\2\u01e7\u01e8\7\30\2\2\u01e8")
        buf.write("\u01e9\b\31\1\2\u01e9\61\3\2\2\2\u01ea\u01eb\7 \2\2\u01eb")
        buf.write("\u01ec\b\32\1\2\u01ec\u01ed\7\23\2\2\u01ed\u01ee\7\24")
        buf.write("\2\2\u01ee\u01ef\b\32\1\2\u01ef\u01f0\7\27\2\2\u01f0\u01f1")
        buf.write("\b\32\1\2\u01f1\u01f2\5\36\20\2\u01f2\u01f3\7\30\2\2\u01f3")
        buf.write("\63\3\2\2\2(;CTdh\u0086\u008b\u0094\u0098\u009d\u00ae")
        buf.write("\u00b7\u00be\u00cf\u00d4\u00dc\u00e3\u00ec\u00f3\u0106")
        buf.write("\u011b\u012b\u012e\u0135\u013f\u0141\u0147\u014e\u0154")
        buf.write("\u0169\u016c\u018d\u0194\u019a\u01a0\u01b1\u01c6\u01da")
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
            self.state = 307
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
                self.state = 281
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
                    self.compiler.addParenthesis()
                    self.state = 264
                    self.mexp()
                    self.compiler.popParenthesis()
                    self.compiler.verify_one_index()
                    self.state = 267
                    self.match(patitoParser.RIGHT_BRACKET)
                    pass

                elif la_ == 4:
                    self.state = 269
                    self.match(patitoParser.LEFT_BRACKET)
                    self.compiler.addParenthesis()
                    self.state = 271
                    self.mexp()
                    self.compiler.popParenthesis()
                    self.state = 273
                    self.match(patitoParser.RIGHT_BRACKET)
                    self.state = 274
                    self.match(patitoParser.LEFT_BRACKET)
                    self.compiler.addParenthesis()
                    self.state = 276
                    self.mexp()
                    self.compiler.popParenthesis()
                    self.compiler.verify_two_indexes()
                    self.state = 279
                    self.match(patitoParser.RIGHT_BRACKET)
                    pass


                pass

            elif la_ == 4:
                self.state = 283
                localctx._ID = self.match(patitoParser.ID)
                self.compiler.validate_function_expression((None if localctx._ID is None else localctx._ID.text))
                self.state = 285
                self.match(patitoParser.LEFT_PARENTHESIS)
                self.compiler.addParenthesis()
                currentCounter=0
                self.state = 300
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [patitoParser.RIGHT_PARENTHESIS]:
                    pass
                elif token in [patitoParser.SUB, patitoParser.LEFT_PARENTHESIS, patitoParser.CTE_BOOL, patitoParser.CTE_FLOAT, patitoParser.CTE_INT, patitoParser.CTE_CHAR, patitoParser.CTE_STRING, patitoParser.ID]:
                    self.state = 289
                    self.mexp()
                    currentCounter += 1
                    self.state = 297
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==patitoParser.COMMA:
                        self.state = 291
                        self.match(patitoParser.COMMA)
                        self.state = 292
                        self.mexp()
                        currentCounter += 1
                        self.state = 299
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                else:
                    raise NoViableAltException(self)

                self.compiler.validate_parameters((None if localctx._ID is None else localctx._ID.text), currentCounter)
                self.compiler.add_func_operand_and_type((None if localctx._ID is None else localctx._ID.text))
                self.compiler.goto_function_quad((None if localctx._ID is None else localctx._ID.text))
                self.state = 305
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
            self.state = 319
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.RETURN) | (1 << patitoParser.INPUT) | (1 << patitoParser.PRINT) | (1 << patitoParser.IF) | (1 << patitoParser.WHILE) | (1 << patitoParser.FROM) | (1 << patitoParser.ID))) != 0):
                self.state = 317
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 309
                    self.assignation()
                    pass

                elif la_ == 2:
                    self.state = 310
                    self.funccall()
                    pass

                elif la_ == 3:
                    self.state = 311
                    self.returncall()
                    pass

                elif la_ == 4:
                    self.state = 312
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 313
                    self.write()
                    pass

                elif la_ == 6:
                    self.state = 314
                    self.conditional()
                    pass

                elif la_ == 7:
                    self.state = 315
                    self.whileloop()
                    pass

                elif la_ == 8:
                    self.state = 316
                    self.fromloop()
                    pass


                self.state = 321
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
            self.state = 322
            localctx._ID = self.match(patitoParser.ID)
            self.compiler.addOperandAndType((None if localctx._ID is None else localctx._ID.text))
            self.state = 325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.LEFT_BRACKET:
                self.state = 324
                self.indexvariable()


            self.state = 327
            localctx._ASSIGN = self.match(patitoParser.ASSIGN)
            self.compiler.addOperator((None if localctx._ASSIGN is None else localctx._ASSIGN.text))
            self.state = 338
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 329
                    localctx._ID = self.match(patitoParser.ID)
                    self.compiler.addOperandAndType((None if localctx._ID is None else localctx._ID.text))
                    self.state = 332
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==patitoParser.LEFT_BRACKET:
                        self.state = 331
                        self.indexvariable()


                    self.state = 334
                    localctx._ASSIGN = self.match(patitoParser.ASSIGN)
                    self.compiler.addOperator((None if localctx._ASSIGN is None else localctx._ASSIGN.text))
                self.state = 340
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

            self.state = 341
            self.mexp()
            self.state = 342
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
            self.state = 345
            localctx._ID = self.match(patitoParser.ID)
            self.compiler.validate_void_function((None if localctx._ID is None else localctx._ID.text))
            self.state = 347
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.compiler.addParenthesis()
            currentCounter=0
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [patitoParser.RIGHT_PARENTHESIS]:
                pass
            elif token in [patitoParser.SUB, patitoParser.LEFT_PARENTHESIS, patitoParser.CTE_BOOL, patitoParser.CTE_FLOAT, patitoParser.CTE_INT, patitoParser.CTE_CHAR, patitoParser.CTE_STRING, patitoParser.ID]:
                self.state = 351
                self.mexp()
                currentCounter += 1
                self.state = 359
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==patitoParser.COMMA:
                    self.state = 353
                    self.match(patitoParser.COMMA)
                    self.state = 354
                    self.mexp()
                    currentCounter += 1
                    self.state = 361
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.compiler.validate_parameters((None if localctx._ID is None else localctx._ID.text), currentCounter)
            self.compiler.goto_void_function_quad((None if localctx._ID is None else localctx._ID.text))
            self.state = 366
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 367
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
            self.state = 369
            self.match(patitoParser.RETURN)
            self.state = 370
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 371
            self.mexp()
            self.state = 372
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 373
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
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 376
                self.match(patitoParser.LEFT_BRACKET)
                self.compiler.addParenthesis()
                self.state = 378
                self.mexp()
                self.compiler.popParenthesis()
                self.compiler.verify_one_index()
                self.state = 381
                self.match(patitoParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.state = 383
                self.match(patitoParser.LEFT_BRACKET)
                self.compiler.addParenthesis()
                self.state = 385
                self.mexp()
                self.compiler.popParenthesis()
                self.state = 387
                self.match(patitoParser.RIGHT_BRACKET)
                self.state = 388
                self.match(patitoParser.LEFT_BRACKET)
                self.compiler.addParenthesis()
                self.state = 390
                self.mexp()
                self.compiler.popParenthesis()
                self.compiler.verify_two_indexes()
                self.state = 393
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
            self.state = 397
            self.match(patitoParser.INPUT)
            self.state = 398
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 399
            localctx.var_id = self.match(patitoParser.ID)
            self.compiler.addOperandAndType((None if localctx.var_id is None else localctx.var_id.text))
            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.LEFT_BRACKET:
                self.state = 401
                self.indexvariable()


            self.compiler.generateReadQuad()
            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 405
                self.match(patitoParser.COMMA)
                self.state = 406
                localctx.var_id2 = self.match(patitoParser.ID)
                self.state = 408
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==patitoParser.LEFT_BRACKET:
                    self.state = 407
                    self.indexvariable()


                self.compiler.addOperandAndType((None if localctx.var_id2 is None else localctx.var_id2.text))
                self.compiler.generateReadQuad()
                self.state = 416
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 417
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 418
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
            self.state = 420
            self.match(patitoParser.PRINT)
            self.state = 421
            self.match(patitoParser.LEFT_PARENTHESIS)

            self.state = 422
            self.mexp()
            self.compiler.generateWriteQuad()
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 425
                self.match(patitoParser.COMMA)

                self.state = 426
                self.mexp()
                self.compiler.generateWriteQuad()
                self.state = 433
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 434
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 435
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
            self.state = 437
            self.match(patitoParser.IF)
            self.state = 438
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 439
            self.mexp()
            self.state = 440
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.compiler.generateIfQuad()
            self.state = 442
            self.match(patitoParser.THEN)
            self.state = 443
            self.match(patitoParser.LEFT_CURLY)
            self.state = 444
            self.statute()
            self.state = 445
            self.match(patitoParser.RIGHT_CURLY)
            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.ELSE:
                self.state = 446
                self.match(patitoParser.ELSE)
                self.compiler.generateGoToQuad()
                self.state = 448
                self.match(patitoParser.LEFT_CURLY)
                self.state = 449
                self.statute()
                self.state = 450
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
            self.state = 456
            self.match(patitoParser.WHILE)
            self.state = 457
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.compiler.generateWhileBeforeCheck()
            self.state = 459
            self.mexp()
            self.state = 460
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.compiler.generateWhileAfterCheck()
            self.state = 462
            self.match(patitoParser.DO)
            self.state = 463
            self.match(patitoParser.LEFT_CURLY)
            self.state = 464
            self.statute()
            self.compiler.generateWhileEnd()
            self.state = 466
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
            self.state = 468
            self.match(patitoParser.FROM)
            self.state = 469
            localctx._ID = self.match(patitoParser.ID)
            self.compiler.addFromVarOperand((None if localctx._ID is None else localctx._ID.text))
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.LEFT_BRACKET:
                self.state = 471
                self.indexvariable()


            self.state = 474
            localctx._ASSIGN = self.match(patitoParser.ASSIGN)
            self.compiler.addOperator((None if localctx._ASSIGN is None else localctx._ASSIGN.text))
            self.state = 476
            self.mexp()
            self.compiler.generateAssignQuads()
            self.state = 478
            self.match(patitoParser.TO)
            self.compiler.generateFromBeforeCheck()
            self.state = 480
            self.mexp()
            self.compiler.generateFromAfterCheck()
            self.state = 482
            self.match(patitoParser.DO)
            self.state = 483
            self.match(patitoParser.LEFT_CURLY)
            self.state = 484
            self.statute()
            self.state = 485
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
            self.state = 488
            self.match(patitoParser.MAIN)
            self.compiler.currentFunction=Function("main", "void", [], {})
            self.state = 490
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 491
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.compiler._add_function(self.compiler.currentFunction)
            self.state = 493
            self.match(patitoParser.LEFT_CURLY)
            self.compiler.fill_goto_main_quad()
            self.state = 495
            self.statute()
            self.state = 496
            self.match(patitoParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





