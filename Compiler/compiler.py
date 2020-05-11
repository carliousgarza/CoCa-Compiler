from antlr4 import *
from Compiler.function import *
from Compiler.variable import *
from Compiler.quadruple import *
from Compiler.semanticCube import *
import operator


class Compiler:
    def __init__(self):
        self.functionTable = {}
        self.currentFunction = Function("global", "void", [], {})
        self.quadruples = []
        self.operatorStack = []
        self.operandStack = []
        self.jumpStack = []
        self.typesStack = []
        self.tempStack = []
        self.temporalCounter = 0
        self.scube = SemanticCube()
        self.fromVariableStack = []
        self.functionStack = []
        print("compiling...")

    def get_operator_fn(op):
        return {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.div,
            '=': operator.eq,
        }[op]

    def _add_function(self, func: Function):
        self.currentFunction.startQuadruple = len(self.quadruples)
        self.functionTable[func.name] = func
        # print("Se agrego la función", func.name, "de tipo", func.returntype)
        # print("parametros:")
        # for parameter in func.parametersTable:
        #     print(func.parametersTable[parameter].vartype, func.parametersTable[parameter].name)
        # print("variables (los parametros se repiten aqui) :")
        # for var in func.varsTable:
        #     print(func.varsTable[var].vartype, func.varsTable[var].name)

    # code generator

    def addType(self, vartype):
        self.typesStack.append(vartype)
        # print(vartype)

    def addOperand(self, operand):
        self.operandStack.append(operand)
        # print(operand)

    def addOperandAndType(self, operand):
        if operand in self.currentFunction.varsTable:
            self.operandStack.append(operand)
            self.addType(self.currentFunction.varsTable[operand].vartype)
            # print(operand)
        elif operand in self.functionTable["global"].varsTable:
            self.operandStack.append(operand)
            self.addType(self.functionTable["global"].varsTable[operand].vartype)
            # print(operand)
        else:
            raise ValueError(f'The variable {operand} is not declared')

    def addFuncOperandAndType(self, operand):
        if self.functionTable[operand].returntype == 'void':
            raise TypeError(f'Cannot assign void function {operand} to value')
        else:
            self.operandStack.append(operand)
            self.addType(self.functionTable[operand].returntype)

    def addOperator(self, operator):
        self.operatorStack.append(operator)
        # print(operator)

    def validate_void_function(self, id):
        if id in self.functionTable:
            if self.functionTable[id].returntype != 'void':
                raise TypeError(f'Function {id} return value must be assigned')
            else:
                print(f'we inside void function {id}')
        else:
            raise ValueError(f'Function {id} is not declared')

    def validate_parameters(self, id, currentCounter):
        if len(self.functionTable[id].parametersTable) == currentCounter:
            # reversed FOR because the parametersTable is reversed in relation to operandStack
            # example: funccall(0, 1, 2) --> passedParameter is the one we want to match with 2
            for parameter in reversed(self.functionTable[id].parametersTable):
                passedParameter = self.operandStack.pop()
                passedParameterType = self.typesStack.pop()
                if(parameter.vartype != passedParameterType):
                    raise TypeError(f'Parameter {passedParameter} of type {passedParameterType} '
                                    f'cannot be matched with {parameter.vartype}')
                else:
                    # tenemos que asignar a memoria aqui passedParameter con su type
                    print("we gucci")
        else:
            raise ValueError(f'Number of parameters in call to function {id} does not match the amount declared')

    def goto_function_quad(self, id):
        quad = Quadruple('GOTO', None, None, self.functionTable[id].startQuadruple)
        print('GOTO', 'None', 'None', self.functionTable[id].startQuadruple)
        # self.quadruples[self.functionTable[id].endQuadruple].resultTemp = len(self.quadruples)
        self.quadruples.append(quad)
        # self.functionStack.append({'function': self.currentFunction, 'quad': len(self.quadruples)})
        # self.currentFunction = self.functionTable[id]

    def create_endfunc_goto(self):
        self.currentFunction.endQuadruple = len(self.quadruples)
        quad = Quadruple('GOTO', None, None, '_')
        print('ENDGOTO', None, None, '_')
        self.quadruples.append(quad)

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
            if self.operatorStack[-1] == "==" or self.operatorStack[-1] == "!=" or self.operatorStack[-1] == ">=" or \
                    self.operatorStack[-1] == "<=" or self.operatorStack[-1] == ">" or self.operatorStack[-1] == "<":
                self.generateQuad()

    def topIsLogicOperator(self):
        if len(self.operatorStack) != 0:
            if self.operatorStack[-1] == "&&" or self.operatorStack[-1] == "||":
                self.generateQuad()

    # QUADRUPLES

    def goto_main_quad(self):
        quad = Quadruple("GOTO", None, None, "_")
        # 0 = the index number of the first quadruple
        self.jumpStack.append(0)
        self.quadruples.append(quad)

    def fill_goto_main_quad(self):
        mainQuad = self.jumpStack.pop()
        print(f'main quad #: {mainQuad}')
        self.quadruples[mainQuad].resultTemp = self.currentFunction.startQuadruple
        print(f'main quad is jumping to {self.currentFunction.startQuadruple}')

    def generateIfQuad(self):
        # beginning of if
        if len(self.operandStack) != 0:
            conditionVar = self.operandStack.pop()
            typeConditionVar = self.typesStack.pop()
            if typeConditionVar == "bool":
                quad = Quadruple("GOTOF", conditionVar, None, "_")
                # this quadruple's index must be saved for later
                self.jumpStack.append(len(self.quadruples))
                self.quadruples.append(quad)
            else:
                raise TypeError(f'Error: {conditionVar} is not a boolean')

    def generateEndIfQuad(self):
        # popping
        false = self.jumpStack.pop()
        # fill the previous quadruple's GOTOF value with the current quadruple index
        self.quadruples[false].resultTemp = len(self.quadruples)

    def generateGoToQuad(self):
        # if there was an else, you are here
        # this GOTO will redirect the end of an if block to the end of the conditional statute
        quad = Quadruple("GOTO", None, None, "_")
        self.quadruples.append(quad)

        # BUT FIRST! we have to make sure that the previously saved GOTOF from the if redirects to this else
        # ALSO, we have to point the GOTO to the end of the conditional statue, as said earlier.
        self.generateEndIfQuad()
        # So we append the GOTO's current index (length-1) to the jumpstack, AFTER having popped the other jump previously saved
        self.jumpStack.append(len(self.quadruples) - 1)

    def addFromVarOperand(self, operand):
        print("agrega fromvaroperand")
        if operand in self.currentFunction.varsTable:
            if self.currentFunction.varsTable[operand].vartype == "int":
                # Add the current operand to the From Variable Stack to keep its address for future reference.
                # We will need its address to be able to modify it
                self.fromVariableStack.append(operand)
                self.operandStack.append(operand)
                self.addType(self.currentFunction.varsTable[operand].vartype)
                # print(operand)
            else:
                raise TypeError(f'The variable {operand} is not an int')
        elif operand in self.functionTable["global"].varsTable:
            if self.functionTable["global"].varsTable[operand].vartype == "int":
                # Add the current operand to the From Variable Stack to keep its address for future reference.
                # We will need its address to be able to modify it
                self.fromVariableStack.append(operand)
                self.operandStack.append(operand)
                self.addType(self.functionTable["global"].varsTable[operand].vartype)
                # print(operand)
            else:
                raise TypeError(f'The variable {operand} is not an int')
        else:
            raise ValueError(f'The variable {operand} is not declared')

    def generateFromBeforeCheck(self):
        print("FromBeginning")
        self.jumpStack.append(len(self.quadruples))

    def generateFromAfterCheck(self):
        print("FromAfter")
        if len(self.operandStack) != 0:
            expResult = self.operandStack.pop()
            typeExpResult = self.typesStack.pop()
            # Get the initial variable of the from loop
            fromVar = self.fromVariableStack[-1]
            if typeExpResult == "int":
                # Aqui vamos a tener que sacar el valor de fromVar, para poder compararlo con expResult
                # una vez comparado, tenemos fromConditionResult y ese es el que ponemos en el quad.
                # fromConditionResult = fromVar <= expResult
                fromConditionResult = False
                quad = Quadruple("GOTOF", fromConditionResult, None, "_")
                # this quadruple's index must be saved for later
                self.jumpStack.append(len(self.quadruples))
                self.quadruples.append(quad)
                print("GOTOF", fromConditionResult, None, "_")
            else:
                raise TypeError(f'Error: The expression resulting in {expResult} must be an integer')

    def generateEndFromQuad(self):
        print("FromEnd")
        # Get the index of the beginning of the from statute
        fromAfterCheckIndex = self.jumpStack.pop()
        fromBeforeCheckIndex = self.jumpStack.pop()
        # Append the current GOTO quadruple, to go back to the beginning of the from
        quad = Quadruple("GOTO", None, None, fromBeforeCheckIndex)
        print("GOTO", None, None, fromBeforeCheckIndex)
        self.quadruples.append(quad)
        self.quadruples[fromAfterCheckIndex].resultTemp = len(self.quadruples)
        print(self.quadruples[fromAfterCheckIndex].operator, self.quadruples[fromAfterCheckIndex].leftOp,
              self.quadruples[fromAfterCheckIndex].rightOp, self.quadruples[fromAfterCheckIndex].resultTemp)
        # NOTE: We need to add 1 to the counter variable in here

    def generateWhileBeforeCheck(self):
        print("WhileBeginning")
        self.jumpStack.append(len(self.quadruples))

    def generateWhileAfterCheck(self):
        print("WhileQuad")
        if len(self.operandStack) != 0:
            conditionVar = self.operandStack.pop()
            typeConditionVar = self.typesStack.pop()
            if typeConditionVar == "bool":
                quad = Quadruple("GOTOF", conditionVar, None, "_")
                # this quadruple's index must be saved for later
                self.jumpStack.append(len(self.quadruples))
                self.quadruples.append(quad)
                print("GOTOF", conditionVar, None, "_")
            else:
                raise TypeError(f'Error: {conditionVar} is not a boolean')

    def generateWhileEnd(self):
        print("WhileEnd")
        # Get the index of the beginning of the while statute
        whileAfterCheckIndex = self.jumpStack.pop()
        whileBeforeCheckIndex = self.jumpStack.pop()
        # Append the current GOTO quadruple, to go back to the beginning of the while
        quad = Quadruple("GOTO", None, None, whileBeforeCheckIndex)
        print("GOTO", None, None, whileBeforeCheckIndex)
        self.quadruples.append(quad)
        self.quadruples[whileAfterCheckIndex].resultTemp = len(self.quadruples)
        print(self.quadruples[whileAfterCheckIndex].operator, self.quadruples[whileAfterCheckIndex].leftOp,
              self.quadruples[whileAfterCheckIndex].rightOp, self.quadruples[whileAfterCheckIndex].resultTemp)

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
        # In case of multiple assignments in the same line, we use a while
        while self.operatorStack and self.operatorStack[-1] == "=":
            rightOperand = self.operandStack.pop()
            leftOperand = self.operandStack.pop()

            operator = self.operatorStack.pop()

            rightOperandType = self.typesStack.pop()
            leftOperandType = self.typesStack.pop()

            # Semantic Cube Error
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

        # Check with semantic cube to see if operation is possible
        if self.scube.cube[leftOperandType][operator][rightOperandType].startswith("Error"):
            raise ValueError(f'{self.scube.cube[leftOperandType][operator][rightOperandType]}')
        else:
            ## FIXME: create real address for temporal variable
            tempResult = 'X' + str(self.temporalCounter)
            self.temporalCounter = self.temporalCounter + 1

            # Create Quad and add it to Quadruples Stack
            quad = Quadruple(operator, leftOperand, rightOperand, tempResult)
            self.quadruples.append(quad)

            # Add result back to the Operand Stack
            self.addOperand(tempResult)

            # Look up result type and add it to type stack
            self.addType(self.scube.cube[leftOperandType][operator][rightOperandType])

            print(operator, leftOperand, rightOperand, tempResult)
