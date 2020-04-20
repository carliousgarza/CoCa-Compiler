import sys
#from Grammar.patito import patito
from Grammar.patitoLexer import patitoLexer
from Grammar.patitoListener import patitoListener
from Grammar.patitoParser import patitoParser
from antlr4 import *
from antlr4.tree.Trees import Trees


def main(argv):
    input = FileStream(argv[1]) #read the first argument as a filestream
    lexer = patitoLexer(input) #call your lexer
    stream = CommonTokenStream(lexer)
    parser = patitoParser(stream)
    tree = parser.program() #start from the parser rule, however should be changed to your entry rule for your specific grammar.
    print(Trees.toStringTree(tree, None, parser))
    printer = patitoListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    if parser.getNumberOfSyntaxErrors() == 0:
      print("PROGRAMA CORRECTO")
    else:
      print("PROGRAMA INCORRECTO")

if __name__ == '__main__':
    main(sys.argv)
