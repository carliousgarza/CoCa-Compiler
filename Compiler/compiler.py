from antlr4 import *


class Variable:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

class Function:
    def __init__(self, name, returntype, parameters, varsTable):
        self.name = name
        self.returntype = returntype
        self.parameters = {}
        self.varsTable = {}

class Compiler:
    def __init__(self):
        self.functionTable = [Function("global", "void", {}, {})]

    def _add_function(self, func: Function):
        self.functionTable.append(func)

def get_parameters(parserParameters):
    parameters={}
    for i in range(len(parserParameters.vartypes())):
        parameterType = (parserParameters.vartypes()[i].getText())
        parameterName = (parserParameters.ID()[i].getText())
        if parameterName not in parameters:
            print(parameterName, parameterType)
            parameters[parameterName] = Variable(parameterName, parameterType, None)
        else:
            print("You can't have two or more parameters with the same name.")

    return parameters

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
