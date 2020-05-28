# Generated from patito.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from Compiler.compiler import *
from Compiler.function import *
from Compiler.variable import *
from Compiler.quadruple import *
compiler = Compiler()



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\28")
        buf.write("\u015f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\3\2\3\2\7")
        buf.write("\2t\n\2\f\2\16\2w\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\7\3\u0082\n\3\f\3\16\3\u0085\13\3\3\3\3\3\3\4\6\4")
        buf.write("\u008a\n\4\r\4\16\4\u008b\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3")
        buf.write("*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3.\3")
        buf.write(".\3.\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u0137\n")
        buf.write("\61\3\62\6\62\u013a\n\62\r\62\16\62\u013b\3\62\3\62\6")
        buf.write("\62\u0140\n\62\r\62\16\62\u0141\3\63\6\63\u0145\n\63\r")
        buf.write("\63\16\63\u0146\3\64\3\64\3\65\3\65\7\65\u014d\n\65\f")
        buf.write("\65\16\65\u0150\13\65\3\65\3\65\3\66\3\66\3\66\3\66\3")
        buf.write("\66\3\67\3\67\7\67\u015b\n\67\f\67\16\67\u015e\13\67\4")
        buf.write("u\u014e\28\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8\3\2\b\4\2\f\f\17\17\5\2\13\f\17\17\"\"\3\2\62;\3")
        buf.write("\2\60\60\5\2C\\aac|\6\2\62;C\\aac|\2\u0167\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\3o\3\2\2\2\5}\3\2\2\2\7\u0089")
        buf.write("\3\2\2\2\t\u008f\3\2\2\2\13\u0091\3\2\2\2\r\u0093\3\2")
        buf.write("\2\2\17\u0096\3\2\2\2\21\u0099\3\2\2\2\23\u009c\3\2\2")
        buf.write("\2\25\u009f\3\2\2\2\27\u00a1\3\2\2\2\31\u00a4\3\2\2\2")
        buf.write("\33\u00a7\3\2\2\2\35\u00a9\3\2\2\2\37\u00ab\3\2\2\2!\u00ad")
        buf.write("\3\2\2\2#\u00af\3\2\2\2%\u00b1\3\2\2\2\'\u00b3\3\2\2\2")
        buf.write(")\u00b5\3\2\2\2+\u00b7\3\2\2\2-\u00b9\3\2\2\2/\u00bb\3")
        buf.write("\2\2\2\61\u00bd\3\2\2\2\63\u00bf\3\2\2\2\65\u00c1\3\2")
        buf.write("\2\2\67\u00c3\3\2\2\29\u00c5\3\2\2\2;\u00c7\3\2\2\2=\u00cf")
        buf.write("\3\2\2\2?\u00d4\3\2\2\2A\u00dd\3\2\2\2C\u00e4\3\2\2\2")
        buf.write("E\u00ea\3\2\2\2G\u00f0\3\2\2\2I\u00f3\3\2\2\2K\u00f8\3")
        buf.write("\2\2\2M\u00fd\3\2\2\2O\u0103\3\2\2\2Q\u0106\3\2\2\2S\u010b")
        buf.write("\3\2\2\2U\u010e\3\2\2\2W\u0112\3\2\2\2Y\u0117\3\2\2\2")
        buf.write("[\u011b\3\2\2\2]\u0121\3\2\2\2_\u0128\3\2\2\2a\u0136\3")
        buf.write("\2\2\2c\u0139\3\2\2\2e\u0144\3\2\2\2g\u0148\3\2\2\2i\u014a")
        buf.write("\3\2\2\2k\u0153\3\2\2\2m\u0158\3\2\2\2op\7\61\2\2pq\7")
        buf.write(",\2\2qu\3\2\2\2rt\13\2\2\2sr\3\2\2\2tw\3\2\2\2uv\3\2\2")
        buf.write("\2us\3\2\2\2vx\3\2\2\2wu\3\2\2\2xy\7,\2\2yz\7\61\2\2z")
        buf.write("{\3\2\2\2{|\b\2\2\2|\4\3\2\2\2}~\7\61\2\2~\177\7\61\2")
        buf.write("\2\177\u0083\3\2\2\2\u0080\u0082\n\2\2\2\u0081\u0080\3")
        buf.write("\2\2\2\u0082\u0085\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084")
        buf.write("\3\2\2\2\u0084\u0086\3\2\2\2\u0085\u0083\3\2\2\2\u0086")
        buf.write("\u0087\b\3\2\2\u0087\6\3\2\2\2\u0088\u008a\t\3\2\2\u0089")
        buf.write("\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u0089\3\2\2\2")
        buf.write("\u008b\u008c\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e\b")
        buf.write("\4\2\2\u008e\b\3\2\2\2\u008f\u0090\7>\2\2\u0090\n\3\2")
        buf.write("\2\2\u0091\u0092\7@\2\2\u0092\f\3\2\2\2\u0093\u0094\7")
        buf.write(">\2\2\u0094\u0095\7?\2\2\u0095\16\3\2\2\2\u0096\u0097")
        buf.write("\7@\2\2\u0097\u0098\7?\2\2\u0098\20\3\2\2\2\u0099\u009a")
        buf.write("\7?\2\2\u009a\u009b\7?\2\2\u009b\22\3\2\2\2\u009c\u009d")
        buf.write("\7#\2\2\u009d\u009e\7?\2\2\u009e\24\3\2\2\2\u009f\u00a0")
        buf.write("\7?\2\2\u00a0\26\3\2\2\2\u00a1\u00a2\7(\2\2\u00a2\u00a3")
        buf.write("\7(\2\2\u00a3\30\3\2\2\2\u00a4\u00a5\7~\2\2\u00a5\u00a6")
        buf.write("\7~\2\2\u00a6\32\3\2\2\2\u00a7\u00a8\7-\2\2\u00a8\34\3")
        buf.write("\2\2\2\u00a9\u00aa\7/\2\2\u00aa\36\3\2\2\2\u00ab\u00ac")
        buf.write("\7,\2\2\u00ac \3\2\2\2\u00ad\u00ae\7\61\2\2\u00ae\"\3")
        buf.write("\2\2\2\u00af\u00b0\7*\2\2\u00b0$\3\2\2\2\u00b1\u00b2\7")
        buf.write("+\2\2\u00b2&\3\2\2\2\u00b3\u00b4\7]\2\2\u00b4(\3\2\2\2")
        buf.write("\u00b5\u00b6\7_\2\2\u00b6*\3\2\2\2\u00b7\u00b8\7}\2\2")
        buf.write("\u00b8,\3\2\2\2\u00b9\u00ba\7\177\2\2\u00ba.\3\2\2\2\u00bb")
        buf.write("\u00bc\7&\2\2\u00bc\60\3\2\2\2\u00bd\u00be\7%\2\2\u00be")
        buf.write("\62\3\2\2\2\u00bf\u00c0\7A\2\2\u00c0\64\3\2\2\2\u00c1")
        buf.write("\u00c2\7.\2\2\u00c2\66\3\2\2\2\u00c3\u00c4\7<\2\2\u00c4")
        buf.write("8\3\2\2\2\u00c5\u00c6\7=\2\2\u00c6:\3\2\2\2\u00c7\u00c8")
        buf.write("\7r\2\2\u00c8\u00c9\7t\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb")
        buf.write("\7i\2\2\u00cb\u00cc\7t\2\2\u00cc\u00cd\7c\2\2\u00cd\u00ce")
        buf.write("\7o\2\2\u00ce<\3\2\2\2\u00cf\u00d0\7o\2\2\u00d0\u00d1")
        buf.write("\7c\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3\7p\2\2\u00d3>\3")
        buf.write("\2\2\2\u00d4\u00d5\7h\2\2\u00d5\u00d6\7w\2\2\u00d6\u00d7")
        buf.write("\7p\2\2\u00d7\u00d8\7e\2\2\u00d8\u00d9\7v\2\2\u00d9\u00da")
        buf.write("\7k\2\2\u00da\u00db\7q\2\2\u00db\u00dc\7p\2\2\u00dc@\3")
        buf.write("\2\2\2\u00dd\u00de\7t\2\2\u00de\u00df\7g\2\2\u00df\u00e0")
        buf.write("\7v\2\2\u00e0\u00e1\7w\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3")
        buf.write("\7p\2\2\u00e3B\3\2\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6")
        buf.write("\7p\2\2\u00e6\u00e7\7r\2\2\u00e7\u00e8\7w\2\2\u00e8\u00e9")
        buf.write("\7v\2\2\u00e9D\3\2\2\2\u00ea\u00eb\7r\2\2\u00eb\u00ec")
        buf.write("\7t\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef")
        buf.write("\7v\2\2\u00efF\3\2\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2")
        buf.write("\7h\2\2\u00f2H\3\2\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5")
        buf.write("\7j\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7\7p\2\2\u00f7J\3")
        buf.write("\2\2\2\u00f8\u00f9\7g\2\2\u00f9\u00fa\7n\2\2\u00fa\u00fb")
        buf.write("\7u\2\2\u00fb\u00fc\7g\2\2\u00fcL\3\2\2\2\u00fd\u00fe")
        buf.write("\7y\2\2\u00fe\u00ff\7j\2\2\u00ff\u0100\7k\2\2\u0100\u0101")
        buf.write("\7n\2\2\u0101\u0102\7g\2\2\u0102N\3\2\2\2\u0103\u0104")
        buf.write("\7f\2\2\u0104\u0105\7q\2\2\u0105P\3\2\2\2\u0106\u0107")
        buf.write("\7h\2\2\u0107\u0108\7t\2\2\u0108\u0109\7q\2\2\u0109\u010a")
        buf.write("\7o\2\2\u010aR\3\2\2\2\u010b\u010c\7v\2\2\u010c\u010d")
        buf.write("\7q\2\2\u010dT\3\2\2\2\u010e\u010f\7x\2\2\u010f\u0110")
        buf.write("\7c\2\2\u0110\u0111\7t\2\2\u0111V\3\2\2\2\u0112\u0113")
        buf.write("\7d\2\2\u0113\u0114\7q\2\2\u0114\u0115\7q\2\2\u0115\u0116")
        buf.write("\7n\2\2\u0116X\3\2\2\2\u0117\u0118\7k\2\2\u0118\u0119")
        buf.write("\7p\2\2\u0119\u011a\7v\2\2\u011aZ\3\2\2\2\u011b\u011c")
        buf.write("\7h\2\2\u011c\u011d\7n\2\2\u011d\u011e\7q\2\2\u011e\u011f")
        buf.write("\7c\2\2\u011f\u0120\7v\2\2\u0120\\\3\2\2\2\u0121\u0122")
        buf.write("\7u\2\2\u0122\u0123\7v\2\2\u0123\u0124\7t\2\2\u0124\u0125")
        buf.write("\7k\2\2\u0125\u0126\7p\2\2\u0126\u0127\7i\2\2\u0127^\3")
        buf.write("\2\2\2\u0128\u0129\7e\2\2\u0129\u012a\7j\2\2\u012a\u012b")
        buf.write("\7c\2\2\u012b\u012c\7t\2\2\u012c`\3\2\2\2\u012d\u012e")
        buf.write("\7v\2\2\u012e\u012f\7t\2\2\u012f\u0130\7w\2\2\u0130\u0137")
        buf.write("\7g\2\2\u0131\u0132\7h\2\2\u0132\u0133\7c\2\2\u0133\u0134")
        buf.write("\7n\2\2\u0134\u0135\7u\2\2\u0135\u0137\7g\2\2\u0136\u012d")
        buf.write("\3\2\2\2\u0136\u0131\3\2\2\2\u0137b\3\2\2\2\u0138\u013a")
        buf.write("\t\4\2\2\u0139\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b")
        buf.write("\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\3\2\2\2")
        buf.write("\u013d\u013f\7\60\2\2\u013e\u0140\t\4\2\2\u013f\u013e")
        buf.write("\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u013f\3\2\2\2\u0141")
        buf.write("\u0142\3\2\2\2\u0142d\3\2\2\2\u0143\u0145\t\4\2\2\u0144")
        buf.write("\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0144\3\2\2\2")
        buf.write("\u0146\u0147\3\2\2\2\u0147f\3\2\2\2\u0148\u0149\t\5\2")
        buf.write("\2\u0149h\3\2\2\2\u014a\u014e\7$\2\2\u014b\u014d\13\2")
        buf.write("\2\2\u014c\u014b\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014f")
        buf.write("\3\2\2\2\u014e\u014c\3\2\2\2\u014f\u0151\3\2\2\2\u0150")
        buf.write("\u014e\3\2\2\2\u0151\u0152\7$\2\2\u0152j\3\2\2\2\u0153")
        buf.write("\u0154\7x\2\2\u0154\u0155\7q\2\2\u0155\u0156\7k\2\2\u0156")
        buf.write("\u0157\7f\2\2\u0157l\3\2\2\2\u0158\u015c\t\6\2\2\u0159")
        buf.write("\u015b\t\7\2\2\u015a\u0159\3\2\2\2\u015b\u015e\3\2\2\2")
        buf.write("\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015dn\3\2\2")
        buf.write("\2\u015e\u015c\3\2\2\2\f\2u\u0083\u008b\u0136\u013b\u0141")
        buf.write("\u0146\u014e\u015c\3\b\2\2")
        return buf.getvalue()


class patitoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    LINE_COMMENT = 2
    WS = 3
    LESS = 4
    GREATER = 5
    LESS_EQUAL = 6
    GREATER_EQUAL = 7
    EQUAL = 8
    NOT_EQUAL = 9
    ASSIGN = 10
    AND = 11
    OR = 12
    ADD = 13
    SUB = 14
    MULT = 15
    DIV = 16
    LEFT_PARENTHESIS = 17
    RIGHT_PARENTHESIS = 18
    LEFT_BRACKET = 19
    RIGHT_BRACKET = 20
    LEFT_CURLY = 21
    RIGHT_CURLY = 22
    DETERMINANT = 23
    TRANSPOSE = 24
    INVERSE = 25
    COMMA = 26
    COLON = 27
    SEMICOLON = 28
    PROGRAM = 29
    MAIN = 30
    FUNCTION = 31
    RETURN = 32
    INPUT = 33
    PRINT = 34
    IF = 35
    THEN = 36
    ELSE = 37
    WHILE = 38
    DO = 39
    FROM = 40
    TO = 41
    VAR = 42
    BOOL = 43
    INT = 44
    FLOAT = 45
    STRING = 46
    CHAR = 47
    CTE_BOOL = 48
    CTE_FLOAT = 49
    CTE_INT = 50
    CTE_CHAR = 51
    CTE_STRING = 52
    VOID = 53
    ID = 54

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", "'='", "'&&'", 
            "'||'", "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "'$'", "'#'", "'?'", "','", "':'", "';'", "'program'", 
            "'main'", "'function'", "'return'", "'input'", "'print'", "'if'", 
            "'then'", "'else'", "'while'", "'do'", "'from'", "'to'", "'var'", 
            "'bool'", "'int'", "'float'", "'string'", "'char'", "'void'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "LINE_COMMENT", "WS", "LESS", "GREATER", "LESS_EQUAL", 
            "GREATER_EQUAL", "EQUAL", "NOT_EQUAL", "ASSIGN", "AND", "OR", 
            "ADD", "SUB", "MULT", "DIV", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", 
            "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_CURLY", "RIGHT_CURLY", 
            "DETERMINANT", "TRANSPOSE", "INVERSE", "COMMA", "COLON", "SEMICOLON", 
            "PROGRAM", "MAIN", "FUNCTION", "RETURN", "INPUT", "PRINT", "IF", 
            "THEN", "ELSE", "WHILE", "DO", "FROM", "TO", "VAR", "BOOL", 
            "INT", "FLOAT", "STRING", "CHAR", "CTE_BOOL", "CTE_FLOAT", "CTE_INT", 
            "CTE_CHAR", "CTE_STRING", "VOID", "ID" ]

    ruleNames = [ "COMMENT", "LINE_COMMENT", "WS", "LESS", "GREATER", "LESS_EQUAL", 
                  "GREATER_EQUAL", "EQUAL", "NOT_EQUAL", "ASSIGN", "AND", 
                  "OR", "ADD", "SUB", "MULT", "DIV", "LEFT_PARENTHESIS", 
                  "RIGHT_PARENTHESIS", "LEFT_BRACKET", "RIGHT_BRACKET", 
                  "LEFT_CURLY", "RIGHT_CURLY", "DETERMINANT", "TRANSPOSE", 
                  "INVERSE", "COMMA", "COLON", "SEMICOLON", "PROGRAM", "MAIN", 
                  "FUNCTION", "RETURN", "INPUT", "PRINT", "IF", "THEN", 
                  "ELSE", "WHILE", "DO", "FROM", "TO", "VAR", "BOOL", "INT", 
                  "FLOAT", "STRING", "CHAR", "CTE_BOOL", "CTE_FLOAT", "CTE_INT", 
                  "CTE_CHAR", "CTE_STRING", "VOID", "ID" ]

    grammarFileName = "patito.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


