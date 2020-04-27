from antlr4 import *
from Compiler.compiler import *
from Compiler.variable import *

class Function:
    def __init__(self, name, returntype, parameters, varsTable):
        self.name = name
        self.returntype = returntype
        self.parameters = {}
        self.varsTable = {}


def get_parameters(parserParameters):
    parameters={}
    for i in range(len(parserParameters.vartypes())):
        parameterType = (parserParameters.vartypes()[i].getText())
        parameterName = (parserParameters.ID()[i].getText())
        if parameterName not in parameters:
            #print(parameterName, parameterType)
            parameters[parameterName] = Variable(parameterName, parameterType, None)
        else:
            print("You can't have two or more parameters with the same name.")

    return parameters
