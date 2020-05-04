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
        #print(vartype)

    def addOperand(self, operand):
        self.operandStack.append(operand)
        #print(operand)

    def addOperandAndType(self, operand):
        if operand in self.currentFunction.varsTable:
            self.operandStack.append(operand)
            self.addType(self.currentFunction.varsTable[operand].vartype)
            #print(operand)
        elif operand in self.functionTable["global"].varsTable:
            self.operandStack.append(operand)
            self.addType(self.functionTable["global"].varsTable[operand].vartype)
            #print(operand)
        else:
            raise ValueError(f'The variable {operand} is not declared')

    def addOperator(self, operator):
        self.operatorStack.append(operator)
        #print(operator)

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

    def topIsComparison(self):
        if len(self.operatorStack) != 0:
            if self.operatorStack[-1] == "==" or self.operatorStack[-1] == "!=" or self.operatorStack[-1] == ">=" or self.operatorStack[-1] == "<=" or self.operatorStack[-1] == ">" or self.operatorStack[-1] == "<":
                self.generateQuad()

    def topIsLogicOperator(self):
        if len(self.operatorStack) != 0:
            if self.operatorStack[-1] == "&&" or self.operatorStack[-1] == "||":
                self.generateQuad()

    def generateReadQuad(self, operand):
        # NOTE: If we need the type in the future, we could assign it here in either the 3rd or 4th position of the quad.
        if operand in self.currentFunction.varsTable:
            print("read", operand, None, "-")
            quad = Quadruple("read", operand, None, "_")
            self.quadruples.append(quad)
        elif operand in self.functionTable["global"].varsTable:
            print("read", operand, None, "-")
            quad = Quadruple("read", operand, None, "_")
            self.quadruples.append(quad)
        else:
            raise ValueError(f'The variable {operand} is not declared')

    def generateWriteQuad(self):
        printedOperand = self.operandStack.pop()
        printedType = self.typesStack.pop()

        print("print", printedOperand, None, "_")

        quad = Quadruple("print", printedOperand, None, "_")
        self.quadruples.append(quad)

    def generateAssignQuads(self):
        #In case of multiple assignments in the same line, we use a while
        while self.operatorStack and self.operatorStack[-1] == "=":
            rightOperand = self.operandStack.pop()
            leftOperand = self.operandStack.pop()

            operator = self.operatorStack.pop()

            rightOperandType = self.typesStack.pop()
            leftOperandType = self.typesStack.pop()

            #Semantic Cube Error
            if self.scube.cube[leftOperandType][operator][rightOperandType].startswith("Error"):
                raise ValueError(f'{self.scube.cube[leftOperandType][operator][rightOperandType]}')

            quad = Quadruple(operator, leftOperand, rightOperand, "_")
            self.quadruples.append(quad)

            self.operandStack.append(leftOperand)
            self.typesStack.append(leftOperandType)
            print(operator, leftOperand, rightOperand, "_")

        self.operandStack.pop()
        self.typesStack.pop()

    def generateQuad(self):
        rightOperand = self.operandStack.pop()
        leftOperand = self.operandStack.pop()
        operator = self.operatorStack.pop()
        rightOperandType = self.typesStack.pop()
        leftOperandType = self.typesStack.pop()

        #Check with semantic cube to see if operation is possible
        if self.scube.cube[leftOperandType][operator][rightOperandType].startswith("Error"):
            raise ValueError(f'{self.scube.cube[leftOperandType][operator][rightOperandType]}')
        else:
            ## FIXME: create real address for temporal variable
            tempResult = 'X' + str(self.counter)
            self.counter = self.counter + 1

            #Create Quad and add it to Quadruples Stack
            quad = Quadruple(operator, leftOperand, rightOperand, tempResult)
            self.quadruples.append(quad)

            #Add result back to the Operand Stack
            self.addOperand(tempResult)

            #Look up result type and add it to type stack
            self.addType(self.scube.cube[leftOperandType][operator][rightOperandType])

            print(operator, leftOperand, rightOperand, tempResult)
