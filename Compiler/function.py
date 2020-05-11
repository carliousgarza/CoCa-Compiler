from antlr4 import *
from Compiler.compiler import *
from Compiler.variable import *

class Function:
    def __init__(self, name, returntype, parameters, varsTable):
        self.name = name
        self.returntype = returntype
        self.parametersTable = parameters
        self.varsTable = varsTable
        self.quadrupleIndex = -1
        self.varsCount = 0

    def _update_parameters(self, id, vartype):
        if id not in self.parametersTable:
            self.parametersTable.append(Variable(id, vartype, None))
            self._update_vars_table(id, vartype)
        else:
            print("You can't have two or more parameters with the same name")

    def _update_vars_table(self, id, vartype):
        if id not in self.varsTable:
            self.varsTable[id] = Variable(id, vartype, None)
            self.varsCount += 1
        else:
            print("You can't have two or more variables with the same name")
