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
        buf.write("\u01cd\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\6\3B\n\3\r\3\16\3C\3\4\3\4\3\4\3\4\5")
        buf.write("\4J\n\4\3\4\3\4\3\4\3\4\5\4P\n\4\3\4\7\4S\n\4\f\4\16\4")
        buf.write("V\13\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\5\6s\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5")
        buf.write("\7~\n\7\3\b\6\b\u0081\n\b\r\b\16\b\u0082\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\5\t\u008c\n\t\3\t\3\t\5\t\u0090\n\t\3\t")
        buf.write("\3\t\3\t\5\t\u0095\n\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\7\13\u00a4\n\13\f\13\16\13")
        buf.write("\u00a7\13\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00af\n\f\3\f")
        buf.write("\3\f\3\f\7\f\u00b4\n\f\f\f\16\f\u00b7\13\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00c7")
        buf.write("\n\r\3\r\3\r\3\r\5\r\u00cc\n\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u00d4\n\16\3\16\3\16\3\16\7\16\u00d9\n\16\f")
        buf.write("\16\16\16\u00dc\13\16\3\17\3\17\3\17\3\17\3\17\3\17\5")
        buf.write("\17\u00e4\n\17\3\17\3\17\3\17\7\17\u00e9\n\17\f\17\16")
        buf.write("\17\u00ec\13\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u0104\n\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u0111\n\20\f\20")
        buf.write("\16\20\u0114\13\20\5\20\u0116\n\20\3\20\3\20\3\20\5\20")
        buf.write("\u011b\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7")
        buf.write("\21\u0125\n\21\f\21\16\21\u0128\13\21\3\22\3\22\3\22\5")
        buf.write("\22\u012d\n\22\3\22\3\22\3\22\3\22\3\22\5\22\u0134\n\22")
        buf.write("\3\22\3\22\7\22\u0138\n\22\f\22\16\22\u013b\13\22\3\22")
        buf.write("\3\22\3\22\5\22\u0140\n\22\3\22\3\22\3\22\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\7\23\u014c\n\23\f\23\16\23\u014f")
        buf.write("\13\23\5\23\u0151\n\23\3\23\3\23\3\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u0168\n\25\3\26\3\26\3\26\3")
        buf.write("\26\5\26\u016e\n\26\3\26\3\26\3\26\3\26\5\26\u0174\n\26")
        buf.write("\3\26\7\26\u0177\n\26\f\26\16\26\u017a\13\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27")
        buf.write("\u0188\n\27\f\27\16\27\u018b\13\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\5\30\u019f\n\30\3\30\3\30\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u01b3\n\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\2\2")
        buf.write("\34\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\2\5\3\2-\61\4\2-\61\67\67\3\2\31\33\2\u01eb\2\66")
        buf.write("\3\2\2\2\4?\3\2\2\2\6E\3\2\2\2\bY\3\2\2\2\nr\3\2\2\2\f")
        buf.write("}\3\2\2\2\16\u0080\3\2\2\2\20\u0084\3\2\2\2\22\u0099\3")
        buf.write("\2\2\2\24\u009b\3\2\2\2\26\u00a8\3\2\2\2\30\u00b8\3\2")
        buf.write("\2\2\32\u00cd\3\2\2\2\34\u00dd\3\2\2\2\36\u011a\3\2\2")
        buf.write("\2 \u0126\3\2\2\2\"\u0129\3\2\2\2$\u0144\3\2\2\2&\u0155")
        buf.write("\3\2\2\2(\u0167\3\2\2\2*\u0169\3\2\2\2,\u017e\3\2\2\2")
        buf.write(".\u018f\3\2\2\2\60\u01a2\3\2\2\2\62\u01ae\3\2\2\2\64\u01c2")
        buf.write("\3\2\2\2\66\67\7\37\2\2\678\78\2\289\b\2\1\29:\7\36\2")
        buf.write("\2:;\5\4\3\2;<\b\2\1\2<=\5\16\b\2=>\5\64\33\2>\3\3\2\2")
        buf.write("\2?A\7,\2\2@B\5\6\4\2A@\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD")
        buf.write("\3\2\2\2D\5\3\2\2\2EF\5\b\5\2FG\7\35\2\2GI\78\2\2HJ\5")
        buf.write("\f\7\2IH\3\2\2\2IJ\3\2\2\2JK\3\2\2\2KT\b\4\1\2LM\7\34")
        buf.write("\2\2MO\78\2\2NP\5\f\7\2ON\3\2\2\2OP\3\2\2\2PQ\3\2\2\2")
        buf.write("QS\b\4\1\2RL\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2UW\3")
        buf.write("\2\2\2VT\3\2\2\2WX\7\36\2\2X\7\3\2\2\2YZ\t\2\2\2Z\t\3")
        buf.write("\2\2\2[\\\7\62\2\2\\]\b\6\1\2]s\b\6\1\2^_\7\20\2\2_`\7")
        buf.write("\63\2\2`a\b\6\1\2as\b\6\1\2bc\7\63\2\2cd\b\6\1\2ds\b\6")
        buf.write("\1\2ef\7\20\2\2fg\7\64\2\2gh\b\6\1\2hs\b\6\1\2ij\7\64")
        buf.write("\2\2jk\b\6\1\2ks\b\6\1\2lm\7\65\2\2mn\b\6\1\2ns\b\6\1")
        buf.write("\2op\7\66\2\2pq\b\6\1\2qs\b\6\1\2r[\3\2\2\2r^\3\2\2\2")
        buf.write("rb\3\2\2\2re\3\2\2\2ri\3\2\2\2rl\3\2\2\2ro\3\2\2\2s\13")
        buf.write("\3\2\2\2tu\7\25\2\2uv\7\64\2\2v~\7\26\2\2wx\7\25\2\2x")
        buf.write("y\7\64\2\2yz\7\26\2\2z{\7\25\2\2{|\7\64\2\2|~\7\26\2\2")
        buf.write("}t\3\2\2\2}w\3\2\2\2~\r\3\2\2\2\177\u0081\5\20\t\2\u0080")
        buf.write("\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0080\3\2\2\2\u0082")
        buf.write("\u0083\3\2\2\2\u0083\17\3\2\2\2\u0084\u0085\7!\2\2\u0085")
        buf.write("\u0086\5\22\n\2\u0086\u0087\78\2\2\u0087\u0088\b\t\1\2")
        buf.write("\u0088\u0089\b\t\1\2\u0089\u008b\7\23\2\2\u008a\u008c")
        buf.write("\5\24\13\2\u008b\u008a\3\2\2\2\u008b\u008c\3\2\2\2\u008c")
        buf.write("\u008d\3\2\2\2\u008d\u008f\7\24\2\2\u008e\u0090\5\4\3")
        buf.write("\2\u008f\u008e\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0091")
        buf.write("\3\2\2\2\u0091\u0092\b\t\1\2\u0092\u0094\7\27\2\2\u0093")
        buf.write("\u0095\5 \21\2\u0094\u0093\3\2\2\2\u0094\u0095\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\u0097\7\30\2\2\u0097\u0098")
        buf.write("\b\t\1\2\u0098\21\3\2\2\2\u0099\u009a\t\3\2\2\u009a\23")
        buf.write("\3\2\2\2\u009b\u009c\5\b\5\2\u009c\u009d\78\2\2\u009d")
        buf.write("\u00a5\b\13\1\2\u009e\u009f\7\34\2\2\u009f\u00a0\5\b\5")
        buf.write("\2\u00a0\u00a1\78\2\2\u00a1\u00a2\b\13\1\2\u00a2\u00a4")
        buf.write("\3\2\2\2\u00a3\u009e\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5")
        buf.write("\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\25\3\2\2\2\u00a7")
        buf.write("\u00a5\3\2\2\2\u00a8\u00a9\5\30\r\2\u00a9\u00b5\b\f\1")
        buf.write("\2\u00aa\u00ab\7\r\2\2\u00ab\u00af\b\f\1\2\u00ac\u00ad")
        buf.write("\7\16\2\2\u00ad\u00af\b\f\1\2\u00ae\u00aa\3\2\2\2\u00ae")
        buf.write("\u00ac\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\5\26\f")
        buf.write("\2\u00b1\u00b2\b\f\1\2\u00b2\u00b4\3\2\2\2\u00b3\u00ae")
        buf.write("\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5")
        buf.write("\u00b6\3\2\2\2\u00b6\27\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8")
        buf.write("\u00b9\5\32\16\2\u00b9\u00cb\b\r\1\2\u00ba\u00bb\7\7\2")
        buf.write("\2\u00bb\u00c7\b\r\1\2\u00bc\u00bd\7\6\2\2\u00bd\u00c7")
        buf.write("\b\r\1\2\u00be\u00bf\7\t\2\2\u00bf\u00c7\b\r\1\2\u00c0")
        buf.write("\u00c1\7\b\2\2\u00c1\u00c7\b\r\1\2\u00c2\u00c3\7\13\2")
        buf.write("\2\u00c3\u00c7\b\r\1\2\u00c4\u00c5\7\n\2\2\u00c5\u00c7")
        buf.write("\b\r\1\2\u00c6\u00ba\3\2\2\2\u00c6\u00bc\3\2\2\2\u00c6")
        buf.write("\u00be\3\2\2\2\u00c6\u00c0\3\2\2\2\u00c6\u00c2\3\2\2\2")
        buf.write("\u00c6\u00c4\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\5")
        buf.write("\30\r\2\u00c9\u00ca\b\r\1\2\u00ca\u00cc\3\2\2\2\u00cb")
        buf.write("\u00c6\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\31\3\2\2\2\u00cd")
        buf.write("\u00ce\5\34\17\2\u00ce\u00da\b\16\1\2\u00cf\u00d0\7\17")
        buf.write("\2\2\u00d0\u00d4\b\16\1\2\u00d1\u00d2\7\20\2\2\u00d2\u00d4")
        buf.write("\b\16\1\2\u00d3\u00cf\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4")
        buf.write("\u00d5\3\2\2\2\u00d5\u00d6\5\32\16\2\u00d6\u00d7\b\16")
        buf.write("\1\2\u00d7\u00d9\3\2\2\2\u00d8\u00d3\3\2\2\2\u00d9\u00dc")
        buf.write("\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db")
        buf.write("\33\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd\u00de\5\36\20\2")
        buf.write("\u00de\u00ea\b\17\1\2\u00df\u00e0\7\21\2\2\u00e0\u00e4")
        buf.write("\b\17\1\2\u00e1\u00e2\7\22\2\2\u00e2\u00e4\b\17\1\2\u00e3")
        buf.write("\u00df\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4\u00e5\3\2\2\2")
        buf.write("\u00e5\u00e6\5\34\17\2\u00e6\u00e7\b\17\1\2\u00e7\u00e9")
        buf.write("\3\2\2\2\u00e8\u00e3\3\2\2\2\u00e9\u00ec\3\2\2\2\u00ea")
        buf.write("\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\35\3\2\2\2\u00ec")
        buf.write("\u00ea\3\2\2\2\u00ed\u011b\5\n\6\2\u00ee\u00ef\7\23\2")
        buf.write("\2\u00ef\u00f0\b\20\1\2\u00f0\u00f1\5\26\f\2\u00f1\u00f2")
        buf.write("\7\24\2\2\u00f2\u00f3\b\20\1\2\u00f3\u011b\3\2\2\2\u00f4")
        buf.write("\u00f5\78\2\2\u00f5\u0103\b\20\1\2\u00f6\u0104\3\2\2\2")
        buf.write("\u00f7\u0104\t\4\2\2\u00f8\u00f9\7\25\2\2\u00f9\u00fa")
        buf.write("\5\26\f\2\u00fa\u00fb\7\26\2\2\u00fb\u0104\3\2\2\2\u00fc")
        buf.write("\u00fd\7\25\2\2\u00fd\u00fe\5\26\f\2\u00fe\u00ff\7\26")
        buf.write("\2\2\u00ff\u0100\7\25\2\2\u0100\u0101\5\26\f\2\u0101\u0102")
        buf.write("\7\26\2\2\u0102\u0104\3\2\2\2\u0103\u00f6\3\2\2\2\u0103")
        buf.write("\u00f7\3\2\2\2\u0103\u00f8\3\2\2\2\u0103\u00fc\3\2\2\2")
        buf.write("\u0104\u011b\3\2\2\2\u0105\u0106\78\2\2\u0106\u0107\b")
        buf.write("\20\1\2\u0107\u0108\7\23\2\2\u0108\u0115\b\20\1\2\u0109")
        buf.write("\u0116\3\2\2\2\u010a\u010b\5\26\f\2\u010b\u0112\b\20\1")
        buf.write("\2\u010c\u010d\7\34\2\2\u010d\u010e\5\26\f\2\u010e\u010f")
        buf.write("\b\20\1\2\u010f\u0111\3\2\2\2\u0110\u010c\3\2\2\2\u0111")
        buf.write("\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2")
        buf.write("\u0113\u0116\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0109\3")
        buf.write("\2\2\2\u0115\u010a\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118")
        buf.write("\b\20\1\2\u0118\u0119\b\20\1\2\u0119\u011b\7\24\2\2\u011a")
        buf.write("\u00ed\3\2\2\2\u011a\u00ee\3\2\2\2\u011a\u00f4\3\2\2\2")
        buf.write("\u011a\u0105\3\2\2\2\u011b\37\3\2\2\2\u011c\u0125\5\"")
        buf.write("\22\2\u011d\u0125\5$\23\2\u011e\u0125\5&\24\2\u011f\u0125")
        buf.write("\5*\26\2\u0120\u0125\5,\27\2\u0121\u0125\5.\30\2\u0122")
        buf.write("\u0125\5\60\31\2\u0123\u0125\5\62\32\2\u0124\u011c\3\2")
        buf.write("\2\2\u0124\u011d\3\2\2\2\u0124\u011e\3\2\2\2\u0124\u011f")
        buf.write("\3\2\2\2\u0124\u0120\3\2\2\2\u0124\u0121\3\2\2\2\u0124")
        buf.write("\u0122\3\2\2\2\u0124\u0123\3\2\2\2\u0125\u0128\3\2\2\2")
        buf.write("\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127!\3\2\2")
        buf.write("\2\u0128\u0126\3\2\2\2\u0129\u012a\78\2\2\u012a\u012c")
        buf.write("\b\22\1\2\u012b\u012d\5(\25\2\u012c\u012b\3\2\2\2\u012c")
        buf.write("\u012d\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u012f\7\f\2\2")
        buf.write("\u012f\u0139\b\22\1\2\u0130\u0131\78\2\2\u0131\u0133\b")
        buf.write("\22\1\2\u0132\u0134\5(\25\2\u0133\u0132\3\2\2\2\u0133")
        buf.write("\u0134\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\7\f\2\2")
        buf.write("\u0136\u0138\b\22\1\2\u0137\u0130\3\2\2\2\u0138\u013b")
        buf.write("\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write("\u013f\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u013d\78\2\2")
        buf.write("\u013d\u0140\b\22\1\2\u013e\u0140\5\26\f\2\u013f\u013c")
        buf.write("\3\2\2\2\u013f\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141")
        buf.write("\u0142\7\36\2\2\u0142\u0143\b\22\1\2\u0143#\3\2\2\2\u0144")
        buf.write("\u0145\78\2\2\u0145\u0146\b\23\1\2\u0146\u0150\7\23\2")
        buf.write("\2\u0147\u0151\3\2\2\2\u0148\u014d\5\26\f\2\u0149\u014a")
        buf.write("\7\34\2\2\u014a\u014c\5\26\f\2\u014b\u0149\3\2\2\2\u014c")
        buf.write("\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2")
        buf.write("\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0147\3")
        buf.write("\2\2\2\u0150\u0148\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0153")
        buf.write("\7\24\2\2\u0153\u0154\7\36\2\2\u0154%\3\2\2\2\u0155\u0156")
        buf.write("\7\"\2\2\u0156\u0157\7\23\2\2\u0157\u0158\5\26\f\2\u0158")
        buf.write("\u0159\7\24\2\2\u0159\u015a\7\36\2\2\u015a\u015b\b\24")
        buf.write("\1\2\u015b\'\3\2\2\2\u015c\u015d\7\25\2\2\u015d\u015e")
        buf.write("\5\26\f\2\u015e\u015f\7\26\2\2\u015f\u0168\3\2\2\2\u0160")
        buf.write("\u0161\7\25\2\2\u0161\u0162\5\26\f\2\u0162\u0163\7\26")
        buf.write("\2\2\u0163\u0164\7\25\2\2\u0164\u0165\5\26\f\2\u0165\u0166")
        buf.write("\7\26\2\2\u0166\u0168\3\2\2\2\u0167\u015c\3\2\2\2\u0167")
        buf.write("\u0160\3\2\2\2\u0168)\3\2\2\2\u0169\u016a\7#\2\2\u016a")
        buf.write("\u016b\7\23\2\2\u016b\u016d\78\2\2\u016c\u016e\5(\25\2")
        buf.write("\u016d\u016c\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\3")
        buf.write("\2\2\2\u016f\u0178\b\26\1\2\u0170\u0171\7\34\2\2\u0171")
        buf.write("\u0173\78\2\2\u0172\u0174\5(\25\2\u0173\u0172\3\2\2\2")
        buf.write("\u0173\u0174\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0177\b")
        buf.write("\26\1\2\u0176\u0170\3\2\2\2\u0177\u017a\3\2\2\2\u0178")
        buf.write("\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017b\3\2\2\2")
        buf.write("\u017a\u0178\3\2\2\2\u017b\u017c\7\24\2\2\u017c\u017d")
        buf.write("\7\36\2\2\u017d+\3\2\2\2\u017e\u017f\7$\2\2\u017f\u0180")
        buf.write("\7\23\2\2\u0180\u0181\5\26\f\2\u0181\u0182\b\27\1\2\u0182")
        buf.write("\u0189\3\2\2\2\u0183\u0184\7\34\2\2\u0184\u0185\5\26\f")
        buf.write("\2\u0185\u0186\b\27\1\2\u0186\u0188\3\2\2\2\u0187\u0183")
        buf.write("\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2\u0189")
        buf.write("\u018a\3\2\2\2\u018a\u018c\3\2\2\2\u018b\u0189\3\2\2\2")
        buf.write("\u018c\u018d\7\24\2\2\u018d\u018e\7\36\2\2\u018e-\3\2")
        buf.write("\2\2\u018f\u0190\7%\2\2\u0190\u0191\7\23\2\2\u0191\u0192")
        buf.write("\5\26\f\2\u0192\u0193\7\24\2\2\u0193\u0194\b\30\1\2\u0194")
        buf.write("\u0195\7&\2\2\u0195\u0196\7\27\2\2\u0196\u0197\5 \21\2")
        buf.write("\u0197\u019e\7\30\2\2\u0198\u0199\7\'\2\2\u0199\u019a")
        buf.write("\b\30\1\2\u019a\u019b\7\27\2\2\u019b\u019c\5 \21\2\u019c")
        buf.write("\u019d\7\30\2\2\u019d\u019f\3\2\2\2\u019e\u0198\3\2\2")
        buf.write("\2\u019e\u019f\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1")
        buf.write("\b\30\1\2\u01a1/\3\2\2\2\u01a2\u01a3\7(\2\2\u01a3\u01a4")
        buf.write("\7\23\2\2\u01a4\u01a5\b\31\1\2\u01a5\u01a6\5\26\f\2\u01a6")
        buf.write("\u01a7\7\24\2\2\u01a7\u01a8\b\31\1\2\u01a8\u01a9\7)\2")
        buf.write("\2\u01a9\u01aa\7\27\2\2\u01aa\u01ab\5 \21\2\u01ab\u01ac")
        buf.write("\b\31\1\2\u01ac\u01ad\7\30\2\2\u01ad\61\3\2\2\2\u01ae")
        buf.write("\u01af\7*\2\2\u01af\u01b0\78\2\2\u01b0\u01b2\b\32\1\2")
        buf.write("\u01b1\u01b3\5(\25\2\u01b2\u01b1\3\2\2\2\u01b2\u01b3\3")
        buf.write("\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\7\f\2\2\u01b5\u01b6")
        buf.write("\b\32\1\2\u01b6\u01b7\5\26\f\2\u01b7\u01b8\b\32\1\2\u01b8")
        buf.write("\u01b9\7+\2\2\u01b9\u01ba\b\32\1\2\u01ba\u01bb\5\26\f")
        buf.write("\2\u01bb\u01bc\b\32\1\2\u01bc\u01bd\7)\2\2\u01bd\u01be")
        buf.write("\7\27\2\2\u01be\u01bf\5 \21\2\u01bf\u01c0\7\30\2\2\u01c0")
        buf.write("\u01c1\b\32\1\2\u01c1\63\3\2\2\2\u01c2\u01c3\7 \2\2\u01c3")
        buf.write("\u01c4\b\33\1\2\u01c4\u01c5\7\23\2\2\u01c5\u01c6\7\24")
        buf.write("\2\2\u01c6\u01c7\b\33\1\2\u01c7\u01c8\7\27\2\2\u01c8\u01c9")
        buf.write("\b\33\1\2\u01c9\u01ca\5 \21\2\u01ca\u01cb\7\30\2\2\u01cb")
        buf.write("\65\3\2\2\2(CIOTr}\u0082\u008b\u008f\u0094\u00a5\u00ae")
        buf.write("\u00b5\u00c6\u00cb\u00d3\u00da\u00e3\u00ea\u0103\u0112")
        buf.write("\u0115\u011a\u0124\u0126\u012c\u0133\u0139\u013f\u014d")
        buf.write("\u0150\u0167\u016d\u0173\u0178\u0189\u019e\u01b2")
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
            compiler._add_function(compiler.currentFunction)
            self.state = 55
            self.match(patitoParser.SEMICOLON)
            self.state = 56
            self.declarevars()
            compiler.goto_main_quad()
            self.state = 58
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
            self.state = 67
            localctx._vartypes = self.vartypes()
            self.state = 68
            self.match(patitoParser.COLON)
            self.state = 69
            localctx._ID = self.match(patitoParser.ID)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.LEFT_BRACKET:
                self.state = 70
                self.arrayconstant()


            compiler.update_vars_table((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 74
                self.match(patitoParser.COMMA)
                self.state = 75
                localctx._ID = self.match(patitoParser.ID)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==patitoParser.LEFT_BRACKET:
                    self.state = 76
                    self.arrayconstant()


                compiler.update_vars_table((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
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
            self.state = 87
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
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 89
                localctx._CTE_BOOL = self.match(patitoParser.CTE_BOOL)
                compiler.addOperand((None if localctx._CTE_BOOL is None else localctx._CTE_BOOL.text))
                compiler.addConstantToTypeStackAndTable("bool")
                pass

            elif la_ == 2:
                self.state = 92
                self.match(patitoParser.SUB)
                self.state = 93
                localctx._CTE_FLOAT = self.match(patitoParser.CTE_FLOAT)
                compiler.addOperand("-" + (None if localctx._CTE_FLOAT is None else localctx._CTE_FLOAT.text))
                compiler.addConstantToTypeStackAndTable("float")
                pass

            elif la_ == 3:
                self.state = 96
                localctx._CTE_FLOAT = self.match(patitoParser.CTE_FLOAT)
                compiler.addOperand((None if localctx._CTE_FLOAT is None else localctx._CTE_FLOAT.text))
                compiler.addConstantToTypeStackAndTable("float")
                pass

            elif la_ == 4:
                self.state = 99
                self.match(patitoParser.SUB)
                self.state = 100
                localctx._CTE_INT = self.match(patitoParser.CTE_INT)
                compiler.addOperand("-" + (None if localctx._CTE_INT is None else localctx._CTE_INT.text))
                compiler.addConstantToTypeStackAndTable("int")
                pass

            elif la_ == 5:
                self.state = 103
                localctx._CTE_INT = self.match(patitoParser.CTE_INT)
                compiler.addOperand((None if localctx._CTE_INT is None else localctx._CTE_INT.text))
                compiler.addConstantToTypeStackAndTable("int")
                pass

            elif la_ == 6:
                self.state = 106
                localctx._CTE_CHAR = self.match(patitoParser.CTE_CHAR)
                compiler.addOperand((None if localctx._CTE_CHAR is None else localctx._CTE_CHAR.text))
                compiler.addConstantToTypeStackAndTable("char")
                pass

            elif la_ == 7:
                self.state = 109
                localctx._CTE_STRING = self.match(patitoParser.CTE_STRING)
                compiler.addOperand((None if localctx._CTE_STRING is None else localctx._CTE_STRING.text))
                compiler.addConstantToTypeStackAndTable("string")
                pass


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
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 115
                self.match(patitoParser.CTE_INT)
                self.state = 116
                self.match(patitoParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 118
                self.match(patitoParser.CTE_INT)
                self.state = 119
                self.match(patitoParser.RIGHT_BRACKET)
                self.state = 120
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 121
                self.match(patitoParser.CTE_INT)
                self.state = 122
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
            self.state = 126 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 125
                self.function()
                self.state = 128 
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
            self.state = 130
            self.match(patitoParser.FUNCTION)
            self.state = 131
            localctx._functiontype = self.functiontype()
            self.state = 132
            localctx._ID = self.match(patitoParser.ID)
            compiler.currentFunction=Function((None if localctx._ID is None else localctx._ID.text), (None if localctx._functiontype is None else self._input.getText(localctx._functiontype.start,localctx._functiontype.stop)), [], {})
            compiler.clear_local_memory()
            self.state = 135
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.BOOL) | (1 << patitoParser.INT) | (1 << patitoParser.FLOAT) | (1 << patitoParser.STRING) | (1 << patitoParser.CHAR))) != 0):
                self.state = 136
                self.parameters()


            self.state = 139
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.VAR:
                self.state = 140
                self.declarevars()


            compiler._add_function(compiler.currentFunction)
            self.state = 144
            self.match(patitoParser.LEFT_CURLY)
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 145
                self.statute()


            self.state = 148
            self.match(patitoParser.RIGHT_CURLY)
            compiler.create_void_endfunc_goto()
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
            self.state = 151
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
            self.state = 153
            localctx._vartypes = self.vartypes()
            self.state = 154
            localctx._ID = self.match(patitoParser.ID)
            compiler.update_parameters((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 156
                self.match(patitoParser.COMMA)
                self.state = 157
                localctx._vartypes = self.vartypes()
                self.state = 158
                localctx._ID = self.match(patitoParser.ID)
                compiler.update_parameters((None if localctx._ID is None else localctx._ID.text), (None if localctx._vartypes is None else self._input.getText(localctx._vartypes.start,localctx._vartypes.stop)))
                self.state = 165
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
            self.state = 166
            self.sexp()
            compiler.topIsLogicOperator()
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 172
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.AND]:
                        self.state = 168
                        localctx._AND = self.match(patitoParser.AND)
                        compiler.addOperator((None if localctx._AND is None else localctx._AND.text))
                        pass
                    elif token in [patitoParser.OR]:
                        self.state = 170
                        localctx._OR = self.match(patitoParser.OR)
                        compiler.addOperator((None if localctx._OR is None else localctx._OR.text))
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 174
                    self.mexp()
                    compiler.topIsLogicOperator() 
                self.state = 181
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
            self.state = 182
            self.exp()
            compiler.topIsComparison()
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.LESS) | (1 << patitoParser.GREATER) | (1 << patitoParser.LESS_EQUAL) | (1 << patitoParser.GREATER_EQUAL) | (1 << patitoParser.EQUAL) | (1 << patitoParser.NOT_EQUAL))) != 0):
                self.state = 196
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [patitoParser.GREATER]:
                    self.state = 184
                    localctx._GREATER = self.match(patitoParser.GREATER)
                    compiler.addOperator((None if localctx._GREATER is None else localctx._GREATER.text))
                    pass
                elif token in [patitoParser.LESS]:
                    self.state = 186
                    localctx._LESS = self.match(patitoParser.LESS)
                    compiler.addOperator((None if localctx._LESS is None else localctx._LESS.text))
                    pass
                elif token in [patitoParser.GREATER_EQUAL]:
                    self.state = 188
                    localctx._GREATER_EQUAL = self.match(patitoParser.GREATER_EQUAL)
                    compiler.addOperator((None if localctx._GREATER_EQUAL is None else localctx._GREATER_EQUAL.text))
                    pass
                elif token in [patitoParser.LESS_EQUAL]:
                    self.state = 190
                    localctx._LESS_EQUAL = self.match(patitoParser.LESS_EQUAL)
                    compiler.addOperator((None if localctx._LESS_EQUAL is None else localctx._LESS_EQUAL.text))
                    pass
                elif token in [patitoParser.NOT_EQUAL]:
                    self.state = 192
                    localctx._NOT_EQUAL = self.match(patitoParser.NOT_EQUAL)
                    compiler.addOperator((None if localctx._NOT_EQUAL is None else localctx._NOT_EQUAL.text))
                    pass
                elif token in [patitoParser.EQUAL]:
                    self.state = 194
                    localctx._EQUAL = self.match(patitoParser.EQUAL)
                    compiler.addOperator((None if localctx._EQUAL is None else localctx._EQUAL.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 198
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
            self.state = 203
            self.term()
            compiler.topIsAddOrSub()
            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 209
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.ADD]:
                        self.state = 205
                        localctx._ADD = self.match(patitoParser.ADD)
                        compiler.addOperator((None if localctx._ADD is None else localctx._ADD.text))
                        pass
                    elif token in [patitoParser.SUB]:
                        self.state = 207
                        localctx._SUB = self.match(patitoParser.SUB)
                        compiler.addOperator((None if localctx._SUB is None else localctx._SUB.text))
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 211
                    self.exp()
                    compiler.topIsAddOrSub() 
                self.state = 218
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
            self.state = 219
            self.factor()
            compiler.topIsMultOrDiv()
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 225
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.MULT]:
                        self.state = 221
                        localctx._MULT = self.match(patitoParser.MULT)
                        compiler.addOperator((None if localctx._MULT is None else localctx._MULT.text))
                        pass
                    elif token in [patitoParser.DIV]:
                        self.state = 223
                        localctx._DIV = self.match(patitoParser.DIV)
                        compiler.addOperator((None if localctx._DIV is None else localctx._DIV.text))
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 227
                    self.term()
                    compiler.topIsMultOrDiv() 
                self.state = 234
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
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 235
                self.constant()
                pass

            elif la_ == 2:
                self.state = 236
                self.match(patitoParser.LEFT_PARENTHESIS)
                compiler.addParenthesis()
                self.state = 238
                self.mexp()
                self.state = 239
                self.match(patitoParser.RIGHT_PARENTHESIS)
                compiler.popParenthesis()
                pass

            elif la_ == 3:
                self.state = 242
                localctx._ID = self.match(patitoParser.ID)
                compiler.addOperandAndType((None if localctx._ID is None else localctx._ID.text))
                self.state = 257
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    pass

                elif la_ == 2:
                    self.state = 245
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.DETERMINANT) | (1 << patitoParser.TRANSPOSE) | (1 << patitoParser.INVERSE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass

                elif la_ == 3:
                    self.state = 246
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 247
                    self.mexp()
                    self.state = 248
                    self.match(patitoParser.RIGHT_BRACKET)
                    pass

                elif la_ == 4:
                    self.state = 250
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 251
                    self.mexp()
                    self.state = 252
                    self.match(patitoParser.RIGHT_BRACKET)
                    self.state = 253
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 254
                    self.mexp()
                    self.state = 255
                    self.match(patitoParser.RIGHT_BRACKET)
                    pass


                pass

            elif la_ == 4:
                self.state = 259
                localctx._ID = self.match(patitoParser.ID)
                compiler.addFuncOperandAndType((None if localctx._ID is None else localctx._ID.text))
                self.state = 261
                self.match(patitoParser.LEFT_PARENTHESIS)
                currentCounter=0
                self.state = 275
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [patitoParser.RIGHT_PARENTHESIS]:
                    pass
                elif token in [patitoParser.SUB, patitoParser.LEFT_PARENTHESIS, patitoParser.CTE_BOOL, patitoParser.CTE_FLOAT, patitoParser.CTE_INT, patitoParser.CTE_CHAR, patitoParser.CTE_STRING, patitoParser.ID]:
                    self.state = 264
                    self.mexp()
                    currentCounter += 1
                    self.state = 272
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==patitoParser.COMMA:
                        self.state = 266
                        self.match(patitoParser.COMMA)
                        self.state = 267
                        self.mexp()
                        currentCounter += 1
                        self.state = 274
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                else:
                    raise NoViableAltException(self)

                compiler.goto_function_quad((None if localctx._ID is None else localctx._ID.text))
                compiler.validate_parameters((None if localctx._ID is None else localctx._ID.text), currentCounter)
                self.state = 279
                self.match(patitoParser.RIGHT_PARENTHESIS)
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
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.RETURN) | (1 << patitoParser.INPUT) | (1 << patitoParser.PRINT) | (1 << patitoParser.IF) | (1 << patitoParser.WHILE) | (1 << patitoParser.FROM) | (1 << patitoParser.ID))) != 0):
                self.state = 290
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 282
                    self.assignation()
                    pass

                elif la_ == 2:
                    self.state = 283
                    self.voidcall()
                    pass

                elif la_ == 3:
                    self.state = 284
                    self.returncall()
                    pass

                elif la_ == 4:
                    self.state = 285
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 286
                    self.write()
                    pass

                elif la_ == 6:
                    self.state = 287
                    self.conditional()
                    pass

                elif la_ == 7:
                    self.state = 288
                    self.whileloop()
                    pass

                elif la_ == 8:
                    self.state = 289
                    self.fromloop()
                    pass


                self.state = 294
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
            self.state = 295
            localctx._ID = self.match(patitoParser.ID)
            compiler.addOperandAndType((None if localctx._ID is None else localctx._ID.text))
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.LEFT_BRACKET:
                self.state = 297
                self.indexvariable()


            self.state = 300
            localctx._ASSIGN = self.match(patitoParser.ASSIGN)
            compiler.addOperator((None if localctx._ASSIGN is None else localctx._ASSIGN.text))
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 302
                    localctx._ID = self.match(patitoParser.ID)
                    compiler.addOperandAndType((None if localctx._ID is None else localctx._ID.text))
                    self.state = 305
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==patitoParser.LEFT_BRACKET:
                        self.state = 304
                        self.indexvariable()


                    self.state = 307
                    localctx._ASSIGN = self.match(patitoParser.ASSIGN)
                    compiler.addOperator((None if localctx._ASSIGN is None else localctx._ASSIGN.text)) 
                self.state = 313
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 314
                localctx._ID = self.match(patitoParser.ID)
                compiler.addOperandAndType((None if localctx._ID is None else localctx._ID.text))
                pass

            elif la_ == 2:
                self.state = 316
                self.mexp()
                pass


            self.state = 319
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
            self.state = 322
            localctx._ID = self.match(patitoParser.ID)
            compiler.validate_void_function((None if localctx._ID is None else localctx._ID.text))
            self.state = 324
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [patitoParser.RIGHT_PARENTHESIS]:
                pass
            elif token in [patitoParser.SUB, patitoParser.LEFT_PARENTHESIS, patitoParser.CTE_BOOL, patitoParser.CTE_FLOAT, patitoParser.CTE_INT, patitoParser.CTE_CHAR, patitoParser.CTE_STRING, patitoParser.ID]:
                self.state = 326
                self.mexp()
                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==patitoParser.COMMA:
                    self.state = 327
                    self.match(patitoParser.COMMA)
                    self.state = 328
                    self.mexp()
                    self.state = 333
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 336
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 337
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
            self.state = 339
            self.match(patitoParser.RETURN)
            self.state = 340
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 341
            self.mexp()
            self.state = 342
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 343
            self.match(patitoParser.SEMICOLON)
            compiler.create_return_endfunc_goto()
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
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 346
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 347
                self.mexp()
                self.state = 348
                self.match(patitoParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.state = 350
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 351
                self.mexp()
                self.state = 352
                self.match(patitoParser.RIGHT_BRACKET)
                self.state = 353
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 354
                self.mexp()
                self.state = 355
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
            self.state = 359
            self.match(patitoParser.INPUT)
            self.state = 360
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 361
            localctx.var_id = self.match(patitoParser.ID)
            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.LEFT_BRACKET:
                self.state = 362
                self.indexvariable()


            compiler.generateReadQuad((None if localctx.var_id is None else localctx.var_id.text))
            self.state = 374
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 366
                self.match(patitoParser.COMMA)
                self.state = 367
                localctx.var_id2 = self.match(patitoParser.ID)
                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==patitoParser.LEFT_BRACKET:
                    self.state = 368
                    self.indexvariable()


                compiler.generateReadQuad((None if localctx.var_id2 is None else localctx.var_id2.text))
                self.state = 376
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 377
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 378
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
            self.state = 380
            self.match(patitoParser.PRINT)
            self.state = 381
            self.match(patitoParser.LEFT_PARENTHESIS)

            self.state = 382
            self.mexp()
            compiler.generateWriteQuad()
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 385
                self.match(patitoParser.COMMA)

                self.state = 386
                self.mexp()
                compiler.generateWriteQuad()
                self.state = 393
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 394
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 395
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
            self.state = 397
            self.match(patitoParser.IF)
            self.state = 398
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 399
            self.mexp()
            self.state = 400
            self.match(patitoParser.RIGHT_PARENTHESIS)
            compiler.generateIfQuad()
            self.state = 402
            self.match(patitoParser.THEN)
            self.state = 403
            self.match(patitoParser.LEFT_CURLY)
            self.state = 404
            self.statute()
            self.state = 405
            self.match(patitoParser.RIGHT_CURLY)
            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.ELSE:
                self.state = 406
                self.match(patitoParser.ELSE)
                compiler.generateGoToQuad()
                self.state = 408
                self.match(patitoParser.LEFT_CURLY)
                self.state = 409
                self.statute()
                self.state = 410
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
            self.state = 416
            self.match(patitoParser.WHILE)
            self.state = 417
            self.match(patitoParser.LEFT_PARENTHESIS)
            compiler.generateWhileBeforeCheck()
            self.state = 419
            self.mexp()
            self.state = 420
            self.match(patitoParser.RIGHT_PARENTHESIS)
            compiler.generateWhileAfterCheck()
            self.state = 422
            self.match(patitoParser.DO)
            self.state = 423
            self.match(patitoParser.LEFT_CURLY)
            self.state = 424
            self.statute()
            compiler.generateWhileEnd()
            self.state = 426
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
        self.enterRule(localctx, 48, self.RULE_fromloop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(patitoParser.FROM)
            self.state = 429
            localctx._ID = self.match(patitoParser.ID)
            compiler.addFromVarOperand((None if localctx._ID is None else localctx._ID.text))
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.LEFT_BRACKET:
                self.state = 431
                self.indexvariable()


            self.state = 434
            localctx._ASSIGN = self.match(patitoParser.ASSIGN)
            compiler.addOperator((None if localctx._ASSIGN is None else localctx._ASSIGN.text))
            self.state = 436
            self.mexp()
            compiler.generateAssignQuads()
            self.state = 438
            self.match(patitoParser.TO)
            compiler.generateFromBeforeCheck()
            self.state = 440
            self.mexp()
            compiler.generateFromAfterCheck()
            self.state = 442
            self.match(patitoParser.DO)
            self.state = 443
            self.match(patitoParser.LEFT_CURLY)
            self.state = 444
            self.statute()
            self.state = 445
            self.match(patitoParser.RIGHT_CURLY)
            compiler.generateEndFromQuad()
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
            self.state = 448
            self.match(patitoParser.MAIN)
            compiler.currentFunction=Function("main", "void", [], {})
            self.state = 450
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 451
            self.match(patitoParser.RIGHT_PARENTHESIS)
            compiler._add_function(compiler.currentFunction)
            self.state = 453
            self.match(patitoParser.LEFT_CURLY)
            compiler.fill_goto_main_quad()
            self.state = 455
            self.statute()
            self.state = 456
            self.match(patitoParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





