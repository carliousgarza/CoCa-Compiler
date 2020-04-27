from antlr4 import *
from Compiler.function import *
from Compiler.variable import *
from Compiler.compiler import *

#code generator
class Interpreter:
    def __init__(self):
        self.quadruples = []
        self.operatorStack = []
        self.operandStack = []
        self.jumpStack = []
        self.typesStack =[]
        print("interpreting...")

    def addVarType(self, varId, varType):
        self.operandStack.append(varId)
        self.typesStack.append(varType)
        print(varId, varType)

    def addOperator(self, operator):
        self.operatorStack.append(operator)
        print(operator)

    def addParenthesis(self):
        self.operatorStack.append('(')
        print('(')

    def popParenthesis(self):
        self.operatorStack.pop()
        print(')')

    def createQuadruple(self):
        print("desmadrote aqui")

class Quadruples:
    def __init__(self, operator, leftOp, rightOp, resultTemp):
        self.operator = operator
        self.leftOp = leftOp
        self.rightOp = rightOp
        self.resultTemp = resultTemp
