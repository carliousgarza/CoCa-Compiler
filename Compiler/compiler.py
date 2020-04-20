from antlr4 import *


class Variable:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

class Function:
    def __init__(self, name, returntype, varsTable):
        self.name = name
        self.returntype = returntype
        self.varsTable = []

class Compiler:
    def __init__(self):
        self.functionTable = [Function("global", "void", [])]

    def _add_function(self, func: Function):
        self.functionTable.append(func)

    def _add_variable(self, var: Variable):
        self.functionTable[len(self.functionTable) - 1].varsTable.append(var)

        print(self.functionTable[len(self.functionTable) - 1].name)
        for var in self.functionTable[len(self.functionTable) - 1].varsTable:
            print(var.type, var.name)
