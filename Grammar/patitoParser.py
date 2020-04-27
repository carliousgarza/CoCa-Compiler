# Generated from patito.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys
from Compiler.compiler import *
from Compiler.function import *
from Compiler.variable import *
from Compiler.interpreter import *
interpreter = Interpreter()
compiler = Compiler()

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38")
        buf.write("\u017c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\6\3@\n\3\r\3\16\3A\3\4\3\4\3\4\3\4\3\4\7\4I\n")
        buf.write("\4\f\4\16\4L\13\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7^\n\7\3\b\6\ba\n\b\r\b")
        buf.write("\16\bb\3\t\3\t\3\t\5\th\n\t\3\t\3\t\3\t\5\tm\n\t\3\t\3")
        buf.write("\t\5\tq\n\t\3\t\3\t\5\tu\n\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\7\n\177\n\n\f\n\16\n\u0082\13\n\3\13\3\13\3\13")
        buf.write("\7\13\u0087\n\13\f\13\16\13\u008a\13\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\5\f\u0091\n\f\3\f\7\f\u0094\n\f\f\f\16\f\u0097")
        buf.write("\13\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\5\r\u00a6\n\r\3\r\5\r\u00a9\n\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\5\16\u00b0\n\16\3\16\7\16\u00b3\n\16\f\16\16")
        buf.write("\16\u00b6\13\16\3\17\3\17\3\17\3\17\3\17\5\17\u00bd\n")
        buf.write("\17\3\17\7\17\u00c0\n\17\f\17\16\17\u00c3\13\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\7\20\u00e0\n\20\f\20\16\20\u00e3")
        buf.write("\13\20\5\20\u00e5\n\20\3\20\3\20\5\20\u00e9\n\20\5\20")
        buf.write("\u00eb\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7")
        buf.write("\21\u00f5\n\21\f\21\16\21\u00f8\13\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22")
        buf.write("\u0107\n\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\7\23\u0113\n\23\f\23\16\23\u0116\13\23\5\23\u0118")
        buf.write("\n\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\5\25\u0130\n\25\3\26\3\26\3\26\3\26\3\26\7\26\u0137")
        buf.write("\n\26\f\26\16\26\u013a\13\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u0143\n\27\3\27\3\27\3\27\5\27\u0148\n")
        buf.write("\27\7\27\u014a\n\27\f\27\16\27\u014d\13\27\3\27\3\27\3")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\5\30\u015f\n\30\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\2\2\34\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\2\5\3\2-\61\3\2\62\66\3\2\31\33")
        buf.write("\2\u0193\2\66\3\2\2\2\4=\3\2\2\2\6C\3\2\2\2\bO\3\2\2\2")
        buf.write("\nQ\3\2\2\2\fS\3\2\2\2\16`\3\2\2\2\20d\3\2\2\2\22x\3\2")
        buf.write("\2\2\24\u0083\3\2\2\2\26\u008b\3\2\2\2\30\u0098\3\2\2")
        buf.write("\2\32\u00aa\3\2\2\2\34\u00b7\3\2\2\2\36\u00ea\3\2\2\2")
        buf.write(" \u00f6\3\2\2\2\"\u00f9\3\2\2\2$\u010c\3\2\2\2&\u011c")
        buf.write("\3\2\2\2(\u0122\3\2\2\2*\u0131\3\2\2\2,\u013e\3\2\2\2")
        buf.write(".\u0151\3\2\2\2\60\u0160\3\2\2\2\62\u0169\3\2\2\2\64\u0174")
        buf.write("\3\2\2\2\66\67\7\37\2\2\678\78\2\289\7\36\2\29:\5\4\3")
        buf.write("\2:;\5\16\b\2;<\5\64\33\2<\3\3\2\2\2=?\7,\2\2>@\5\6\4")
        buf.write("\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2B\5\3\2\2\2")
        buf.write("CD\5\b\5\2DE\7\35\2\2EJ\5\f\7\2FG\7\34\2\2GI\5\f\7\2H")
        buf.write("F\3\2\2\2IL\3\2\2\2JH\3\2\2\2JK\3\2\2\2KM\3\2\2\2LJ\3")
        buf.write("\2\2\2MN\7\36\2\2N\7\3\2\2\2OP\t\2\2\2P\t\3\2\2\2QR\t")
        buf.write("\3\2\2R\13\3\2\2\2S]\78\2\2TU\7\25\2\2UV\7\64\2\2V^\7")
        buf.write("\26\2\2WX\7\25\2\2XY\7\64\2\2YZ\7\26\2\2Z[\7\25\2\2[\\")
        buf.write("\7\64\2\2\\^\7\26\2\2]T\3\2\2\2]W\3\2\2\2]^\3\2\2\2^\r")
        buf.write("\3\2\2\2_a\5\20\t\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3")
        buf.write("\2\2\2c\17\3\2\2\2dg\7!\2\2eh\5\b\5\2fh\7\67\2\2ge\3\2")
        buf.write("\2\2gf\3\2\2\2hi\3\2\2\2ij\78\2\2jl\7\23\2\2km\5\22\n")
        buf.write("\2lk\3\2\2\2lm\3\2\2\2mn\3\2\2\2np\7\24\2\2oq\5\4\3\2")
        buf.write("po\3\2\2\2pq\3\2\2\2qr\3\2\2\2rt\7\27\2\2su\5 \21\2ts")
        buf.write("\3\2\2\2tu\3\2\2\2uv\3\2\2\2vw\7\30\2\2w\21\3\2\2\2xy")
        buf.write("\5\b\5\2y\u0080\78\2\2z{\7\34\2\2{|\5\b\5\2|}\78\2\2}")
        buf.write("\177\3\2\2\2~z\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2\2")
        buf.write("\2\u0080\u0081\3\2\2\2\u0081\23\3\2\2\2\u0082\u0080\3")
        buf.write("\2\2\2\u0083\u0088\5\26\f\2\u0084\u0085\7\f\2\2\u0085")
        buf.write("\u0087\5\26\f\2\u0086\u0084\3\2\2\2\u0087\u008a\3\2\2")
        buf.write("\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\25\3")
        buf.write("\2\2\2\u008a\u0088\3\2\2\2\u008b\u0095\5\30\r\2\u008c")
        buf.write("\u008d\7\r\2\2\u008d\u0091\b\f\1\2\u008e\u008f\7\16\2")
        buf.write("\2\u008f\u0091\b\f\1\2\u0090\u008c\3\2\2\2\u0090\u008e")
        buf.write("\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0094\5\30\r\2\u0093")
        buf.write("\u0090\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\27\3\2\2\2\u0097\u0095\3\2")
        buf.write("\2\2\u0098\u00a8\5\32\16\2\u0099\u009a\7\7\2\2\u009a\u00a6")
        buf.write("\b\r\1\2\u009b\u009c\7\6\2\2\u009c\u00a6\b\r\1\2\u009d")
        buf.write("\u009e\7\t\2\2\u009e\u00a6\b\r\1\2\u009f\u00a0\7\b\2\2")
        buf.write("\u00a0\u00a6\b\r\1\2\u00a1\u00a2\7\13\2\2\u00a2\u00a6")
        buf.write("\b\r\1\2\u00a3\u00a4\7\n\2\2\u00a4\u00a6\b\r\1\2\u00a5")
        buf.write("\u0099\3\2\2\2\u00a5\u009b\3\2\2\2\u00a5\u009d\3\2\2\2")
        buf.write("\u00a5\u009f\3\2\2\2\u00a5\u00a1\3\2\2\2\u00a5\u00a3\3")
        buf.write("\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a9\5\32\16\2\u00a8")
        buf.write("\u00a5\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\31\3\2\2\2\u00aa")
        buf.write("\u00b4\5\34\17\2\u00ab\u00ac\7\17\2\2\u00ac\u00b0\b\16")
        buf.write("\1\2\u00ad\u00ae\7\20\2\2\u00ae\u00b0\b\16\1\2\u00af\u00ab")
        buf.write("\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1")
        buf.write("\u00b3\5\34\17\2\u00b2\u00af\3\2\2\2\u00b3\u00b6\3\2\2")
        buf.write("\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\33\3")
        buf.write("\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00c1\5\36\20\2\u00b8")
        buf.write("\u00b9\7\21\2\2\u00b9\u00bd\b\17\1\2\u00ba\u00bb\7\22")
        buf.write("\2\2\u00bb\u00bd\b\17\1\2\u00bc\u00b8\3\2\2\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c0\5\36\20\2\u00bf")
        buf.write("\u00bc\3\2\2\2\u00c0\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2")
        buf.write("\u00c1\u00c2\3\2\2\2\u00c2\35\3\2\2\2\u00c3\u00c1\3\2")
        buf.write("\2\2\u00c4\u00eb\5\n\6\2\u00c5\u00c6\7\23\2\2\u00c6\u00c7")
        buf.write("\b\20\1\2\u00c7\u00c8\5\24\13\2\u00c8\u00c9\7\24\2\2\u00c9")
        buf.write("\u00ca\b\20\1\2\u00ca\u00eb\3\2\2\2\u00cb\u00e8\78\2\2")
        buf.write("\u00cc\u00e9\3\2\2\2\u00cd\u00e9\t\4\2\2\u00ce\u00cf\7")
        buf.write("\25\2\2\u00cf\u00d0\5\26\f\2\u00d0\u00d1\7\26\2\2\u00d1")
        buf.write("\u00e9\3\2\2\2\u00d2\u00d3\7\25\2\2\u00d3\u00d4\5\26\f")
        buf.write("\2\u00d4\u00d5\7\26\2\2\u00d5\u00d6\7\25\2\2\u00d6\u00d7")
        buf.write("\5\26\f\2\u00d7\u00d8\7\26\2\2\u00d8\u00e9\3\2\2\2\u00d9")
        buf.write("\u00da\7\23\2\2\u00da\u00e4\b\20\1\2\u00db\u00e5\3\2\2")
        buf.write("\2\u00dc\u00e1\5\24\13\2\u00dd\u00de\7\34\2\2\u00de\u00e0")
        buf.write("\5\24\13\2\u00df\u00dd\3\2\2\2\u00e0\u00e3\3\2\2\2\u00e1")
        buf.write("\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e5\3\2\2\2")
        buf.write("\u00e3\u00e1\3\2\2\2\u00e4\u00db\3\2\2\2\u00e4\u00dc\3")
        buf.write("\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e7\7\24\2\2\u00e7")
        buf.write("\u00e9\b\20\1\2\u00e8\u00cc\3\2\2\2\u00e8\u00cd\3\2\2")
        buf.write("\2\u00e8\u00ce\3\2\2\2\u00e8\u00d2\3\2\2\2\u00e8\u00d9")
        buf.write("\3\2\2\2\u00e9\u00eb\3\2\2\2\u00ea\u00c4\3\2\2\2\u00ea")
        buf.write("\u00c5\3\2\2\2\u00ea\u00cb\3\2\2\2\u00eb\37\3\2\2\2\u00ec")
        buf.write("\u00f5\5\"\22\2\u00ed\u00f5\5$\23\2\u00ee\u00f5\5&\24")
        buf.write("\2\u00ef\u00f5\5*\26\2\u00f0\u00f5\5,\27\2\u00f1\u00f5")
        buf.write("\5.\30\2\u00f2\u00f5\5\60\31\2\u00f3\u00f5\5\62\32\2\u00f4")
        buf.write("\u00ec\3\2\2\2\u00f4\u00ed\3\2\2\2\u00f4\u00ee\3\2\2\2")
        buf.write("\u00f4\u00ef\3\2\2\2\u00f4\u00f0\3\2\2\2\u00f4\u00f1\3")
        buf.write("\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5\u00f8")
        buf.write("\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7")
        buf.write("!\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f9\u0106\78\2\2\u00fa")
        buf.write("\u0107\3\2\2\2\u00fb\u00fc\7\25\2\2\u00fc\u00fd\5\26\f")
        buf.write("\2\u00fd\u00fe\7\26\2\2\u00fe\u0107\3\2\2\2\u00ff\u0100")
        buf.write("\7\25\2\2\u0100\u0101\5\26\f\2\u0101\u0102\7\26\2\2\u0102")
        buf.write("\u0103\7\25\2\2\u0103\u0104\5\26\f\2\u0104\u0105\7\26")
        buf.write("\2\2\u0105\u0107\3\2\2\2\u0106\u00fa\3\2\2\2\u0106\u00fb")
        buf.write("\3\2\2\2\u0106\u00ff\3\2\2\2\u0107\u0108\3\2\2\2\u0108")
        buf.write("\u0109\7\f\2\2\u0109\u010a\5\24\13\2\u010a\u010b\7\36")
        buf.write("\2\2\u010b#\3\2\2\2\u010c\u010d\78\2\2\u010d\u0117\7\23")
        buf.write("\2\2\u010e\u0118\3\2\2\2\u010f\u0114\5\26\f\2\u0110\u0111")
        buf.write("\7\34\2\2\u0111\u0113\5\26\f\2\u0112\u0110\3\2\2\2\u0113")
        buf.write("\u0116\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2")
        buf.write("\u0115\u0118\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u010e\3")
        buf.write("\2\2\2\u0117\u010f\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011a")
        buf.write("\7\24\2\2\u011a\u011b\7\36\2\2\u011b%\3\2\2\2\u011c\u011d")
        buf.write("\7\"\2\2\u011d\u011e\7\23\2\2\u011e\u011f\5\24\13\2\u011f")
        buf.write("\u0120\7\24\2\2\u0120\u0121\7\36\2\2\u0121\'\3\2\2\2\u0122")
        buf.write("\u012f\78\2\2\u0123\u0130\3\2\2\2\u0124\u0125\7\25\2\2")
        buf.write("\u0125\u0126\5\26\f\2\u0126\u0127\7\26\2\2\u0127\u0130")
        buf.write("\3\2\2\2\u0128\u0129\7\25\2\2\u0129\u012a\5\26\f\2\u012a")
        buf.write("\u012b\7\26\2\2\u012b\u012c\7\25\2\2\u012c\u012d\5\26")
        buf.write("\f\2\u012d\u012e\7\26\2\2\u012e\u0130\3\2\2\2\u012f\u0123")
        buf.write("\3\2\2\2\u012f\u0124\3\2\2\2\u012f\u0128\3\2\2\2\u0130")
        buf.write(")\3\2\2\2\u0131\u0132\7#\2\2\u0132\u0133\7\23\2\2\u0133")
        buf.write("\u0138\5(\25\2\u0134\u0135\7\34\2\2\u0135\u0137\5(\25")
        buf.write("\2\u0136\u0134\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136")
        buf.write("\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013b\3\2\2\2\u013a")
        buf.write("\u0138\3\2\2\2\u013b\u013c\7\24\2\2\u013c\u013d\7\36\2")
        buf.write("\2\u013d+\3\2\2\2\u013e\u013f\7$\2\2\u013f\u0142\7\23")
        buf.write("\2\2\u0140\u0143\5\24\13\2\u0141\u0143\7\66\2\2\u0142")
        buf.write("\u0140\3\2\2\2\u0142\u0141\3\2\2\2\u0143\u014b\3\2\2\2")
        buf.write("\u0144\u0147\7\34\2\2\u0145\u0148\5\24\13\2\u0146\u0148")
        buf.write("\7\66\2\2\u0147\u0145\3\2\2\2\u0147\u0146\3\2\2\2\u0148")
        buf.write("\u014a\3\2\2\2\u0149\u0144\3\2\2\2\u014a\u014d\3\2\2\2")
        buf.write("\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014e\3")
        buf.write("\2\2\2\u014d\u014b\3\2\2\2\u014e\u014f\7\24\2\2\u014f")
        buf.write("\u0150\7\36\2\2\u0150-\3\2\2\2\u0151\u0152\7%\2\2\u0152")
        buf.write("\u0153\7\23\2\2\u0153\u0154\5\26\f\2\u0154\u0155\7\24")
        buf.write("\2\2\u0155\u0156\7&\2\2\u0156\u0157\7\27\2\2\u0157\u0158")
        buf.write("\5 \21\2\u0158\u015e\7\30\2\2\u0159\u015a\7\'\2\2\u015a")
        buf.write("\u015b\7\27\2\2\u015b\u015c\5 \21\2\u015c\u015d\7\30\2")
        buf.write("\2\u015d\u015f\3\2\2\2\u015e\u0159\3\2\2\2\u015e\u015f")
        buf.write("\3\2\2\2\u015f/\3\2\2\2\u0160\u0161\7(\2\2\u0161\u0162")
        buf.write("\7\23\2\2\u0162\u0163\5\26\f\2\u0163\u0164\7\24\2\2\u0164")
        buf.write("\u0165\7)\2\2\u0165\u0166\7\27\2\2\u0166\u0167\5 \21\2")
        buf.write("\u0167\u0168\7\30\2\2\u0168\61\3\2\2\2\u0169\u016a\7*")
        buf.write("\2\2\u016a\u016b\5(\25\2\u016b\u016c\7\f\2\2\u016c\u016d")
        buf.write("\5\26\f\2\u016d\u016e\7+\2\2\u016e\u016f\5\26\f\2\u016f")
        buf.write("\u0170\7)\2\2\u0170\u0171\7\27\2\2\u0171\u0172\5 \21\2")
        buf.write("\u0172\u0173\7\30\2\2\u0173\63\3\2\2\2\u0174\u0175\7 ")
        buf.write("\2\2\u0175\u0176\7\23\2\2\u0176\u0177\7\24\2\2\u0177\u0178")
        buf.write("\7\27\2\2\u0178\u0179\5 \21\2\u0179\u017a\7\30\2\2\u017a")
        buf.write("\65\3\2\2\2#AJ]bglpt\u0080\u0088\u0090\u0095\u00a5\u00a8")
        buf.write("\u00af\u00b4\u00bc\u00c1\u00e1\u00e4\u00e8\u00ea\u00f4")
        buf.write("\u00f6\u0106\u0114\u0117\u012f\u0138\u0142\u0147\u014b")
        buf.write("\u015e")
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
    RULE_varindividual = 5
    RULE_functions = 6
    RULE_function = 7
    RULE_parameters = 8
    RULE_hexp = 9
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
                   "varindividual", "functions", "function", "parameters",
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
        self.checkVersion("4.7.1")
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
            self.state = 56
            self.functions()
            self.state = 57
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
            self.state = 59
            self.match(patitoParser.VAR)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.variables()
                self.state = 63
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

        def vartypes(self):
            return self.getTypedRuleContext(patitoParser.VartypesContext,0)


        def COLON(self):
            return self.getToken(patitoParser.COLON, 0)

        def varindividual(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.VarindividualContext)
            else:
                return self.getTypedRuleContext(patitoParser.VarindividualContext,i)


        def SEMICOLON(self):
            return self.getToken(patitoParser.SEMICOLON, 0)

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
            self.state = 65
            self.vartypes()
            self.state = 66
            self.match(patitoParser.COLON)
            self.state = 67
            self.varindividual()
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                interpreter.addVarType(interpreter.getLastVarType())
                self.state = 68
                self.match(patitoParser.COMMA)
                self.state = 69
                self.varindividual()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
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
            self.state = 77
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.BOOL) | (1 << patitoParser.INT) | (1 << patitoParser.FLOAT) | (1 << patitoParser.STRING) | (1 << patitoParser.CHAR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                if(_la in [patitoParser.INT]):
                    interpreter.addVarType('int')
                elif(_la in [patitoParser.FLOAT]):
                    interpreter.addVarType('float')
                elif(_la in [patitoParser.CHAR]):
                    interpreter.addVarType('char')
                elif(_la in [patitoParser.BOOL]):
                    interpreter.addVarType('bool')
                elif(_la in [patitoParser.STRING]):
                    interpreter.addVarType('string')                                                              
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.CTE_BOOL) | (1 << patitoParser.CTE_FLOAT) | (1 << patitoParser.CTE_INT) | (1 << patitoParser.CTE_CHAR) | (1 << patitoParser.CTE_STRING))) != 0)):
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

    class VarindividualContext(ParserRuleContext):

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
            return patitoParser.RULE_varindividual

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarindividual" ):
                listener.enterVarindividual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarindividual" ):
                listener.exitVarindividual(self)




    def varindividual(self):

        localctx = patitoParser.VarindividualContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varindividual)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(patitoParser.ID)
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            interpreter.addOperand(str(localctx.ID()))
            if la_ == 1:
                self.state = 82
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 83
                self.match(patitoParser.CTE_INT)
                self.state = 84
                self.match(patitoParser.RIGHT_BRACKET)

            elif la_ == 2:
                self.state = 85
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 86
                self.match(patitoParser.CTE_INT)
                self.state = 87
                self.match(patitoParser.RIGHT_BRACKET)
                self.state = 88
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 89
                self.match(patitoParser.CTE_INT)
                self.state = 90
                self.match(patitoParser.RIGHT_BRACKET)


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
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 93
                self.function()
                self.state = 96
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

        def FUNCTION(self):
            return self.getToken(patitoParser.FUNCTION, 0)

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

        def vartypes(self):
            return self.getTypedRuleContext(patitoParser.VartypesContext,0)


        def VOID(self):
            return self.getToken(patitoParser.VOID, 0)

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
            self.state = 98
            self.match(patitoParser.FUNCTION)
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [patitoParser.BOOL, patitoParser.INT, patitoParser.FLOAT, patitoParser.STRING, patitoParser.CHAR]:
                self.state = 99
                self.vartypes()
                pass
            elif token in [patitoParser.VOID]:
                self.state = 100
                self.match(patitoParser.VOID)
                pass
            else:
                raise NoViableAltException(self)
            
            self.state = 103
            self.match(patitoParser.ID)
            self.state = 104
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)

            #Function ID
            fid = (localctx.ID())

            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.BOOL) | (1 << patitoParser.INT) | (1 << patitoParser.FLOAT) | (1 << patitoParser.STRING) | (1 << patitoParser.CHAR))) != 0):
                self.state = 105
                self.parameters()


            self.state = 108
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)

            #Function Parameters
            parserParameters = (localctx.parameters())
            parameters = get_parameters(parserParameters)

            if _la==patitoParser.VAR:
                self.state = 109
                self.declarevars()


            self.state = 112
            self.match(patitoParser.LEFT_CURLY)
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)

            #Function Variables
            parserVariables = (localctx.declarevars())
            variables = get_variables(parserVariables)

            #Function Type
            vartype = get_vartype(localctx) #type

            #Build Function object and send to compiler
            func = Function(fid, vartype, parameters, variables)
            compiler._add_function(func)

            if la_ == 1:
                self.state = 113
                self.statute()


            self.state = 116
            self.match(patitoParser.RIGHT_CURLY)
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
            self.state = 118
            self.vartypes()
            self.state = 119
            self.match(patitoParser.ID)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 120
                self.match(patitoParser.COMMA)
                self.state = 121
                self.vartypes()
                self.state = 122
                self.match(patitoParser.ID)
                self.state = 128
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
        self.enterRule(localctx, 18, self.RULE_hexp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.mexp()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.ASSIGN:
                self.state = 130
                self.match(patitoParser.ASSIGN)
                self.state = 131
                self.mexp()
                self.state = 136
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

        def sexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.SexpContext)
            else:
                return self.getTypedRuleContext(patitoParser.SexpContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.sexp()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.AND or _la==patitoParser.OR:
                self.state = 142
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [patitoParser.AND]:
                    self.state = 138
                    localctx._AND = self.match(patitoParser.AND)
                    interpreter.addOperator((None if localctx._AND is None else localctx._AND.text))
                    pass
                elif token in [patitoParser.OR]:
                    self.state = 140
                    localctx._OR = self.match(patitoParser.OR)
                    interpreter.addOperator((None if localctx._OR is None else localctx._OR.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 144
                self.sexp()
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

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.ExpContext)
            else:
                return self.getTypedRuleContext(patitoParser.ExpContext,i)


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
            self.state = 150
            self.exp()
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.LESS) | (1 << patitoParser.GREATER) | (1 << patitoParser.LESS_EQUAL) | (1 << patitoParser.GREATER_EQUAL) | (1 << patitoParser.EQUAL) | (1 << patitoParser.NOT_EQUAL))) != 0):
                self.state = 163
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [patitoParser.GREATER]:
                    self.state = 151
                    localctx._GREATER = self.match(patitoParser.GREATER)
                    interpreter.addOperator((None if localctx._GREATER is None else localctx._GREATER.text))
                    pass
                elif token in [patitoParser.LESS]:
                    self.state = 153
                    localctx._LESS = self.match(patitoParser.LESS)
                    interpreter.addOperator((None if localctx._LESS is None else localctx._LESS.text))
                    pass
                elif token in [patitoParser.GREATER_EQUAL]:
                    self.state = 155
                    localctx._GREATER_EQUAL = self.match(patitoParser.GREATER_EQUAL)
                    interpreter.addOperator((None if localctx._GREATER_EQUAL is None else localctx._GREATER_EQUAL.text))
                    pass
                elif token in [patitoParser.LESS_EQUAL]:
                    self.state = 157
                    localctx._LESS_EQUAL = self.match(patitoParser.LESS_EQUAL)
                    interpreter.addOperator((None if localctx._LESS_EQUAL is None else localctx._LESS_EQUAL.text))
                    pass
                elif token in [patitoParser.NOT_EQUAL]:
                    self.state = 159
                    localctx._NOT_EQUAL = self.match(patitoParser.NOT_EQUAL)
                    interpreter.addOperator((None if localctx._NOT_EQUAL is None else localctx._NOT_EQUAL.text))
                    pass
                elif token in [patitoParser.EQUAL]:
                    self.state = 161
                    localctx._EQUAL = self.match(patitoParser.EQUAL)
                    interpreter.addOperator((None if localctx._EQUAL is None else localctx._EQUAL.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 165
                self.exp()


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

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.TermContext)
            else:
                return self.getTypedRuleContext(patitoParser.TermContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.term()
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.ADD or _la==patitoParser.SUB:
                self.state = 173
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [patitoParser.ADD]:
                    self.state = 169
                    localctx._ADD = self.match(patitoParser.ADD)
                    interpreter.addOperator((None if localctx._ADD is None else localctx._ADD.text))
                    pass
                elif token in [patitoParser.SUB]:
                    self.state = 171
                    localctx._SUB = self.match(patitoParser.SUB)
                    interpreter.addOperator((None if localctx._SUB is None else localctx._SUB.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 175
                self.term()
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.FactorContext)
            else:
                return self.getTypedRuleContext(patitoParser.FactorContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.factor()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.MULT or _la==patitoParser.DIV:
                self.state = 186
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [patitoParser.MULT]:
                    self.state = 182
                    localctx._MULT = self.match(patitoParser.MULT)
                    interpreter.addOperator((None if localctx._MULT is None else localctx._MULT.text))
                    pass
                elif token in [patitoParser.DIV]:
                    self.state = 184
                    localctx._DIV = self.match(patitoParser.DIV)
                    interpreter.addOperator((None if localctx._DIV is None else localctx._DIV.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 188
                self.factor()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def constant(self):
            return self.getTypedRuleContext(patitoParser.ConstantContext,0)


        def LEFT_PARENTHESIS(self):
            return self.getToken(patitoParser.LEFT_PARENTHESIS, 0)

        def hexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.HexpContext)
            else:
                return self.getTypedRuleContext(patitoParser.HexpContext,i)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(patitoParser.RIGHT_PARENTHESIS, 0)

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
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [patitoParser.CTE_BOOL, patitoParser.CTE_FLOAT, patitoParser.CTE_INT, patitoParser.CTE_CHAR, patitoParser.CTE_STRING]:
                self.state = 194
                self.constant()
                pass
            elif token in [patitoParser.LEFT_PARENTHESIS]:
                self.state = 195
                self.match(patitoParser.LEFT_PARENTHESIS)
                interpreter.addParenthesis()
                self.state = 197
                self.hexp()
                self.state = 198
                self.match(patitoParser.RIGHT_PARENTHESIS)
                interpreter.popParenthesis()
                pass
            elif token in [patitoParser.ID]:
                self.state = 201
                self.match(patitoParser.ID)
                self.state = 230
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    pass

                elif la_ == 2:
                    self.state = 203
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.DETERMINANT) | (1 << patitoParser.TRANSPOSE) | (1 << patitoParser.INVERSE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass

                elif la_ == 3:
                    self.state = 204
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 205
                    self.mexp()
                    self.state = 206
                    self.match(patitoParser.RIGHT_BRACKET)
                    pass

                elif la_ == 4:
                    self.state = 208
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 209
                    self.mexp()
                    self.state = 210
                    self.match(patitoParser.RIGHT_BRACKET)
                    self.state = 211
                    self.match(patitoParser.LEFT_BRACKET)
                    self.state = 212
                    self.mexp()
                    self.state = 213
                    self.match(patitoParser.RIGHT_BRACKET)
                    pass

                elif la_ == 5:
                    self.state = 215
                    self.match(patitoParser.LEFT_PARENTHESIS)
                    interpreter.addParenthesis()
                    self.state = 226
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [patitoParser.RIGHT_PARENTHESIS]:
                        pass
                    elif token in [patitoParser.LEFT_PARENTHESIS, patitoParser.CTE_BOOL, patitoParser.CTE_FLOAT, patitoParser.CTE_INT, patitoParser.CTE_CHAR, patitoParser.CTE_STRING, patitoParser.ID]:
                        self.state = 218
                        self.hexp()
                        self.state = 223
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==patitoParser.COMMA:
                            self.state = 219
                            self.match(patitoParser.COMMA)
                            self.state = 220
                            self.hexp()
                            self.state = 225
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 228
                    self.match(patitoParser.RIGHT_PARENTHESIS)
                    interpreter.popParenthesis()
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
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << patitoParser.RETURN) | (1 << patitoParser.INPUT) | (1 << patitoParser.PRINT) | (1 << patitoParser.IF) | (1 << patitoParser.WHILE) | (1 << patitoParser.FROM) | (1 << patitoParser.ID))) != 0):
                self.state = 242
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 234
                    self.assignation()
                    pass

                elif la_ == 2:
                    self.state = 235
                    self.voidcall()
                    pass

                elif la_ == 3:
                    self.state = 236
                    self.returncall()
                    pass

                elif la_ == 4:
                    self.state = 237
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 238
                    self.write()
                    pass

                elif la_ == 6:
                    self.state = 239
                    self.conditional()
                    pass

                elif la_ == 7:
                    self.state = 240
                    self.whileloop()
                    pass

                elif la_ == 8:
                    self.state = 241
                    self.fromloop()
                    pass


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

    class AssignationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
        self.enterRule(localctx, 32, self.RULE_assignation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(patitoParser.ID)
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                self.state = 249
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 250
                self.mexp()
                self.state = 251
                self.match(patitoParser.RIGHT_BRACKET)
                pass

            elif la_ == 3:
                self.state = 253
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 254
                self.mexp()
                self.state = 255
                self.match(patitoParser.RIGHT_BRACKET)
                self.state = 256
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 257
                self.mexp()
                self.state = 258
                self.match(patitoParser.RIGHT_BRACKET)
                pass


            self.state = 262
            self.match(patitoParser.ASSIGN)
            self.state = 263
            self.hexp()
            self.state = 264
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
        self.enterRule(localctx, 34, self.RULE_voidcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(patitoParser.ID)
            self.state = 267
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [patitoParser.RIGHT_PARENTHESIS]:
                pass
            elif token in [patitoParser.LEFT_PARENTHESIS, patitoParser.CTE_BOOL, patitoParser.CTE_FLOAT, patitoParser.CTE_INT, patitoParser.CTE_CHAR, patitoParser.CTE_STRING, patitoParser.ID]:
                self.state = 269
                self.mexp()
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==patitoParser.COMMA:
                    self.state = 270
                    self.match(patitoParser.COMMA)
                    self.state = 271
                    self.mexp()
                    self.state = 276
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 279
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 280
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

        def hexp(self):
            return self.getTypedRuleContext(patitoParser.HexpContext,0)


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
            self.state = 282
            self.match(patitoParser.RETURN)
            self.state = 283
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 284
            self.hexp()
            self.state = 285
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 286
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
        self.enterRule(localctx, 38, self.RULE_indexvariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(patitoParser.ID)
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                self.state = 290
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 291
                self.mexp()
                self.state = 292
                self.match(patitoParser.RIGHT_BRACKET)
                pass

            elif la_ == 3:
                self.state = 294
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 295
                self.mexp()
                self.state = 296
                self.match(patitoParser.RIGHT_BRACKET)
                self.state = 297
                self.match(patitoParser.LEFT_BRACKET)
                self.state = 298
                self.mexp()
                self.state = 299
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
        self.enterRule(localctx, 40, self.RULE_read)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(patitoParser.INPUT)
            self.state = 304
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 305
            self.indexvariable()
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 306
                self.match(patitoParser.COMMA)
                self.state = 307
                self.indexvariable()
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 313
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 314
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
        self.enterRule(localctx, 42, self.RULE_write)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(patitoParser.PRINT)
            self.state = 317
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 318
                self.hexp()
                pass

            elif la_ == 2:
                self.state = 319
                self.match(patitoParser.CTE_STRING)
                pass


            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==patitoParser.COMMA:
                self.state = 322
                self.match(patitoParser.COMMA)
                self.state = 325
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 323
                    self.hexp()
                    pass

                elif la_ == 2:
                    self.state = 324
                    self.match(patitoParser.CTE_STRING)
                    pass


                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 332
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 333
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
            self.state = 335
            self.match(patitoParser.IF)
            self.state = 336
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 337
            self.mexp()
            self.state = 338
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 339
            self.match(patitoParser.THEN)
            self.state = 340
            self.match(patitoParser.LEFT_CURLY)
            self.state = 341
            self.statute()
            self.state = 342
            self.match(patitoParser.RIGHT_CURLY)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==patitoParser.ELSE:
                self.state = 343
                self.match(patitoParser.ELSE)
                self.state = 344
                self.match(patitoParser.LEFT_CURLY)
                self.state = 345
                self.statute()
                self.state = 346
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
        self.enterRule(localctx, 46, self.RULE_whileloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(patitoParser.WHILE)
            self.state = 351
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 352
            self.mexp()
            self.state = 353
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 354
            self.match(patitoParser.DO)
            self.state = 355
            self.match(patitoParser.LEFT_CURLY)
            self.state = 356
            self.statute()
            self.state = 357
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
        self.enterRule(localctx, 48, self.RULE_fromloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(patitoParser.FROM)
            self.state = 360
            self.indexvariable()
            self.state = 361
            self.match(patitoParser.ASSIGN)
            self.state = 362
            self.mexp()
            self.state = 363
            self.match(patitoParser.TO)
            self.state = 364
            self.mexp()
            self.state = 365
            self.match(patitoParser.DO)
            self.state = 366
            self.match(patitoParser.LEFT_CURLY)
            self.state = 367
            self.statute()
            self.state = 368
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
            self.state = 370
            self.match(patitoParser.MAIN)
            self.state = 371
            self.match(patitoParser.LEFT_PARENTHESIS)
            self.state = 372
            self.match(patitoParser.RIGHT_PARENTHESIS)
            self.state = 373
            self.match(patitoParser.LEFT_CURLY)
            self.state = 374
            self.statute()
            self.state = 375
            self.match(patitoParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
