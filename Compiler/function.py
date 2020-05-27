from antlr4 import *
from Compiler.compiler import *
from Compiler.variable import *

class Function:
    def __init__(self, name, returntype, parameters, varsTable):
        self.name = name
        self.returntype = returntype
        self.parametersTable = parameters
        self.varsTable = varsTable
        self.startQuadruple = -1
        self.varsCount = 0
