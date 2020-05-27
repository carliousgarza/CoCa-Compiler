from antlr4 import *
from Compiler.function import *
from Compiler.variable import *
from Compiler.quadruple import *
from Compiler.semanticCube import *
from Compiler.constant import *
from Memory.memory import Memory
import operator


class Compiler:
    def __init__(self):
        self.functionTable = {}
        self.currentFunction = Function("global", "void", [], {})
        self.constantTable = {}
        self.quadruples = []
        self.operatorStack = []
        self.operandStack = []
        self.jumpStack = []
        self.typesStack = []
        self.tempStack = []
        self.scube = SemanticCube()
        self.loopVariableStack = []
        self.functionStack = []
        self.memory = Memory()
        self.temporalStack = []
        print("compiling...")

    def get_quadruples(self):
        return self.quadruples

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
        if func.name not in self.functionTable:
            self.functionTable[func.name] = func
        else:
            raise Exception(f'The function {func.name} is already declared.')
        # print("Se agrego la función", func.name, "de tipo", func.returntype)
        # print("parametros:")
        # for parameter in func.parametersTable:
        #     print(func.parametersTable[parameter].vartype, func.parametersTable[parameter].name)
        # print("variables (los parametros se repiten aqui) :")
        # for var in func.varsTable:
        #     print(func.varsTable[var].vartype, func.varsTable[var].name)

    # code generator

    def addConstantToTypeStackAndTable(self, vartype):
        self.typesStack.append(vartype)
        if self.operandStack[-1] not in self.constantTable:
            self.constantTable[self.operandStack[-1]] = Constant(vartype, self.memory.mem_constant)
            print(f'added constant {vartype} {self.operandStack[-1]} to {self.memory.mem_constant}')
            self.memory.mem_constant += 1

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

    def validate_function_expression(self, operand):
        if self.functionTable[operand].returntype == 'void':
            raise TypeError(f'Cannot assign void function {operand} to value')
        quad = Quadruple("ERA", None, None, operand)
        self.quadruples.append(quad)
        print(f'ERA, None, None, {operand}')

    def add_func_operand_and_type(self, operand):
        tempResult = 'X' + str(len(self.temporalStack))
        tempType = self.functionTable[operand].returntype
        self.operandStack.append(tempResult)
        self.addType(tempType)
        if tempType == "int":
            if self.memory.mem_temp_int == 2000:
                raise Exception("Stack Overflow on temporal integer variables")
            self.temporalStack.append(self.memory.mem_temp_int)
            print(f'temporal {tempResult} (function {operand}) of type {tempType} assigned to {self.memory.mem_temp_int}')
            self.memory.mem_temp_int += 1
        elif tempType == "float":
            if self.memory.mem_temp_float == 4000:
                raise Exception("Stack Overflow on temporal float variables")
            self.temporalStack.append(self.memory.mem_temp_float)
            print(f'temporal {tempResult} (function {operand}) of type {tempType} assigned to {self.memory.mem_temp_float}')
            self.memory.mem_temp_float += 1
        elif tempType == "string":
            if self.memory.mem_local_string == 6000:
                raise Exception("Stack Overflow on temporal string variables")
            self.temporalStack.append(self.memory.mem_temp_string)
            print(f'temporal {tempResult} (function {operand}) of type {tempType} assigned to {self.memory.mem_temp_string}')
            self.memory.mem_temp_string += 1
        elif tempType == "bool":
            if self.memory.mem_local_bool == 8000:
                raise Exception("Stack Overflow on temporal bool variables")
            self.temporalStack.append(self.memory.mem_temp_bool)
            print(f'temporal {tempResult} (function {operand}) of type {tempType} assigned to {self.memory.mem_temp_bool}')
            self.memory.mem_temp_bool += 1
        elif tempType == "char":
            if self.memory.mem_local_char == 10000:
                raise Exception("Stack Overflow on temporal char variables")
            self.temporalStack.append(self.memory.mem_temp_char)
            print(f'temporal {tempResult} (function {operand}) of type {tempType} assigned to {self.memory.mem_temp_char}')
            self.memory.mem_temp_char += 1

    def addOperator(self, operator):
        self.operatorStack.append(operator)
        # print(operator)

    def update_parameters(self, id, vartype):
        if id not in self.currentFunction.parametersTable:
            self.currentFunction.parametersTable.append(Variable(id, vartype, None, -1))
            self.update_vars_table(id, vartype)
        else:
            print("You can't have two or more parameters with the same name")

    def update_vars_table(self, id, vartype):
        if id not in self.currentFunction.varsTable:
            if self.currentFunction.name == "global":
                if vartype == "int":
                    if self.memory.mem_global_int == 12000:
                        raise Exception("Stack Overflow on global integer variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_global_int)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_global_int}')
                    self.memory.mem_global_int += 1
                elif vartype == "float":
                    if self.memory.mem_global_float == 14000:
                        raise Exception("Stack Overflow on global float variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_global_float)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_global_float}')
                    self.memory.mem_global_float += 1
                elif vartype == "string":
                    if self.memory.mem_global_string == 16000:
                        raise Exception("Stack Overflow on global string variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_global_string)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_global_string}')
                    self.memory.mem_global_string += 1
                elif vartype == "bool":
                    if self.memory.mem_global_bool == 18000:
                        raise Exception("Stack Overflow on global bool variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_global_bool)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_global_bool}')
                    self.memory.mem_global_bool += 1
                elif vartype == "char":
                    if self.memory.mem_global_char == 20000:
                        raise Exception("Stack Overflow on global char variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_global_char)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_global_char}')
                    self.memory.mem_global_char += 1

            else:
                if vartype == "int":
                    if self.memory.mem_local_int == 22000:
                        raise Exception("Stack Overflow on local integer variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_local_int)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_local_int}')
                    self.memory.mem_local_int += 1
                elif vartype == "float":
                    if self.memory.mem_local_float == 24000:
                        raise Exception("Stack Overflow on local float variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_local_float)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_local_float}')
                    self.memory.mem_local_float += 1
                elif vartype == "string":
                    if self.memory.mem_local_string == 26000:
                        raise Exception("Stack Overflow on local string variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_local_string)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_local_string}')
                    self.memory.mem_local_string += 1
                elif vartype == "bool":
                    if self.memory.mem_local_bool == 28000:
                        raise Exception("Stack Overflow on local bool variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_local_bool)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_local_bool}')
                    self.memory.mem_local_bool += 1
                elif vartype == "char":
                    if self.memory.mem_local_char == 30000:
                        raise Exception("Stack Overflow on local char variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_local_char)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_local_char}')
                    self.memory.mem_local_char += 1
        else:
            print("You can't have two or more variables with the same name")

    def update_array_variable(self, id, index, vartype):
        index_num = int(index)
        self.currentFunction.varsTable[id].isArray = True
        self.currentFunction.varsCount += (index_num-1)
        if self.currentFunction.name == "global":
            if vartype == "int":
                if self.memory.mem_global_int + (index_num-1) >= 12000:
                    raise Exception("Stack Overflow on global integer variables")
                self.memory.mem_global_int += (index_num-1)
            elif vartype == "float":
                if self.memory.mem_global_float + (index_num - 1) >= 14000:
                    raise Exception("Stack Overflow on global float variables")
                self.memory.mem_global_float += (index_num - 1)
            elif vartype == "string":
                if self.memory.mem_global_string + (index_num - 1) >= 16000:
                    raise Exception("Stack Overflow on global string variables")
                self.memory.mem_global_string += (index_num - 1)
            elif vartype == "bool":
                if self.memory.mem_global_bool + (index_num - 1) >= 18000:
                    raise Exception("Stack Overflow on global bool variables")
                self.memory.mem_global_bool += (index_num - 1)
            elif vartype == "char":
                if self.memory.mem_global_char + (index_num - 1) >= 20000:
                    raise Exception("Stack Overflow on global char variables")
                self.memory.mem_global_char += (index_num - 1)

        else:
            if vartype == "int":
                if self.memory.mem_local_int + (index_num - 1) >= 22000:
                    raise Exception("Stack Overflow on local integer variables")
                self.memory.mem_local_int += (index_num - 1)
            elif vartype == "float":
                if self.memory.mem_local_float + (index_num - 1) >= 24000:
                    raise Exception("Stack Overflow on local float variables")
                self.memory.mem_local_float += (index_num - 1)
            elif vartype == "string":
                if self.memory.mem_local_string + (index_num - 1) >= 26000:
                    raise Exception("Stack Overflow on local string variables")
                self.memory.mem_local_string += (index_num - 1)
            elif vartype == "bool":
                if self.memory.mem_local_bool + (index_num - 1) >= 28000:
                    raise Exception("Stack Overflow on local bool variables")
                self.memory.mem_local_bool += (index_num - 1)
            elif vartype == "char":
                if self.memory.mem_local_char + (index_num - 1) >= 30000:
                    raise Exception("Stack Overflow on local char variables")
                self.memory.mem_local_char += (index_num - 1)

    def update_matrix_variable(self, id, first_index, second_index, vartype):
        memory_size = (int(first_index) * int(second_index)) - 1
        self.currentFunction.varsTable[id].isMatrix = True
        self.currentFunction.varsCount += (memory_size)

        if self.currentFunction.name == "global":
            if vartype == "int":
                if self.memory.mem_global_int + (memory_size) >= 12000:
                    raise Exception("Stack Overflow on global integer variables")
                self.memory.mem_global_int += (memory_size)
            elif vartype == "float":
                if self.memory.mem_global_float + (memory_size) >= 14000:
                    raise Exception("Stack Overflow on global float variables")
                self.memory.mem_global_float += (memory_size)
            elif vartype == "string":
                if self.memory.mem_global_string + (memory_size) >= 16000:
                    raise Exception("Stack Overflow on global string variables")
                self.memory.mem_global_string += (memory_size)
            elif vartype == "bool":
                if self.memory.mem_global_bool + (memory_size) >= 18000:
                    raise Exception("Stack Overflow on global bool variables")
                self.memory.mem_global_bool += (memory_size)
            elif vartype == "char":
                if self.memory.mem_global_char + (memory_size) >= 20000:
                    raise Exception("Stack Overflow on global char variables")
                self.memory.mem_global_char += (memory_size)

        else:
            if vartype == "int":
                if self.memory.mem_local_int + (memory_size) >= 22000:
                    raise Exception("Stack Overflow on local integer variables")
                self.memory.mem_local_int += (memory_size)
            elif vartype == "float":
                if self.memory.mem_local_float + (memory_size) >= 24000:
                    raise Exception("Stack Overflow on local float variables")
                self.memory.mem_local_float += (memory_size)
            elif vartype == "string":
                if self.memory.mem_local_string + (memory_size) >= 26000:
                    raise Exception("Stack Overflow on local string variables")
                self.memory.mem_local_string += (memory_size)
            elif vartype == "bool":
                if self.memory.mem_local_bool + (memory_size) >= 28000:
                    raise Exception("Stack Overflow on local bool variables")
                self.memory.mem_local_bool += (memory_size)
            elif vartype == "char":
                if self.memory.mem_local_char + (memory_size) >= 30000:
                    raise Exception("Stack Overflow on local char variables")
                self.memory.mem_local_char += (memory_size)


    def clear_local_memory(self):
        self.memory.mem_local_int = 20000
        self.memory.mem_local_float = 22000
        self.memory.mem_local_bool = 24000
        self.memory.mem_local_string = 26000
        self.memory.mem_local_char = 28000
        self.memory.mem_temp_int = 0
        self.memory.mem_temp_float = 2000
        self.memory.mem_temp_bool = 4000
        self.memory.mem_temp_string = 6000
        self.memory.mem_temp_char = 8000

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
            temporalsTaken = 0
            # reversed FOR because the parametersTable is reversed in relation to operandStack
            # example: funccall(0, 1, 2) --> passedParameter is the one we want to match with 2
            for idx,parameter in enumerate(reversed(self.functionTable[id].parametersTable)):
                passedParameter = self.operandStack.pop()
                passedParameterType = self.typesStack.pop()
                if(parameter.vartype != passedParameterType):
                    raise TypeError(f'Parameter {passedParameter} of type {passedParameterType} '
                                    f'cannot be matched with {parameter.vartype}')
                else:
                    parameterAddress = None
                    if passedParameter in self.currentFunction.varsTable:
                        parameterAddress = self.currentFunction.varsTable[passedParameter].address
                    elif passedParameter in self.functionTable["global"].varsTable:
                        parameterAddress = self.functionTable["global"].varsTable[passedParameter].address
                    elif passedParameter in self.constantTable:
                        parameterAddress = self.constantTable[passedParameter].address
                    else:
                        parameterAddress = self.temporalStack[len(self.temporalStack)-1-temporalsTaken]
                        temporalsTaken += 1

                    quad = Quadruple("param",parameterAddress,None,f'par{currentCounter-idx-1}')
                    self.quadruples.append(quad)
                    print("parametro bueno")
                    print("param",parameterAddress,None,f'par{currentCounter-idx-1}')
        else:
            raise ValueError(f'Number of parameters in call to function {id} does not match the amount declared.')

    def goto_function_quad(self, id):
        quad = Quadruple('GOSUB', None, None, self.functionTable[id].startQuadruple)
        print('GOSUB', 'None', 'None', self.functionTable[id].startQuadruple)
        self.quadruples.append(quad)


    def create_return_endfunc_goto(self):
        #checar que el tipo del operando sea el mismo que el de la function
        #checar en donde esta el operando (global, local, temporal, constante, etc.)
        #obtener la direccion del operando
        #regresar la direccion del operando

        if self.currentFunction.returntype != "void":
            result = self.operandStack.pop()
            resultType = self.typesStack.pop()
            if resultType != self.currentFunction.returntype:
                raise TypeError(f'Cannot return type {resultType} in function {self.currentFunction.name}')
            resultAddress = None
            if result in self.currentFunction.varsTable:
                resultAddress = self.currentFunction.varsTable[result].address
            elif result in self.functionTable["global"].varsTable:
                resultAddress = self.functionTable["global"].varsTable[result].address
            elif result in self.constantTable:
                resultAddress = self.constantTable[result].address
            else:
                resultAddress = self.temporalStack[-1]

            quad = Quadruple('RETURN', None, None, resultAddress)
            print('RETURN', None, None, resultAddress)
            self.quadruples.append(quad)
        else:
            raise TypeError(f'Void function {self.currentFunction.name} cannot have a return statement.')

    def create_endfunc(self):
        quad = Quadruple('ENDFUNC', None, None, None)
        print('ENDFUNC', None, None, None)
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
                conditionAddress = None
                if conditionVar in self.currentFunction.varsTable:
                    conditionAddress = self.currentFunction.varsTable[conditionVar].address
                elif conditionVar in self.functionTable["global"].varsTable:
                    conditionAddress = self.functionTable["global"].varsTable[conditionVar].address
                elif conditionVar in self.constantTable:
                    conditionAddress = self.constantTable[conditionVar].address
                else:
                    conditionAddress = self.temporalStack[-1]
                print(f'GOTOF, {conditionVar} {conditionAddress} None "_')
                quad = Quadruple("GOTOF", conditionAddress, None, "_")
                # this quadruple's index must be saved for later
                self.jumpStack.append(len(self.quadruples))
                self.quadruples.append(quad)
            else:
                raise TypeError(f'Error: {conditionVar} is not a boolean')

    def generateEndIfQuad(self):
        # popping
        false = self.jumpStack.pop()
        # fill the previous quadruple's GOTOF value with the current quadruple index
        print(f'filled endif quadruple {false} with {len(self.quadruples)}')
        self.quadruples[false].resultTemp = len(self.quadruples)

    def generateGoToQuad(self):
        # if there was an else, you are here
        # this GOTO will redirect the end of an if block to the end of the conditional statute
        print(f'Created GOTO at the end of the if block: GOTO None None _')
        quad = Quadruple("GOTO", None, None, "_")
        self.quadruples.append(quad)

        # BUT FIRST! we have to make sure that the previously saved GOTOF from the if redirects to this else
        # ALSO, we have to point the GOTO to the end of the conditional statue, as said earlier.
        self.generateEndIfQuad()

        # So we append the GOTO's current index (length-1) to the jumpstack, AFTER having
        # popped the other jump previously saved
        self.jumpStack.append(len(self.quadruples) - 1)

    def addFromVarOperand(self, operand):
        print("agrega fromvaroperand")
        if operand in self.currentFunction.varsTable:
            if self.currentFunction.varsTable[operand].vartype == "int":
                operandAddress = self.currentFunction.varsTable[operand].address

                # Add the current operand to the From Variable Stack to keep its address for future reference.
                # We will need its address to be able to modify it
                self.loopVariableStack.append(operandAddress)
                self.operandStack.append(operand)
                self.addType(self.currentFunction.varsTable[operand].vartype)
            else:
                raise TypeError(f'The variable {operand} is not an int')
        elif operand in self.functionTable["global"].varsTable:
            if self.functionTable["global"].varsTable[operand].vartype == "int":
                operandAddress = self.functionTable["global"].varsTable[operand].address

                # Add the current operand to the From Variable Stack to keep its address for future reference.
                # We will need its address to be able to modify it
                self.loopVariableStack.append(operandAddress)
                self.operandStack.append(operand)
                self.addType(self.functionTable["global"].varsTable[operand].vartype)
            else:
                raise TypeError(f'The variable {operand} is not an int')
        else:
            raise ValueError(f'The variable {operand} is not declared')

    def generateFromBeforeCheck(self):
        print("From Before Check")
        self.jumpStack.append(len(self.quadruples))

    def generateEndFromQuad(self):
        print("From End")
        # Get the index of the beginning of the from statute
        fromAfterCheckIndex = self.jumpStack.pop()
        fromBeforeCheckIndex = self.jumpStack.pop()

        # add 1 to the from index
        tempResult = 'X' + str(len(self.temporalStack))
        if self.memory.mem_local_int == 2000:
            raise Exception("Stack Overflow on temporal int variables")
        self.temporalStack.append(self.memory.mem_temp_int)
        print(f'temporal {tempResult} of type int assigned to {self.memory.mem_temp_int}')
        self.memory.mem_temp_int += 1
        print(f'+ (from index) {self.loopVariableStack[-1]} 1 {tempResult} {self.temporalStack[-1]}')
        quad1 = Quadruple("+", self.loopVariableStack[-1], "1", self.temporalStack[-1])
        self.quadruples.append(quad1)

        # Append the current GOTO quadruple, to go back to the beginning of the from
        quad2 = Quadruple("GOTO", None, None, fromBeforeCheckIndex)
        print("GOTO BEGIN OF FROM", None, None, fromBeforeCheckIndex)
        self.quadruples.append(quad2)
        print(f'FILLING Quad After checking from index {fromAfterCheckIndex} GOTO to {len(self.quadruples)}')
        self.quadruples[fromAfterCheckIndex].resultTemp = len(self.quadruples)
        self.loopVariableStack.pop()

    def generateFromAfterCheck(self):
        print("From After Check")
        if len(self.operandStack) != 0:
            expResult = self.operandStack.pop()
            typeExpResult = self.typesStack.pop()
            # Get the initial variable of the from loop
            fromVarAddress = self.loopVariableStack[-1]
            if typeExpResult == "int":
                expResultAddress = None
                if expResult in self.currentFunction.varsTable:
                    expResultAddress = self.currentFunction.varsTable[expResult].address
                elif expResult in self.functionTable["global"].varsTable:
                    expResultAddress = self.functionTable["global"].varsTable[expResult].address
                elif expResult in self.constantTable:
                    expResultAddress = self.constantTable[expResult].address
                else:
                    expResultAddress = self.temporalStack[-1]

                tempResult = 'X' + str(len(self.temporalStack))

                if self.memory.mem_local_bool == 8000:
                    raise Exception("Stack Overflow on temporal bool variables")
                self.temporalStack.append(self.memory.mem_temp_bool)
                print(f'temporal {tempResult} of type bool assigned to {self.memory.mem_temp_bool}')
                self.memory.mem_temp_bool += 1

                # Aqui vamos a tener que sacar el valor de fromVar, para poder compararlo con expResult
                # una vez comparado, tenemos fromConditionResult y ese es el que ponemos en el quad.
                # fromConditionResult = fromVar <= expResult
                quad1 = Quadruple('<', fromVarAddress, expResultAddress, self.temporalStack[-1])
                print(f'< (from index) {fromVarAddress} {expResult} {expResultAddress} {tempResult} {self.temporalStack[-1]}')
                self.quadruples.append(quad1)

                print(f'GOTOF {tempResult} {self.temporalStack[-1]} None _')
                quad2 = Quadruple("GOTOF", self.temporalStack[-1], None, "_")
                # this quadruple's index must be saved for later
                self.jumpStack.append(len(self.quadruples))
                self.quadruples.append(quad2)
            else:
                raise TypeError(f'Error: The expression resulting in {expResult} must be an integer')

    def generateWhileBeforeCheck(self):
        print("While Before Check", len(self.quadruples))
        self.jumpStack.append(len(self.quadruples))

    def generateWhileAfterCheck(self):
        print("While After Check")
        if len(self.operandStack) != 0:
            conditionVar = self.operandStack.pop()
            typeConditionVar = self.typesStack.pop()
            if typeConditionVar == "bool":
                print(f"CONDITIONVAR: {conditionVar}")
                self.addWhileVarOperand(conditionVar)
                whileVarAddress = self.loopVariableStack[-1]
                print(f'whileVarAddress {self.loopVariableStack[-1]}')
                quad = Quadruple("GOTOF", whileVarAddress, None, "_")
                # this quadruple's index must be saved for later
                self.jumpStack.append(len(self.quadruples))
                self.quadruples.append(quad)
                print("GOTOF", conditionVar, whileVarAddress, None, "_")
            else:
                raise TypeError(f'Error: {conditionVar} is not a boolean')

    def addWhileVarOperand(self, operand):
        if operand in self.currentFunction.varsTable:
            operandAddress = self.currentFunction.varsTable[operand].address

            # Add the current operand to the From Variable Stack to keep its address for future reference.
            # We will need its address to be able to modify it
            self.loopVariableStack.append(operandAddress)
            #self.operandStack.append(operand)
            #self.addType(self.currentFunction.varsTable[operand].vartype)
            print(f'WHILEVAROPERAND OPERANDADDRESS {operandAddress}')
        elif operand in self.functionTable["global"].varsTable:
            operandAddress = self.functionTable["global"].varsTable[operand].address

            # Add the current operand to the From Variable Stack to keep its address for future reference.
            # We will need its address to be able to modify it
            self.loopVariableStack.append(operandAddress)
            #self.operandStack.append(operand)
            #self.addType(self.functionTable["global"].varsTable[operand].vartype)
            print(f'WHILEVAROPERAND OPERANDADDRESS {operandAddress}')
        elif operand != "true" and operand != "false":
            operandAddress = self.temporalStack[-1]
            self.loopVariableStack.append(operandAddress)
            #self.operandStack.append(operand)
            #self.addType("bool")
            print(f'WHILEVAROPERAND OPERANDADDRESS {operandAddress}')
        else:
            if operand == "true" or operand == "false":
                raise TypeError(f'Error: constant {operand} will cause infinite execution of while loop.')
            raise TypeError(f'Error: variable {operand} does not exist.')

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
            print("read", operand, self.currentFunction.varsTable[operand].address, None, "-")
            quad = Quadruple("read", self.currentFunction.varsTable[operand].address, None, "_")
            self.quadruples.append(quad)
        elif operand in self.functionTable["global"].varsTable:
            print("read", operand, self.functionTable["global"].varsTable[operand].address, None, "-")
            quad = Quadruple("read", self.functionTable["global"].varsTable[operand].address, None, "_")
            self.quadruples.append(quad)
        else:
            raise ValueError(f'The variable {operand} is not declared')

    def generateWriteQuad(self):
        if len(self.operandStack) == 0:
            raise Exception("Empty print statement")
        printedOperand = self.operandStack.pop()
        self.typesStack.pop()

        if printedOperand in self.currentFunction.varsTable:
            print("print", printedOperand, self.currentFunction.varsTable[printedOperand].address, None, "_")
            quad = Quadruple("print", self.currentFunction.varsTable[printedOperand].address, None, "_")
            self.quadruples.append(quad)
        elif printedOperand in self.functionTable["global"].varsTable:
            print("print", printedOperand, self.functionTable["global"].varsTable[printedOperand].address, None, "_")
            quad = Quadruple("print", self.functionTable["global"].varsTable[printedOperand].address, None, "_")
            self.quadruples.append(quad)
        elif printedOperand in self.constantTable:
            print("print", printedOperand, self.constantTable[printedOperand].address, None, "_")
            quad = Quadruple("print", self.constantTable[printedOperand].address, None, "_")
            self.quadruples.append(quad)
        else:
            print("print", printedOperand, self.temporalStack[-1], None, "_")
            quad = Quadruple("print", self.temporalStack[-1], None, "_")
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

            roAddress = None
            if rightOperand in self.currentFunction.varsTable:
                roAddress = self.currentFunction.varsTable[rightOperand].address
            elif rightOperand in self.functionTable["global"].varsTable:
                roAddress = self.functionTable["global"].varsTable[rightOperand].address
            elif rightOperand in self.constantTable:
                roAddress = self.constantTable[rightOperand].address
            else:
                roAddress = self.temporalStack[-1]

            loAddress = None
            if leftOperand in self.currentFunction.varsTable:
                loAddress = self.currentFunction.varsTable[leftOperand].address
            elif leftOperand in self.functionTable["global"].varsTable:
                loAddress = self.functionTable["global"].varsTable[leftOperand].address
            elif leftOperand in self.constantTable:
                loAddress = self.constantTable[leftOperand].address

            quad = Quadruple(operator, loAddress, roAddress, "_")
            self.quadruples.append(quad)

            self.operandStack.append(leftOperand)
            self.typesStack.append(leftOperandType)
            print(operator, leftOperand, loAddress, rightOperand, roAddress)

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

            # Get the operands' addresses
            roAddress = None
            if rightOperand in self.currentFunction.varsTable:
                roAddress = self.currentFunction.varsTable[rightOperand].address
            elif rightOperand in self.functionTable["global"].varsTable:
                roAddress = self.functionTable["global"].varsTable[rightOperand].address
            elif rightOperand in self.constantTable:
                roAddress = self.constantTable[rightOperand].address
            else:
                roAddress = self.temporalStack[int(rightOperand[1:])]

            loAddress = None
            if leftOperand in self.currentFunction.varsTable:
                loAddress = self.currentFunction.varsTable[leftOperand].address
            elif leftOperand in self.functionTable["global"].varsTable:
                loAddress = self.functionTable["global"].varsTable[leftOperand].address
            elif leftOperand in self.constantTable:
                loAddress = self.constantTable[leftOperand].address
            else:
                loAddress = self.temporalStack[int(leftOperand[1:])]

            tempResult = 'X' + str(len(self.temporalStack))

            temptype = self.scube.cube[leftOperandType][operator][rightOperandType]
            if temptype == "int":
                if self.memory.mem_temp_int == 2000:
                    raise Exception("Stack Overflow on temporal integer variables")
                self.temporalStack.append(self.memory.mem_temp_int)
                print(f'temporal {tempResult} of type {temptype} assigned to {self.memory.mem_temp_int}')
                self.memory.mem_temp_int += 1
            elif temptype == "float":
                if self.memory.mem_temp_float == 4000:
                    raise Exception("Stack Overflow on temporal float variables")
                self.temporalStack.append(self.memory.mem_temp_float)
                print(f'temporal {tempResult} of type {temptype} assigned to {self.memory.mem_temp_float}')
                self.memory.mem_temp_float += 1
            elif temptype == "string":
                if self.memory.mem_local_string == 6000:
                    raise Exception("Stack Overflow on temporal string variables")
                self.temporalStack.append(self.memory.mem_temp_string)
                print(f'temporal {tempResult} of type {temptype} assigned to {self.memory.mem_temp_string}')
                self.memory.mem_temp_string += 1
            elif temptype == "bool":
                if self.memory.mem_local_bool == 8000:
                    raise Exception("Stack Overflow on temporal bool variables")
                self.temporalStack.append(self.memory.mem_temp_bool)
                print(f'temporal {tempResult} of type {temptype} assigned to {self.memory.mem_temp_bool}')
                self.memory.mem_temp_bool += 1
            elif temptype == "char":
                if self.memory.mem_local_char == 10000:
                    raise Exception("Stack Overflow on temporal char variables")
                self.temporalStack.append(self.memory.mem_temp_char)
                print(f'temporal {tempResult} of type {temptype} assigned to {self.memory.mem_temp_char}')
                self.memory.mem_temp_char += 1

            # Create Quad and add it to Quadruples Stack
            quad = Quadruple(operator, loAddress, roAddress, self.temporalStack[-1])
            print(operator, leftOperand, loAddress, rightOperand, roAddress, tempResult, self.temporalStack[-1])
            self.quadruples.append(quad)

            # Add result back to the Operand Stack
            self.addOperand(tempResult)

            # Add type to type stack
            self.addType(temptype)
