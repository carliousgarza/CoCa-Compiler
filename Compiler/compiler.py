from antlr4 import *


class Variable:
    def __init__(self, name, type, value, scope):
        self.name = name
        self.type = type
        self.value = value
        self.scope = scope

class Function:
    def __init__(self, name, returntype):
        self.name = name
        self.returntype = returntype

class Compiler:
    def __init__(self):
        self.functionTable = []

    def _add_function(self, func: Function):
        print(func.returntype)
        print(func.name)
        self.functionTable.append(func)
