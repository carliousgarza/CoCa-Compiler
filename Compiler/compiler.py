from antlr4 import *
from Compiler.function import *
from Compiler.variable import *

class Compiler:
    def __init__(self):
        self.functionTable = [Function("global", "void", {}, {})]

    def _add_function(self, func: Function):
        self.functionTable.append(func)
        print(func.name)
