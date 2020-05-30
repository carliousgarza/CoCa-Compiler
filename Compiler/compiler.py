from antlr4 import *
from Compiler.function import *
from Compiler.variable import *
from Compiler.quadruple import *
from Compiler.semanticCube import *
from Compiler.constant import *
from Compiler.temporalDimensionVariable import *
from Memory.memory import Memory
import operator


class Compiler:
    def __init__(self):
        self.functionTable = {}
        self.currentFunction = Function("global", "void", [], {})
        self.constantTable = {}
        self.realConstantTable = {}
        self.quadruples = []
        self.operatorStack = []
        self.operandStack = []
        self.jumpStack = []
        self.typesStack = []
        self.scube = SemanticCube()
        self.loopVariableStack = []
        self.functionStack = []
        self.memory = Memory()
        self.temporalStack = []
        self.temporalDimensionVariableStack = []
        print("compiling...")

    def get_quadruples(self):
        return self.quadruples

    def get_constants_table(self):
        return self.realConstantTable

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
            if self.memory.mem_constant < 40000:
                self.constantTable[self.operandStack[-1]] = Constant(vartype, self.memory.mem_constant, self.operandStack[-1])
                print(f'added constant {vartype} {self.operandStack[-1]} to {self.memory.mem_constant}')
                self.realConstantTable[self.memory.mem_constant] = Constant(vartype, self.memory.mem_constant, self.operandStack[-1])
                self.memory.mem_constant += 1
            else:
                raise Exception(f'StackOverflow on constants')

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
            if self.memory.mem_temp_string == 6000:
                raise Exception("Stack Overflow on temporal string variables")
            self.temporalStack.append(self.memory.mem_temp_string)
            print(f'temporal {tempResult} (function {operand}) of type {tempType} assigned to {self.memory.mem_temp_string}')
            self.memory.mem_temp_string += 1
        elif tempType == "bool":
            if self.memory.mem_temp_bool == 8000:
                raise Exception("Stack Overflow on temporal bool variables")
            self.temporalStack.append(self.memory.mem_temp_bool)
            print(f'temporal {tempResult} (function {operand}) of type {tempType} assigned to {self.memory.mem_temp_bool}')
            self.memory.mem_temp_bool += 1
        elif tempType == "char":
            if self.memory.mem_temp_char == 10000:
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
                    if self.memory.mem_global_int >= 12000:
                        raise Exception("Stack Overflow on global integer variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_global_int)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_global_int}')
                    self.memory.mem_global_int += 1
                elif vartype == "float":
                    if self.memory.mem_global_float >= 14000:
                        raise Exception("Stack Overflow on global float variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_global_float)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_global_float}')
                    self.memory.mem_global_float += 1
                elif vartype == "string":
                    if self.memory.mem_global_string >= 16000:
                        raise Exception("Stack Overflow on global string variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_global_string)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_global_string}')
                    self.memory.mem_global_string += 1
                elif vartype == "bool":
                    if self.memory.mem_global_bool >= 18000:
                        raise Exception("Stack Overflow on global bool variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_global_bool)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_global_bool}')
                    self.memory.mem_global_bool += 1
                elif vartype == "char":
                    if self.memory.mem_global_char >= 20000:
                        raise Exception("Stack Overflow on global char variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_global_char)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_global_char}')
                    self.memory.mem_global_char += 1

            else:
                if vartype == "int":
                    if self.memory.mem_local_int >= 22000:
                        raise Exception("Stack Overflow on local integer variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_local_int)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_local_int}')
                    self.memory.mem_local_int += 1
                elif vartype == "float":
                    if self.memory.mem_local_float >= 24000:
                        raise Exception("Stack Overflow on local float variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_local_float)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_local_float}')
                    self.memory.mem_local_float += 1
                elif vartype == "string":
                    if self.memory.mem_local_string >= 26000:
                        raise Exception("Stack Overflow on local string variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_local_string)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_local_string}')
                    self.memory.mem_local_string += 1
                elif vartype == "bool":
                    if self.memory.mem_local_bool >= 28000:
                        raise Exception("Stack Overflow on local bool variables")
                    self.currentFunction.varsTable[id] = Variable(id, vartype, None, self.memory.mem_local_bool)
                    self.currentFunction.varsCount += 1
                    print(f'variable {id} of type {vartype} assigned to {self.memory.mem_local_bool}')
                    self.memory.mem_local_bool += 1
                elif vartype == "char":
                    if self.memory.mem_local_char >= 30000:
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
        self.currentFunction.varsTable[id].size = index_num
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
        self.currentFunction.varsTable[id].size = memory_size+1
        self.currentFunction.varsTable[id].first_index = int(first_index)
        self.currentFunction.varsTable[id].second_index = int(second_index)
        self.currentFunction.varsCount += memory_size

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

    def verify_one_index(self):
        id = self.operandStack.pop(-2)
        arrayType = self.typesStack.pop()
        baseAddress = None
        dimSize = None
        if id in self.currentFunction.varsTable:
            if not self.currentFunction.varsTable[id].isArray:
                raise Exception(f'Error: wrong dimensions entered in {id}')
            baseAddress = self.currentFunction.varsTable[id].address
            dimSize = self.currentFunction.varsTable[id].size
        elif id in self.functionTable["global"].varsTable:
            if not self.functionTable["global"].varsTable[id].isArray:
                raise Exception(f'Error: wrong dimensions entered in {id}')
            baseAddress = self.functionTable["global"].varsTable[id].address
            dimSize = self.functionTable["global"].varsTable[id].size
        else:
            raise Exception(f'List {id} is not declared')

        if baseAddress not in self.constantTable:
            if self.memory.mem_constant < 40000:
                self.constantTable[baseAddress] = Constant('int', self.memory.mem_constant, baseAddress)
                self.realConstantTable[self.memory.mem_constant] = Constant('int', self.memory.mem_constant, baseAddress)
                self.memory.mem_constant += 1
            else:
                raise Exception(f'StackOverflow on constants')
        if '0' not in self.constantTable:
            if self.memory.mem_constant < 40000:
                self.constantTable['0'] = Constant('int', self.memory.mem_constant, '0')
                self.realConstantTable[self.memory.mem_constant] = Constant('int', self.memory.mem_constant, '0')
                self.memory.mem_constant += 1
            else:
                raise Exception(f'StackOverflow on constants')
        if str(int(dimSize)-1) not in self.constantTable:
            if self.memory.mem_constant < 40000:
                self.constantTable[str(int(dimSize)-1)] = Constant('int', self.memory.mem_constant, str(int(dimSize)-1))
                self.realConstantTable[self.memory.mem_constant] = Constant('int', self.memory.mem_constant, str(int(dimSize)-1))
                self.memory.mem_constant += 1
            else:
                raise Exception(f'StackOverflow on constants')

        indexOperand = self.operandStack.pop()
        indexType = self.typesStack.pop()

        if indexType != 'int':
            raise TypeError(f'Index value for array {id} is not an integer')

        indexOperandAddress = None
        if indexOperand in self.currentFunction.varsTable:
            indexOperandAddress = self.currentFunction.varsTable[indexOperand].address
        elif indexOperand in self.functionTable["global"].varsTable:
            indexOperandAddress = self.functionTable["global"].varsTable[indexOperand].address
        elif indexOperand in self.constantTable:
            indexOperandAddress = self.constantTable[indexOperand].address
        else:
            indexOperandAddress = self.temporalStack[-1]

        verifyQuad = Quadruple('VERIF', indexOperandAddress, self.constantTable['0'].address, self.constantTable[str(int(dimSize) - 1)].address)
        print(f'VERIF {indexOperand} {indexOperandAddress} between 0 and {int(dimSize)-1}')
        self.quadruples.append(verifyQuad)

        pointerResult = 'P' + str(len(self.temporalStack))
        if self.memory.mem_pointers == 50000:
            raise Exception("Stack Overflow on temporal pointer variables")
        self.temporalStack.append(self.memory.mem_pointers)
        print(f'temporal pointer {pointerResult} of type array index assigned to {self.memory.mem_pointers}')
        self.memory.mem_pointers += 1

        baseAddressQuad = Quadruple('+', self.constantTable[baseAddress].address, indexOperandAddress, self.temporalStack[-1])
        print(f'+ {baseAddress} {self.constantTable[baseAddress].address} {indexOperand} {indexOperandAddress} {self.temporalStack[-1]}')
        self.quadruples.append(baseAddressQuad)
        self.addOperand(pointerResult)
        self.addType(arrayType)


    def verify_two_indexes(self):
        id = self.operandStack.pop(-3)
        matrixType = self.typesStack.pop()
        baseAddress = None
        dimSize = None
        firstIndex = None
        secondIndex = None
        if id in self.currentFunction.varsTable:
            if not self.currentFunction.varsTable[id].isMatrix:
                raise Exception(f'Error: wrong dimensions entered in {id}')
            baseAddress = self.currentFunction.varsTable[id].address
            dimSize = self.currentFunction.varsTable[id].size
            firstIndex = self.currentFunction.varsTable[id].first_index
            secondIndex = self.currentFunction.varsTable[id].second_index
        elif id in self.functionTable["global"].varsTable:
            if not self.functionTable["global"].varsTable[id].isMatrix:
                raise Exception(f'Error: wrong dimensions entered in {id}')
            baseAddress = self.functionTable["global"].varsTable[id].address
            dimSize = self.functionTable["global"].varsTable[id].size
            firstIndex = self.functionTable["global"].varsTable[id].first_index
            secondIndex = self.functionTable["global"].varsTable[id].second_index
        else:
            raise Exception(f'Matrix {id} is not declared')


        # IF THESE VALUES ARE NOT ALLOCATED IN MEMORY, THEY MUST BE ALLOCATED NOW
        # AS THEY WILL BE NEEDED FOR OPERATIONS

        if baseAddress not in self.constantTable:
            if self.memory.mem_constant < 40000:
                self.constantTable[baseAddress] = Constant('int', self.memory.mem_constant, baseAddress)
                self.realConstantTable[self.memory.mem_constant] = Constant('int', self.memory.mem_constant, baseAddress)
                self.memory.mem_constant += 1
            else:
                raise Exception(f'StackOverflow on constants')
        if '0' not in self.constantTable:
            if self.memory.mem_constant < 40000:
                self.constantTable['0'] = Constant('int', self.memory.mem_constant, '0')
                self.realConstantTable[self.memory.mem_constant] = Constant('int', self.memory.mem_constant, '0')
                self.memory.mem_constant += 1
            else:
                raise Exception(f'StackOverflow on constants')
        if str(int(firstIndex)-1) not in self.constantTable:
            if self.memory.mem_constant < 40000:
                self.constantTable[str(int(firstIndex)-1)] = Constant('int', self.memory.mem_constant, str(int(firstIndex)-1))
                self.realConstantTable[self.memory.mem_constant] = Constant('int', self.memory.mem_constant, str(int(firstIndex)-1))
                self.memory.mem_constant += 1
            else:
                raise Exception(f'StackOverflow on constants')
        if firstIndex not in self.constantTable:
            if self.memory.mem_constant < 40000:
                self.constantTable[firstIndex] = Constant('int', self.memory.mem_constant, firstIndex)
                self.realConstantTable[self.memory.mem_constant] = Constant('int', self.memory.mem_constant, firstIndex)
                self.memory.mem_constant += 1
            else:
                raise Exception(f'StackOverflow on constants')
        if str(int(secondIndex)-1) not in self.constantTable:
            if self.memory.mem_constant < 40000:
                self.realConstantTable[self.memory.mem_constant] = Constant('int', self.memory.mem_constant, str(int(secondIndex)-1))
                self.memory.mem_constant += 1
            else:
                raise Exception(f'StackOverflow on constants')
        if secondIndex not in self.constantTable:
            if self.memory.mem_constant < 40000:
                self.constantTable[secondIndex] = Constant('int', self.memory.mem_constant, secondIndex)
                self.realConstantTable[self.memory.mem_constant] = Constant('int', self.memory.mem_constant, secondIndex)
                self.memory.mem_constant += 1
            else:
                raise Exception(f'StackOverflow on constants')


        # POPPING OUT THE RESULTS FOR SECOND AND FIRST INDEX OPERANDS AND TYPECHECKING THEM

        secondIndexOperand = self.operandStack.pop()
        secondIndexType = self.typesStack.pop()

        if secondIndexType != 'int':
            raise TypeError(f'Second index value for array {id} is not an integer')

        firstIndexOperand = self.operandStack.pop()
        firstIndexType = self.typesStack.pop()

        if firstIndexType != 'int':
            raise TypeError(f'First index value for array {id} is not an integer')


        # GET THE ADDRESS OF THE SECOND AND FIRST INDEX OPERANDS, BE IT A LOCAL VAR, GLOBAL VAR, TEMPORAL, OR CONSTANT

        firstIndexOperandAddress = None
        if firstIndexOperand in self.currentFunction.varsTable:
            firstIndexOperandAddress = self.currentFunction.varsTable[firstIndexOperand].address
        elif firstIndexOperand in self.functionTable["global"].varsTable:
            firstIndexOperandAddress = self.functionTable["global"].varsTable[firstIndexOperand].address
        elif firstIndexOperand in self.constantTable:
            firstIndexOperandAddress = self.constantTable[firstIndexOperand].address
        else:
            firstIndexOperandAddress = self.temporalStack[-1]

        secondIndexOperandAddress = None
        if secondIndexOperand in self.currentFunction.varsTable:
            secondIndexOperandAddress = self.currentFunction.varsTable[secondIndexOperand].address
        elif secondIndexOperand in self.functionTable["global"].varsTable:
            secondIndexOperandAddress = self.functionTable["global"].varsTable[secondIndexOperand].address
        elif secondIndexOperand in self.constantTable:
            secondIndexOperandAddress = self.constantTable[secondIndexOperand].address
        else:
            secondIndexOperandAddress = self.temporalStack[-1]


        # CREATE A VERIFICATION QUAD FOR THE FIRST INDEX
        # FIRST INDEX OPERAND MUST BE BETWEEN 0 AND THE FIRST DIMENSION SIZE - 1. THE 0 AND FIRST DIMENSION SIZE ARE STORED NOW IN CONSTANT TABLE

        verifyFirstQuad = Quadruple('VERIF', firstIndexOperandAddress, self.constantTable['0'].address, self.constantTable[str(int(firstIndex)-1)].address)
        print(f'VERIF {firstIndexOperand} {firstIndexOperandAddress} between 0 and {int(firstIndex)-1}')
        self.quadruples.append(verifyFirstQuad)

        # SAME BUT FOR SECOND INDEX OPERAND

        verifySecondQuad = Quadruple('VERIF', secondIndexOperandAddress, self.constantTable['0'].address, self.constantTable[str(int(secondIndex)-1)].address)
        print(f'VERIF {secondIndexOperand} {secondIndexOperandAddress} between 0 and {int(secondIndex)-1}')
        self.quadruples.append(verifySecondQuad)

        # NOW WE NAVIGATE TO THE LOCATION OF OUR FIRST INDEX BY MULTIPLYING THE FIRST INDEX OPERAND BY THE SECOND DIMENSION'S SIZE
        # WE GENERATE A QUAD FOR THAT, OF COURSE

        firstIndexLocationTemp = 'X' + str(len(self.temporalStack))
        if self.memory.mem_temp_int == 2000:
            raise Exception("Stack Overflow on temporal int variables")
        firstIndexLocationQuad = Quadruple('*', self.constantTable[secondIndex].address, firstIndexOperandAddress, self.memory.mem_temp_int)
        print(f'* {secondIndex} {self.constantTable[secondIndex].address} {firstIndexOperand} {firstIndexOperandAddress} {self.memory.mem_temp_int}')
        print(f'temporal {firstIndexLocationTemp} of type int assigned to {self.memory.mem_temp_int}')
        self.temporalStack.append(self.memory.mem_temp_int)
        self.memory.mem_temp_int += 1
        self.quadruples.append(firstIndexLocationQuad)


        # NOW WE NAVIGATE TO THE LOCATION OF OUR SECOND INDEX OPERAND BY ADDING THE PREVIOUS MULTIPLICATION TO OUR SECOND INDEX OPERAND
        # AND WE MAKE THE QUAD

        secondIndexLocationTemp = 'X' + str(len(self.temporalStack))
        if self.memory.mem_temp_int == 2000:
            raise Exception("Stack Overflow on temporal int variables")
        secondIndexLocationQuad = Quadruple('+', self.temporalStack[-1], secondIndexOperandAddress, self.memory.mem_temp_int)
        print(f'+ {firstIndexLocationTemp} {self.temporalStack[-1]} {secondIndexOperand} {secondIndexOperandAddress} {self.memory.mem_temp_int}')
        print(f'temporal {secondIndexLocationTemp} of type int assigned to {self.memory.mem_temp_int}')
        self.temporalStack.append(self.memory.mem_temp_int)
        self.memory.mem_temp_int += 1
        self.quadruples.append(secondIndexLocationQuad)

        # THE PREVIOUS ADDITION IS NOW ADDED TO THE BASE ADDRESS AND WE MAKE A QUAD FOR IT TOO

        baseAddressQuad = Quadruple('+', self.constantTable[baseAddress].address, self.temporalStack[-1], self.memory.mem_pointers)
        print(f'+ {baseAddress} {self.constantTable[baseAddress].address} {secondIndexLocationTemp} {self.temporalStack[-1]} {self.memory.mem_pointers}')
        self.quadruples.append(baseAddressQuad)

        # WE STORE THE WHOLE RESULT IN POINTER MEMORY, AS THE RESULT IS A MEMORY VALUE ALLOCATED TO A MEMORY ADDRESS.

        pointerResult = 'P' + str(len(self.temporalStack))
        if self.memory.mem_pointers == 50000:
            raise Exception("Stack Overflow on temporal pointer variables")
        print(f'temporal pointer {pointerResult} of type matrix index assigned to {self.memory.mem_pointers}')
        self.temporalStack.append(self.memory.mem_pointers)
        self.memory.mem_pointers += 1

        # THE RESULTING ADDRESS MUST BE ADDED TO THE OPERAND STACK NOW, WITH THE MATRIX TYPE, FOR WHATEVER THE NEXT STEP IS

        self.addOperand(pointerResult)
        self.addType(matrixType)




    def generate_matrix_operation_quad(self, operator):
        operand = self.operandStack.pop()
        operandType = self.typesStack.pop()
        size = None
        address = None
        isMatrix = False
        firstIndex = None
        secondIndex = None

        if operand in self.currentFunction.varsTable:
            size = self.currentFunction.varsTable[operand].size
            address= self.currentFunction.varsTable[operand].address
            isMatrix = self.currentFunction.varsTable[operand].isMatrix
            if isMatrix:
                firstIndex = self.currentFunction.varsTable[operand].first_index
                secondIndex = self.currentFunction.varsTable[operand].second_index

        elif operand in self.functionTable["global"].varsTable:
            size = self.functionTable["global"].varsTable[operand].size
            address = self.functionTable["global"].varsTable[operand].address
            isMatrix = self.functionTable["global"].varsTable[operand].isMatrix
            if isMatrix:
                firstIndex = self.functionTable["global"].varsTable[operand].first_index
                secondIndex = self.functionTable["global"].varsTable[operand].second_index
        else:
            raise Exception(f'{operand} is not declared')

        newFirstIndex = firstIndex
        newSecondIndex = secondIndex

        if operator == '#':
            newFirstIndex = secondIndex
            newSecondIndex = firstIndex

        if isMatrix:
            tempResult = 'M' + str(len(self.temporalDimensionVariableStack))
            if operandType == "int":
                if self.memory.mem_temp_int+size >= 2000:
                    raise Exception("Stack Overflow on temporal integer variables")
                print(f'temporal {tempResult} of type {operandType} assigned to {self.memory.mem_temp_int}')
                self.temporalDimensionVariableStack.append(TemporalDimensionVariable
                                                     (self.memory.mem_temp_int, newFirstIndex, newSecondIndex, operandType, size))
                self.memory.mem_temp_int += size
            elif operandType == "float":
                if self.memory.mem_temp_float+size >= 4000:
                    raise Exception("Stack Overflow on temporal float variables")
                print(f'temporal {tempResult} of type {operandType} assigned to {self.memory.mem_temp_float}')
                self.temporalDimensionVariableStack.append(TemporalDimensionVariable
                                                     (self.memory.mem_temp_float, newFirstIndex, newSecondIndex, operandType, size))
                self.memory.mem_temp_float += size
            elif operandType == "string":
                if self.memory.mem_temp_string+size >= 6000:
                    raise Exception("Stack Overflow on temporal string variables")
                print(f'temporal {tempResult} of type {operandType} assigned to {self.memory.mem_temp_string}')
                self.temporalDimensionVariableStack.append(TemporalDimensionVariable
                                                     (self.memory.mem_temp_string, newFirstIndex, newSecondIndex, operandType, size))
                self.memory.mem_temp_string += size
            elif operandType == "bool":
                if self.memory.mem_temp_bool + size >= 8000:
                    raise Exception("Stack Overflow on temporal bool variables")
                print(f'temporal {tempResult} of type {operandType} assigned to {self.memory.mem_temp_bool}')
                self.temporalDimensionVariableStack.append(TemporalDimensionVariable
                                                     (self.memory.mem_temp_bool, newFirstIndex, newSecondIndex, operandType, size))
                self.memory.mem_temp_bool += size
            elif operandType == "char":
                if self.memory.mem_temp_char + size >= 10000:
                    raise Exception("Stack Overflow on temporal char variables")
                print(f'temporal {tempResult} of type {operandType} assigned to {self.memory.mem_temp_char}')
                self.temporalDimensionVariableStack.append(TemporalDimensionVariable
                                                     (self.memory.mem_temp_char, newFirstIndex, newSecondIndex, operandType, size))
                self.memory.mem_temp_char += size

            # Add result to the Operand Stack
            self.addOperand(tempResult)

            # Add matrix type to type stack
            self.addType(operandType)

            quad = Quadruple(operator, address, None, self.temporalDimensionVariableStack[-1].address)
            print(operator, operand, address, tempResult, self.temporalDimensionVariableStack[-1].address)
            self.quadruples.append(quad)
        else:
            raise TypeError(f'{operator} operand can only be applied to a matrix')



    def clear_local_memory(self):
        self.memory.mem_local_int = 20000
        self.memory.mem_local_float = 22000
        self.memory.mem_local_string = 24000
        self.memory.mem_local_bool = 26000
        self.memory.mem_local_char = 28000
        self.memory.mem_temp_int = 0
        self.memory.mem_temp_float = 2000
        self.memory.mem_temp_string = 4000
        self.memory.mem_temp_bool = 6000
        self.memory.mem_temp_char = 8000
        self.memory.mem_pointers = 40000

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
                if parameter.vartype != passedParameterType:
                    raise TypeError(f'Parameter {passedParameter} of type {passedParameterType} '
                                    f'cannot be matched with {parameter.vartype}')
                else:
                    parameterAddress = None
                    if passedParameter in self.currentFunction.varsTable:
                        if self.currentFunction.varsTable[passedParameter].isArray or self.currentFunction.varsTable[passedParameter].isMatrix:
                            raise Exception(f'Error: we did not have time to implement arrays and matrix as params')
                        parameterAddress = self.currentFunction.varsTable[passedParameter].address
                    elif passedParameter in self.functionTable["global"].varsTable:
                        if self.functionTable["global"].varsTable[passedParameter].isArray or self.functionTable["global"].varsTable[passedParameter].isMatrix:
                            raise Exception(f'Error: we did not have time to implement arrays and matrix as params')
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
                self.check_for_array_or_matrix()

    def topIsAddOrSub(self):
        if len(self.operatorStack) != 0:
            if self.operatorStack[-1] == "+" or self.operatorStack[-1] == "-":
                self.check_for_array_or_matrix()

    def topIsComparison(self):
        if len(self.operatorStack) != 0:
            if self.operatorStack[-1] == "==" or self.operatorStack[-1] == "!=" or self.operatorStack[-1] == ">=" or \
                    self.operatorStack[-1] == "<=" or self.operatorStack[-1] == ">" or self.operatorStack[-1] == "<":
                self.check_for_array_or_matrix()

    def topIsLogicOperator(self):
        if len(self.operatorStack) != 0:
            if self.operatorStack[-1] == "&&" or self.operatorStack[-1] == "||":
                self.check_for_array_or_matrix()

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
        print(f'+ (from index) {self.loopVariableStack[-1]} amount 1 {tempResult} {self.temporalStack[-1]}')

        if '1' not in self.constantTable:
            if self.memory.mem_constant < 40000:
                self.constantTable['1'] = Constant('int', self.memory.mem_constant, '1')
                self.realConstantTable[self.memory.mem_constant] = Constant('int', self.memory.mem_constant, '1')
                self.memory.mem_constant += 1
            else:
                raise Exception(f'StackOverflow on constants')

        quad1 = Quadruple("+", self.loopVariableStack[-1],  self.constantTable['1'].address, self.loopVariableStack[-1])
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

                if self.memory.mem_temp_bool == 8000:
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
        elif operand != "True" and operand != "False":
            operandAddress = self.temporalStack[-1]
            self.loopVariableStack.append(operandAddress)
            #self.operandStack.append(operand)
            #self.addType("bool")
            print(f'WHILEVAROPERAND OPERANDADDRESS {operandAddress}')
        else:
            if operand == "True" or operand == "False":
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

    def generateReadQuad(self):
        operand = self.operandStack.pop()
        operandType = self.typesStack.pop()

        if operandType == 'bool':
            raise Exception('Cannot input a bool value')

        if operand in self.currentFunction.varsTable:
            if self.currentFunction.varsTable[operand].isMatrix or self.currentFunction.varsTable[operand].isArray:
                raise Exception('You cannot input a whole matrix/array')
            print("read", operand, self.currentFunction.varsTable[operand].address, operandType, "-")
            quad = Quadruple("read", self.currentFunction.varsTable[operand].address, operandType, "_")
            self.quadruples.append(quad)
        elif operand in self.functionTable["global"].varsTable:
            if self.functionTable["global"].varsTable[operand].isMatrix or self.functionTable["global"].varsTable[operand].isArray:
                raise Exception('You cannot input a whole matrix/array')
            print("read", operand, self.functionTable["global"].varsTable[operand].address, operandType, "-")
            quad = Quadruple("read", self.functionTable["global"].varsTable[operand].address, operandType, "_")
            self.quadruples.append(quad)
        elif int(self.temporalStack[-1] >= 40000):
            print("read", operand, self.temporalStack[-1], operandType, "-")
            quad = Quadruple("read", self.temporalStack[-1], operandType, "_")
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
                raise TypeError(f'{self.scube.cube[leftOperandType][operator][rightOperandType]}')

            # Applying semantics to matrixes and arrays
            # this includes transpose, determinant and inverse operations
            leftOperandVariable = None
            rightOperandVariable = None
            if leftOperand in self.currentFunction.varsTable:
                leftOperandVariable = self.currentFunction.varsTable[leftOperand]
            elif leftOperand in self.functionTable["global"].varsTable:
                leftOperandVariable = self.functionTable["global"].varsTable[leftOperand]
            if rightOperand in self.currentFunction.varsTable:
                rightOperandVariable = self.currentFunction.varsTable[rightOperand]
            elif rightOperand in self.functionTable["global"].varsTable:
                rightOperandVariable = self.functionTable["global"].varsTable[rightOperand]

            # two variables in play... they must match if we are dealing with matrix/arrays
            if leftOperandVariable is not None and rightOperandVariable is not None:
                if leftOperandVariable.isMatrix:
                    if rightOperandVariable.isMatrix is False:
                        raise TypeError(f'Cannot assign {rightOperand} to a matrix')
                    elif leftOperandVariable.first_index != rightOperandVariable.first_index or leftOperandVariable.second_index != rightOperandVariable.second_index:
                        raise Exception(f'Cannot assign lists of different dimensions')
                elif leftOperandVariable.isArray:
                    if rightOperandVariable.isArray is False:
                        raise TypeError(f'Cannot assign {rightOperand} to an array')
                    elif leftOperandVariable.size != rightOperandVariable.size:
                        raise Exception(f'Cannot assign lists of different dimensions')
                elif rightOperandVariable.isMatrix or rightOperandVariable.isArray:
                    raise TypeError(f'Cannot assign {rightOperand} to a non-dimensional variable')

            # temporal/constant assignation to a variable. The temporal may be a transpose/determinant/inverse operation
            elif leftOperandVariable is not None and rightOperandVariable is None:
                if rightOperand[0] == 'M':
                    if leftOperandVariable.isMatrix is False:
                        raise TypeError(f'A matrix cannot be assigned to {leftOperand}')
                    rightOperandMatrix = self.temporalDimensionVariableStack[int(rightOperand[1:])]
                    if leftOperandVariable.first_index != rightOperandMatrix.first_index or leftOperandVariable.second_index != rightOperandMatrix.second_index:
                        raise Exception(f'The indexes in matrix {leftOperand} do not match the ones in a temporal generated matrix')
                elif rightOperand[0] == 'A':
                    if leftOperandVariable.isArray is False:
                        raise TypeError(f'An array cannot be assigned to {leftOperand}')
                    rightOperandArray = self.temporalDimensionVariableStack[int(rightOperand[1:])]
                    if leftOperandVariable.size != rightOperandArray.size:
                        raise Exception(f'The size in array {leftOperand} does not match the one in a temporal generated array')
                elif leftOperandVariable.isMatrix or leftOperandVariable.isArray:
                    raise TypeError(f'Cannot assign non-matrix value to {leftOperand}')

            # trying to assign a value to a constant/temporal that is not the index of a list
            elif leftOperandVariable is None and int(self.temporalStack[-1]) < 40000:
                raise Exception(f'This operation is impossible')

            roAddress = None
            if rightOperand in self.currentFunction.varsTable:
                roAddress = self.currentFunction.varsTable[rightOperand].address
            elif rightOperand in self.functionTable["global"].varsTable:
                roAddress = self.functionTable["global"].varsTable[rightOperand].address
            elif rightOperand in self.constantTable:
                roAddress = self.constantTable[rightOperand].address
            elif rightOperand[0] == 'M' or rightOperand[0] == 'A':
                roAddress = self.temporalDimensionVariableStack[-1].address
            else:
                roAddress = self.temporalStack[-1]

            loAddress = None
            if leftOperand in self.currentFunction.varsTable:
                loAddress = self.currentFunction.varsTable[leftOperand].address
            elif leftOperand in self.functionTable["global"].varsTable:
                loAddress = self.functionTable["global"].varsTable[leftOperand].address
            elif leftOperand in self.constantTable:
                raise Exception(f'This operation is impossible')
            elif int(self.temporalStack[-1]) >= 40000:
                loAddress = self.temporalStack[-1]
            else:
                raise Exception(f'This operation is impossible')

            quad = Quadruple(operator, loAddress, roAddress, "_")
            self.quadruples.append(quad)

            self.operandStack.append(leftOperand)
            self.typesStack.append(leftOperandType)
            print(operator, leftOperand, loAddress, rightOperand, roAddress)

        self.operandStack.pop()
        self.typesStack.pop()

    def generate_simple_operation_quad(self, rightOperand, leftOperand, operator, rightOperandType, leftOperandType):
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
            if self.memory.mem_temp_string == 6000:
                raise Exception("Stack Overflow on temporal string variables")
            self.temporalStack.append(self.memory.mem_temp_string)
            print(f'temporal {tempResult} of type {temptype} assigned to {self.memory.mem_temp_string}')
            self.memory.mem_temp_string += 1
        elif temptype == "bool":
            if self.memory.mem_temp_bool == 8000:
                raise Exception("Stack Overflow on temporal bool variables")
            self.temporalStack.append(self.memory.mem_temp_bool)
            print(f'temporal {tempResult} of type {temptype} assigned to {self.memory.mem_temp_bool}')
            self.memory.mem_temp_bool += 1
        elif temptype == "char":
            if self.memory.mem_temp_char == 10000:
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

    def generate_temporal_array_quad(self, leftArray, rightArray, operator):
        tempResult = 'A' + str(len(self.temporalDimensionVariableStack))
        if leftArray.vartype == "int":
            if self.memory.mem_temp_int + leftArray.size >= 2000:
                raise Exception("Stack Overflow on temporal integer variables")
            print(f'temporal {tempResult} of type {leftArray.vartype} assigned to {self.memory.mem_temp_int}')
            self.temporalDimensionVariableStack.append(TemporalDimensionVariable(self.memory.mem_temp_int, -1, -1, leftArray.vartype, leftArray.size))
            self.memory.mem_temp_int += leftArray.size
        elif leftArray.vartype == "float":
            if self.memory.mem_temp_float + leftArray.size >= 4000:
                raise Exception("Stack Overflow on temporal float variables")
            print(f'temporal {tempResult} of type {leftArray.vartype} assigned to {self.memory.mem_temp_float}')
            self.temporalDimensionVariableStack.append(TemporalDimensionVariable(self.memory.mem_temp_float, -1, -1, leftArray.vartype, leftArray.size))
            self.memory.mem_temp_float += leftArray.size
        elif leftArray.vartype == "string":
            if self.memory.mem_temp_string + leftArray.size >= 6000:
                raise Exception("Stack Overflow on temporal string variables")
            print(f'temporal {tempResult} of type {leftArray.vartype} assigned to {self.memory.mem_temp_string}')
            self.temporalDimensionVariableStack.append(TemporalDimensionVariable(self.memory.mem_temp_string, -1, -1, leftArray.vartype, leftArray.size))
            self.memory.mem_temp_string += leftArray.size
        elif leftArray.vartype == "bool":
            if self.memory.mem_temp_bool + leftArray.size >= 8000:
                raise Exception("Stack Overflow on temporal bool variables")
            print(f'temporal {tempResult} of type {leftArray.vartype} assigned to {self.memory.mem_temp_bool}')
            self.temporalDimensionVariableStack.append(TemporalDimensionVariable(self.memory.mem_temp_bool, -1, -1, leftArray.vartype, leftArray.size))
            self.memory.mem_temp_bool += leftArray.size
        elif leftArray.vartype == "char":
            if self.memory.mem_temp_char + leftArray.size >= 10000:
                raise Exception("Stack Overflow on temporal char variables")
            print(f'temporal {tempResult} of type {leftArray.vartype} assigned to {self.memory.mem_temp_char}')
            self.temporalDimensionVariableStack.append(TemporalDimensionVariable(self.memory.mem_temp_char, -1, -1, leftArray.vartype, leftArray.size))
            self.memory.mem_temp_char += leftArray.size

        # Create Quad and add it to Quadruples Stack
        quad = Quadruple(operator, leftArray.address, rightArray.address, self.temporalDimensionVariableStack[-1].address)
        print(operator, 'array in address', leftArray.address, 'array in address', rightArray.address, tempResult, self.temporalDimensionVariableStack[-1].address)
        self.quadruples.append(quad)

        # Add result to the Operand Stack
        self.addOperand(tempResult)

        # Add matrix type to type stack
        self.addType(leftArray.vartype)

    def generate_temporal_matrix_quad(self, leftMatrix, rightMatrix, operator):
        tempResult = 'M' + str(len(self.temporalDimensionVariableStack))
        if leftMatrix.vartype == "int":
            if self.memory.mem_temp_int + leftMatrix.size >= 2000:
                raise Exception("Stack Overflow on temporal integer variables")
            print(f'temporal {tempResult} of type {leftMatrix.vartype} assigned to {self.memory.mem_temp_int}')
            self.temporalDimensionVariableStack.append(TemporalDimensionVariable(self.memory.mem_temp_int, leftMatrix.first_index, leftMatrix.second_index, leftMatrix.vartype, leftMatrix.size))
            self.memory.mem_temp_int += leftMatrix.size
        elif leftMatrix.vartype == "float":
            if self.memory.mem_temp_float + leftMatrix.size >= 4000:
                raise Exception("Stack Overflow on temporal float variables")
            print(f'temporal {tempResult} of type {leftMatrix.vartype} assigned to {self.memory.mem_temp_float}')
            self.temporalDimensionVariableStack.append(TemporalDimensionVariable(self.memory.mem_temp_float, leftMatrix.first_index, leftMatrix.second_index, leftMatrix.vartype, leftMatrix.size))
            self.memory.mem_temp_float += leftMatrix.size
        elif leftMatrix.vartype == "string":
            if self.memory.mem_temp_string + leftMatrix.size >= 6000:
                raise Exception("Stack Overflow on temporal string variables")
            print(f'temporal {tempResult} of type {leftMatrix.vartype} assigned to {self.memory.mem_temp_string}')
            self.temporalDimensionVariableStack.append(TemporalDimensionVariable(self.memory.mem_temp_string, leftMatrix.first_index, leftMatrix.second_index, leftMatrix.vartype, leftMatrix.size))
            self.memory.mem_temp_string += leftMatrix.size
        elif leftMatrix.vartype == "bool":
            if self.memory.mem_temp_bool + leftMatrix.size >= 8000:
                raise Exception("Stack Overflow on temporal bool variables")
            print(f'temporal {tempResult} of type {leftMatrix.vartype} assigned to {self.memory.mem_temp_bool}')
            self.temporalDimensionVariableStack.append(TemporalDimensionVariable(self.memory.mem_temp_bool, leftMatrix.first_index, leftMatrix.second_index, leftMatrix.vartype, leftMatrix.size))
            self.memory.mem_temp_bool += leftMatrix.size
        elif leftMatrix.vartype == "char":
            if self.memory.mem_temp_char + leftMatrix.size >= 10000:
                raise Exception("Stack Overflow on temporal char variables")
            print(f'temporal {tempResult} of type {leftMatrix.vartype} assigned to {self.memory.mem_temp_char}')
            self.temporalDimensionVariableStack.append(TemporalDimensionVariable(self.memory.mem_temp_char, leftMatrix.first_index, leftMatrix.second_index, leftMatrix.vartype, leftMatrix.size))
            self.memory.mem_temp_char += leftMatrix.size

        # Create Quad and add it to Quadruples Stack
        quad = Quadruple(operator, leftMatrix.address, rightMatrix.address, self.temporalDimensionVariableStack[-1].address)
        print(operator, 'matrix in address', leftMatrix.address, 'matrix in address', rightMatrix.address, tempResult, self.temporalDimensionVariableStack[-1].address)
        self.quadruples.append(quad)

        # Add result to the Operand Stack
        self.addOperand(tempResult)

        # Add matrix type to type stack
        self.addType(leftMatrix.vartype)



    def check_for_array_or_matrix(self):
        rightOperand = self.operandStack.pop()
        leftOperand = self.operandStack.pop()
        operator = self.operatorStack.pop()
        rightOperandType = self.typesStack.pop()
        leftOperandType = self.typesStack.pop()

        # Check with semantic cube to see if operation is possible
        if self.scube.cube[leftOperandType][operator][rightOperandType].startswith("Error"):
            raise TypeError(f'{self.scube.cube[leftOperandType][operator][rightOperandType]}')

        # Applying semantics to matrixes and arrays
        # this includes transpose, determinant and inverse operations
        leftOperandVariable = None
        rightOperandVariable = None
        if leftOperand in self.currentFunction.varsTable:
            leftOperandVariable = self.currentFunction.varsTable[leftOperand]
        elif leftOperand in self.functionTable["global"].varsTable:
            leftOperandVariable = self.functionTable["global"].varsTable[leftOperand]
        if rightOperand in self.currentFunction.varsTable:
            rightOperandVariable = self.currentFunction.varsTable[rightOperand]
        elif rightOperand in self.functionTable["global"].varsTable:
            rightOperandVariable = self.functionTable["global"].varsTable[rightOperand]

        # two variables in play... they must match if we are dealing with matrix/arrays
        if leftOperandVariable is not None and rightOperandVariable is not None:
            if leftOperandVariable.isMatrix:
                if rightOperandVariable.isMatrix is False:
                    raise TypeError(f'{rightOperand} cannot perform operations with a matrix')
                elif leftOperandVariable.first_index != rightOperandVariable.first_index or leftOperandVariable.second_index != rightOperandVariable.second_index:
                    raise Exception(f'{rightOperand} cannot perform operations with a matrix of different dimensions')
                else:
                    self.generate_temporal_matrix_quad(leftOperandVariable, rightOperandVariable, operator)
            elif leftOperandVariable.isArray:
                if rightOperandVariable.isArray is False:
                    raise TypeError(f'{rightOperand} cannot perform operations with an array')
                elif leftOperandVariable.size != rightOperandVariable.size:
                    raise Exception(f'{rightOperand} cannot perform operations with an array of different dimensions')
                else:
                    self.generate_temporal_array_quad(leftOperandVariable, rightOperandVariable, operator)
            elif rightOperandVariable.isMatrix or rightOperandVariable.isArray:
                raise TypeError(f'{rightOperand} cannot perform operations with a non-dimensional variable')
            else:
                self.generate_simple_operation_quad(rightOperand, leftOperand, operator, rightOperandType, leftOperandType)

        # temporal/constant instead of a variable in rightOperand. The temporal may be a matrix operation
        elif leftOperandVariable is not None and rightOperandVariable is None:
            if rightOperand[0] == 'M':
                if leftOperandVariable.isMatrix is False:
                    raise TypeError(f'Operations cannot be performed between a matrix and {leftOperand}')
                rightOperandMatrix = self.temporalDimensionVariableStack[int(rightOperand[1:])]
                if leftOperandVariable.first_index != rightOperandMatrix.first_index or leftOperandVariable.second_index != rightOperandMatrix.second_index:
                    raise Exception(f'The indexes in matrix {leftOperand} do not match the ones in a temporal generated matrix')
                self.generate_temporal_matrix_quad(leftOperandVariable, rightOperandMatrix, operator)
            elif rightOperand[0] == 'A':
                if leftOperandVariable.isArray is False:
                    raise TypeError(f'Operations cannot be performed between an array and {leftOperand}')
                rightOperandArray = self.temporalDimensionVariableStack[int(rightOperand[1:])]
                if leftOperandVariable.size != rightOperandArray.size:
                    raise Exception(f'The size in array {leftOperand} does not match the size in a temporal generated array')
                self.generate_temporal_array_quad(leftOperandVariable, rightOperandArray, operator)
            elif leftOperandVariable.isMatrix or leftOperandVariable.isArray:
                raise TypeError(f'Cannot perform operations of non-matrix value with {leftOperand}')
            else:
                self.generate_simple_operation_quad(rightOperand, leftOperand, operator, rightOperandType, leftOperandType)

        # temporal/constant instead of a variable in leftOperand. The temporal may be a matrix operation
        elif leftOperandVariable is None and rightOperandVariable is not None:
            if leftOperand[0] == 'M':
                if rightOperandVariable.isMatrix is False:
                    raise TypeError(f'Operations cannot be performed between a matrix and {rightOperand}')
                leftOperandMatrix = self.temporalDimensionVariableStack[int(leftOperand[1:])]
                if rightOperandVariable.first_index != leftOperandMatrix.first_index or rightOperandVariable.second_index != leftOperandMatrix.second_index:
                    raise Exception(f'The indexes in matrix {rightOperand} do not match the ones in a temporal generated matrix')
                self.generate_temporal_matrix_quad(leftOperandMatrix, rightOperandVariable, operator)
            elif leftOperand[0] == 'A':
                if rightOperandVariable.isArray is False:
                    raise TypeError(f'Operations cannot be performed between an array and {rightOperand}')
                leftOperandArray = self.temporalDimensionVariableStack[int(leftOperand[1:])]
                if leftOperandArray.size != rightOperandVariable.size:
                    raise Exception(f'The size in array {rightOperand} does not match the size in a temporal generated array')
                self.generate_temporal_array_quad(leftOperandArray, rightOperandVariable)
            elif rightOperandVariable.isMatrix or rightOperandVariable.isArray:
                raise TypeError(f'Cannot perform operations of non-matrix value with {rightOperand}')
            else:
                self.generate_simple_operation_quad(rightOperand, leftOperand, operator, rightOperandType, leftOperandType)
        elif leftOperand[0] == 'M' and rightOperand[0] == 'M':
            leftOperandMatrix = self.temporalDimensionVariableStack[int(leftOperand[1:])]
            rightOperandMatrix = self.temporalDimensionVariableStack[int(rightOperand[1:])]
            if leftOperandMatrix.first_index != rightOperandMatrix.first_index or leftOperandMatrix.second_index != rightOperandMatrix.second_index:
                raise Exception(f'Cannot perform {operator} between two different indexed matrixes')
            self.generate_temporal_matrix_quad(leftOperandMatrix, rightOperandMatrix, operator)
        elif leftOperand[0] == 'A' and rightOperand[0] == 'A':
            leftOperandArray = self.temporalDimensionVariableStack[int(leftOperand[1:])]
            rightOperandArray = self.temporalDimensionVariableStack[int(rightOperand[1:])]
            if leftOperandArray.size != rightOperandArray.size:
                raise Exception(f'Cannot perform {operator} between two different sized arrays')
            self.generate_temporal_array_quad(leftOperandArray, rightOperandArray, operator)
        elif leftOperand[0] == 'M' or rightOperand[0] == 'A' or leftOperand[0] == 'A' or rightOperand[0] == 'M':
            raise Exception(f'There was an error trying to perform operations between variables of different dimensions')
        else:
            self.generate_simple_operation_quad(rightOperand, leftOperand, operator, rightOperandType, leftOperandType)


