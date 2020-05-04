from antlr4 import *
from Compiler.function import *
from Compiler.variable import *
from Compiler.quadruple import *
from Compiler.semanticCube import *
import operator


class Compiler:
    def __init__(self):
        self.functionTable = {}
        self.currentFunction = Function("global", "void", {}, {})
        self.quadruples = []
        self.operatorStack = []
        self.operandStack = []
        self.jumpStack = []
        self.typesStack = []
        self.tempStack = []
        self.counter = 0
        self.scube = SemanticCube()
        print("compiling...")

    def get_operator_fn(op):
        return {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.div,
            '=' : operator.eq,
            }[op]

    def _add_function(self, func: Function):
        self.functionTable[func.name] = func
        # print("Se agrego la función", func.name, "de tipo", func.returntype)
        # print("parametros:")
        # for parameter in func.parametersTable:
        #     print(func.parametersTable[parameter].vartype, func.parametersTable[parameter].name)
        # print("variables (los parametros se repiten aqui) :")
        # for var in func.varsTable:
        #     print(func.varsTable[var].vartype, func.varsTable[var].name)
    #code generator

    def addType(self, vartype):
        self.typesStack.append(vartype)
        # print(vartype)

    def addOperand(self, operand):
        self.operandStack.append(operand)
        # print(operand)

    def addOperandAndType(self, operand):
        self.operandStack.append(operand)
        if operand in self.currentFunction.varsTable:
            self.addType(self.currentFunction.varsTable[operand].vartype)
            # print(operand)
        elif operand in self.functionTable["global"].varsTable:
            self.addType(self.functionTable["global"].varsTable[operand].vartype)
            # print(operand)
        else:
            print("undeclared variable", operand)

    def addOperator(self, operator):
        self.operatorStack.append(operator)
        # print(operator)

    def addParenthesis(self):
        self.operatorStack.append('(')
        # print('(')

    def popParenthesis(self):
        self.operatorStack.pop()
        # print(')')

    def topIsMultOrDiv(self):
        if len(self.operatorStack) != 0:
            if self.operatorStack[-1] == "*" or self.operatorStack[-1] == "/":
                self.generateQuad()

    def topIsAddOrSub(self):
        if len(self.operatorStack) != 0:
            if self.operatorStack[-1] == "+" or self.operatorStack[-1] == "-":
                self.generateQuad()

    def topIsAssignment(self):
        if len(self.operatorStack) != 0:
            # print(self.operatorStack[-1])
            if self.operatorStack[-1] == "=":
                self.generateQuad()

    def generateReadQuad(self, readId):
        print("read", readId, None, "-")
        quad = Quadruple("read", readId, None, "-")
        self.quadruples.append(quad)

    def generateWriteQuad(self, writeId):
        print("writing")

    def generateQuad(self):
        rightOperand = self.operandStack.pop()
        leftOperand = self.operandStack.pop()
        operator = self.operatorStack.pop()
        rightOperandType = self.typesStack.pop()
        leftOperandType = self.typesStack.pop()
        if self.scube.cube[leftOperandType][operator][rightOperandType].startswith("Error"):
            print(self.scube.cube[leftOperandType][operator][rightOperandType])
        else:
            if operator == "=":
                quad = Quadruple(operator, leftOperand, self.quadruples[-1].resultTemp, self.quadruples[-1].resultTemp)
                self.quadruples.append(quad)
                print(operator, leftOperand, rightOperand)
            else:
                ## FIXME:
                tempResult = 'X' + str(self.counter)
                self.counter = self.counter + 1

                quad = Quadruple(operator, leftOperand, rightOperand, tempResult)
                self.quadruples.append(quad)
                self.addOperand(tempResult)
                self.addType('int')
                print(operator, leftOperand, rightOperand, tempResult)
