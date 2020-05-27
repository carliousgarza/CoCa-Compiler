from antlr4 import *
from Compiler.compiler import *
from Compiler.function import *

class Variable:
    def __init__(self, name, vartype, value, address):
        self.name = name
        self.vartype = vartype
        self.value = value
        self.address = address
        self.isArray = False
        self.isMatrix = False
        self.size = 1
        self.first_index = -1
        self.second_index = -1
