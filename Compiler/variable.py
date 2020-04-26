from antlr4 import *
from Compiler.compiler import *
from Compiler.function import *

class Variable:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value


def get_variables(parserVariables):
    variables = {}

    for parserVariable in parserVariables.variables():
        for parserVarIndividual in parserVariable.varindividual():
            name = parserVarIndividual.ID().getText()
            vartype = parserVariable.vartypes().getText()
            var = Variable(name, vartype, None)
            if name not in variables:
                variables[name] = var
            else:
                print("You can't have two or more variables declared with the same name:", name)

    return variables


def get_vartype(parserVartypeContext):
    vartype = parserVartypeContext.vartypes()
    if vartype == None:
        vartype = (parserVartypeContext.VOID())
    else:
        vartype = (parserVartypeContext.vartypes().getText())
    return vartype
