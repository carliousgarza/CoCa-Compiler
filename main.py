import sys
#from Grammar.patito import patito
from Grammar.patitoLexer import patitoLexer
from Grammar.patitoListener import patitoListener
from Grammar.patitoParser import patitoParser
from antlr4 import *
from antlr4.tree.Trees import Trees
from Compiler.compiler import Compiler
from VirtualMachine.virtualMachine import VirtualMachine


def main(argv):
    compiler = Compiler()
    input = FileStream(argv[1]) #read the first argument as a filestream
    lexer = patitoLexer(input) #call your lexer
    stream = CommonTokenStream(lexer)
    parser = patitoParser(compiler, stream)
    tree = parser.program() #start from the parser rule, however should be changed to your entry rule for your specific grammar.

    if parser.getNumberOfSyntaxErrors() == 0:
        print("PROGRAMA CORRECTO ========================================================================")
        quadruples = compiler.get_quadruples()
        constants = compiler.get_constants_table()
        virtualMachine = VirtualMachine(quadruples, constants)
        virtualMachine.begin()
    else:
        print("PROGRAMA INCORRECTO")

if __name__ == '__main__':
    main(sys.argv)
