import numpy as np


class VirtualMachine:
    def __init__(self, quadruples, constantTable, functionTable):
        self.quadPointer = 0
        self.quadruples = quadruples
        self.functionTable = functionTable
        self.functionStack = []
        self.localMemoryStack = []
        self.temporalMemoryStack = []
        self.pointerMemoryStack = []
        self.parameterStack = []

        self.GLOBAL = [None] * 10000
        self.LOCAL = [None] * 10000
        self.TEMPORAL = [None] * 10000
        self.CONSTANT = constantTable
        self.POINTER = [None] * 10000
        self.operators = {
            "+": self.add,
            "-": self.subtract,
            "/": self.divide,
            "*": self.multiply,
            "=": self.assign,
            ">": self.greater_than,
            "<": self.less_than,
            "==": self.equal,
            ">=": self.greater_than_or_equal,
            "<=": self.less_than_or_equal,
            "!=": self.not_equal,
            "&&": self.and_op,
            "||": self.or_op,
            "PRINT": self.print,
            "READ": self.read,
            "GOTOF": self.gotof,
            "GOTO": self.goto,
            "ERA": self.era,
            "RETURN": self.ret,
            "GOSUB": self.gosub,
            "ENDFUNC": self.endfunc,
            "PARAM": self.param,
            "VERIF": self.verif,
            "?": self.inverse,
            "#": self.transpose,
            "$": self.determinant,
            "+L": self.add_lists,
            "-L": self.subtract_lists,
            "/L": self.divide_lists,
            "*L": self.multiply_lists,
            "=L": self.assign_lists,
            "==L": self.equal_lists,
            "!=L": self.not_equal_lists,
            "PRINTARRAY": self.print_array,
            "PRINTMATRIX": self.print_matrix,
        }

    def begin(self):
        # This function begins running and executing all quadruples in the program
        counter = 0
        for quad in self.quadruples:
            print(f'{counter} - {quad.operator}.{quad.leftOp}.{quad.rightOp}.{quad.resultTemp}')
            counter+=1
        while self.quadPointer < len(self.quadruples):
            currentQuad = self.current_quad()
            operator = currentQuad.operator
            self.operators.get(operator)()

    def increase_current_quad_pointer(self):
        self.quadPointer += 1

    def current_quad(self):
        return self.quadruples[self.quadPointer]

    def check_memory(self, operandAddress):
        #This function checks where the operandAddress lies, and calls
        #check_type_and_return_true_value in order to return its true value to
        #the caller

        if operandAddress < 10000:
            value = self.TEMPORAL[operandAddress]
            if value is None:
                raise Exception(f'Using an operand that has not been assigned a value yet')
            trueValue = self.check_type_and_return_true_value(value, operandAddress, "temporal")
            return trueValue
        elif operandAddress < 20000:
            operandAddress -= 10000
            value = self.GLOBAL[operandAddress]
            if value is None:
                raise Exception(f'Using an operand that has not been assigned a value yet')
            trueValue = self.check_type_and_return_true_value(value, operandAddress, "global")
            return trueValue
        elif operandAddress < 30000:
            operandAddress -= 20000
            value = self.LOCAL[operandAddress]
            if value is None:
                raise Exception(f'Using an operand that has not been assigned a value yet')
            trueValue = self.check_type_and_return_true_value(value, operandAddress, "local")
            return trueValue
        elif operandAddress < 40000:
            value = self.CONSTANT[operandAddress].operand
            if value is None:
                raise Exception(f'Using an operand that has not been assigned a value yet')
            trueValue = self.check_type_and_return_true_value(value, operandAddress, "constant")
            return trueValue
        elif operandAddress < 50000:
            operandAddress -= 40000
            addressValue = int(self.POINTER[operandAddress])
            if addressValue is None:
                raise Exception(f'Using an operand that has not been assigned a value yet')
            return self.check_memory(addressValue)
        else:
            raise Exception("Danger zone, something is wrong")

    def check_type_and_return_true_value(self, value, address, memory):
        #This function gets the value of an operand (string), and turns it into
        #its true value, based on its address

        if memory == 'constant':
            if self.CONSTANT[address].type == "int":
                return int(value)
            elif self.CONSTANT[address].type == "float":
                return float(value)
            elif self.CONSTANT[address].type == "string":
                return str(value)
            elif self.CONSTANT[address].type == "bool":
                if value:
                    return True
                else:
                    return False
            elif self.CONSTANT[address].type == "char":
                return str(value)
            else:
                raise Exception("Danger zone: you should not be here!")
        else:
            if address < 2000:
                return int(value)
            elif address < 4000:
                return float(value)
            elif address < 6000:
                return str(value)
            elif address < 8000:
                if value:
                    return True
                else:
                    return False
            elif address < 10000:
                return str(value)

    def set_value(self, value, valueAddress):
        # This function receives a value and an address to store it in

        if valueAddress < 10000:
            self.TEMPORAL[valueAddress] = value
            print(f'setting value {value} to temporal address({valueAddress})')

        elif valueAddress < 20000:
            print(f'setting value {value} to global address({valueAddress})')
            valueAddress -= 10000
            self.GLOBAL[valueAddress] = value

        elif valueAddress < 30000:
            print(f'setting value {value} to local address({valueAddress})')
            valueAddress -= 20000
            self.LOCAL[valueAddress] = value

        elif valueAddress < 40000:
            raise Exception("You should not be assigning stuff to constant address")

        elif valueAddress < 50000:
            valueAddress -= 40000
            if self.current_quad().operator != '=':
                print(f'setting {value} to pointer {valueAddress + 40000}')
                self.POINTER[valueAddress] = value
            else:
                print(f'extracting address value from pointer {valueAddress + 40000}')
                newValueAddress = self.POINTER[valueAddress]
                self.set_value(value, newValueAddress)
        else:
            raise Exception("You should not be here man!")

    def assign(self):
        # Get the current quad, and its addresses
        currentQuad = self.current_quad()
        leftOperandAddress = currentQuad.leftOp
        rightOperandAddress = currentQuad.rightOp

        # Get what type of memory rightOperandAddress is stored in, and get its true value
        rightValue = self.check_memory(rightOperandAddress)

        # removes "" and '' from chars and strings
        if type(rightValue) is str and (rightValue.startswith("\"") or rightValue.startswith("\'")):
            rightValue = rightValue[1:-1]

        self.set_value(rightValue, leftOperandAddress)

        self.increase_current_quad_pointer()

    def add(self):
        # Get the current quad, and its addresses
        currentQuad = self.current_quad()
        leftOperandAddress = currentQuad.leftOp
        rightOperandAddress = currentQuad.rightOp
        resultAddress = currentQuad.resultTemp
        # Get what type of memory leftOperandAddress is stored in, and get its true value
        leftValue = self.check_memory(leftOperandAddress)
        # Get what type of memory rightOperandAddress is stored in, and get its true value
        rightValue = self.check_memory(rightOperandAddress)

        # removes "" and '' from chars and strings
        if type(leftValue) is str and leftValue.startswith("\""):
            leftValue = leftValue[1:-1]
        # removes "" and '' from chars and strings
        if type(rightValue) is str and rightValue.startswith("\""):
            rightValue = rightValue[1:-1]

        # Get the real result of adding both operands together
        result = leftValue + rightValue

        print(f'{leftValue} + {rightValue} = {result}')

        # Check where to store the result and store it
        self.set_value(result, resultAddress)

        self.increase_current_quad_pointer()

    def subtract(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        leftOperandAddress = currentQuad.leftOp
        rightOperandAddress = currentQuad.rightOp
        resultAddress = currentQuad.resultTemp

        # Get what type of memory leftOperandAddress is stored in, and get its true value
        leftValue = self.check_memory(leftOperandAddress)
        # Get what type of memory rightOperandAddress is stored in, and get its true value
        rightValue = self.check_memory(rightOperandAddress)

        # Get the result of adding both operands together
        result = leftValue - rightValue

        print(f'{leftValue} - {rightValue} = {result}')

        # Check where to store the result and store it
        self.set_value(result, resultAddress)

        self.increase_current_quad_pointer()

    def multiply(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        leftOperandAddress = currentQuad.leftOp
        rightOperandAddress = currentQuad.rightOp
        resultAddress = currentQuad.resultTemp

        # Get what type of memory leftOperandAddress is stored in, and get its true value
        leftValue = self.check_memory(leftOperandAddress)

        # Get what type of memory rightOperandAddress is stored in, and get its true value
        rightValue = self.check_memory(rightOperandAddress)

        # Get the result of adding both operands together
        result = leftValue * rightValue

        print(f'{leftValue} * {rightValue} = {result}')

        # Check where to store the result and store it
        self.set_value(result, resultAddress)

        self.increase_current_quad_pointer()

    def divide(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        leftOperandAddress = currentQuad.leftOp
        rightOperandAddress = currentQuad.rightOp
        resultAddress = currentQuad.resultTemp

        # Get what type of memory leftOperandAddress is stored in, and get its true value
        leftValue = self.check_memory(leftOperandAddress)

        # Get what type of memory rightOperandAddress is stored in, and get its true value
        rightValue = self.check_memory(rightOperandAddress)

        # Get the result of adding both operands together
        result = leftValue / rightValue

        print(f'{leftValue} / {rightValue} = {result}')

        # Check where to store the result and store it
        self.set_value(result, resultAddress)

        self.increase_current_quad_pointer()

    def print(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        operandAddress = currentQuad.leftOp

        operandValue = self.check_memory(operandAddress)

        if type(operandValue) is str and (operandValue.startswith("\"") or operandValue.startswith("\'")):
            operandValue = operandValue[1:-1]

        print(f'printing:{operandValue}:')

        self.increase_current_quad_pointer()

    def read(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        operandAddress = currentQuad.leftOp
        typeOfOperand = currentQuad.rightOp

        inputValue = input()
        if typeOfOperand == 'int':
            inputValue = int(inputValue)
        if typeOfOperand == 'string':
            inputValue = str(inputValue)
        if typeOfOperand == 'char':
            if len(inputValue) > 1:
                raise Exception('Cannot input string to char')
            inputValue = str(inputValue)
        if typeOfOperand == 'float':
            inputValue = float(inputValue)

        self.set_value(inputValue, operandAddress)

        print(f'Input {inputValue} to {operandAddress}')
        self.increase_current_quad_pointer()

    def greater_than(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        leftOperandAddress = currentQuad.leftOp
        rightOperandAddress = currentQuad.rightOp
        resultAddress = currentQuad.resultTemp

        # Get what type of memory leftOperandAddress is stored in, and get its true value
        leftValue = self.check_memory(leftOperandAddress)

        # Get what type of memory rightOperandAddress is stored in, and get its true value
        rightValue = self.check_memory(rightOperandAddress)

        if leftValue > rightValue:
            self.set_value(True, resultAddress)
        else:
            self.set_value(False, resultAddress)

        self.increase_current_quad_pointer()

    def less_than(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        leftOperandAddress = currentQuad.leftOp
        rightOperandAddress = currentQuad.rightOp
        resultAddress = currentQuad.resultTemp

        # Get what type of memory leftOperandAddress is stored in, and get its true value
        leftValue = self.check_memory(leftOperandAddress)

        # Get what type of memory rightOperandAddress is stored in, and get its true value
        rightValue = self.check_memory(rightOperandAddress)

        if leftValue < rightValue:
            self.set_value(True, resultAddress)
        else:
            self.set_value(False, resultAddress)

        self.increase_current_quad_pointer()

    def equal(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        leftOperandAddress = currentQuad.leftOp
        rightOperandAddress = currentQuad.rightOp
        resultAddress = currentQuad.resultTemp

        # Get what type of memory leftOperandAddress is stored in, and get its true value
        leftValue = self.check_memory(leftOperandAddress)

        # Get what type of memory rightOperandAddress is stored in, and get its true value
        rightValue = self.check_memory(rightOperandAddress)

        if leftValue == rightValue:
            self.set_value(True, resultAddress)
        else:
            self.set_value(False, resultAddress)

        self.increase_current_quad_pointer()

    def greater_than_or_equal(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        leftOperandAddress = currentQuad.leftOp
        rightOperandAddress = currentQuad.rightOp
        resultAddress = currentQuad.resultTemp

        # Get what type of memory leftOperandAddress is stored in, and get its true value
        leftValue = self.check_memory(leftOperandAddress)

        # Get what type of memory rightOperandAddress is stored in, and get its true value
        rightValue = self.check_memory(rightOperandAddress)

        if leftValue >= rightValue:
            self.set_value(True, resultAddress)
        else:
            self.set_value(False, resultAddress)

        self.increase_current_quad_pointer()

    def less_than_or_equal(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        leftOperandAddress = currentQuad.leftOp
        rightOperandAddress = currentQuad.rightOp
        resultAddress = currentQuad.resultTemp

        # Get what type of memory leftOperandAddress is stored in, and get its true value
        leftValue = self.check_memory(leftOperandAddress)

        # Get what type of memory rightOperandAddress is stored in, and get its true value
        rightValue = self.check_memory(rightOperandAddress)

        if leftValue <= rightValue:
            self.set_value(True, resultAddress)
        else:
            self.set_value(False, resultAddress)

        self.increase_current_quad_pointer()

    def not_equal(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        leftOperandAddress = currentQuad.leftOp
        rightOperandAddress = currentQuad.rightOp
        resultAddress = currentQuad.resultTemp

        # Get what type of memory leftOperandAddress is stored in, and get its true value
        leftValue = self.check_memory(leftOperandAddress)

        # Get what type of memory rightOperandAddress is stored in, and get its true value
        rightValue = self.check_memory(rightOperandAddress)

        if leftValue != rightValue:
            self.set_value(True, resultAddress)
        else:
            self.set_value(False, resultAddress)

        self.increase_current_quad_pointer()

    def and_op(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        leftOperandAddress = currentQuad.leftOp
        rightOperandAddress = currentQuad.rightOp
        resultAddress = currentQuad.resultTemp

        # Get what type of memory leftOperandAddress is stored in, and get its true value
        leftValue = self.check_memory(leftOperandAddress)

        # Get what type of memory rightOperandAddress is stored in, and get its true value
        rightValue = self.check_memory(rightOperandAddress)

        if leftValue and rightValue:
            self.set_value(True, resultAddress)
        else:
            self.set_value(False, resultAddress)

        self.increase_current_quad_pointer()

    def or_op(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        leftOperandAddress = currentQuad.leftOp
        rightOperandAddress = currentQuad.rightOp
        resultAddress = currentQuad.resultTemp

        # Get what type of memory leftOperandAddress is stored in, and get its true value
        leftValue = self.check_memory(leftOperandAddress)

        # Get what type of memory rightOperandAddress is stored in, and get its true value
        rightValue = self.check_memory(rightOperandAddress)

        if leftValue or rightValue:
            self.set_value(True, resultAddress)
        else:
            self.set_value(False, resultAddress)

        self.increase_current_quad_pointer()

    def gotof(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        conditional_address = currentQuad.leftOp
        quadrupleToJump = currentQuad.resultTemp

        # Get what type of memory leftOperandAddress is stored in, and get its true value
        conditional_value = self.check_memory(conditional_address)

        if not conditional_value:
            self.quadPointer = quadrupleToJump
        else:
            self.increase_current_quad_pointer()

    def goto(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        quadrupleToJump = currentQuad.resultTemp

        self.quadPointer = quadrupleToJump

    def era(self):
        self.increase_current_quad_pointer()

    def param(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        passedParamAddress = currentQuad.leftOp
        parameterAddress = currentQuad.resultTemp

        # gets the param value from previous memory, as we have migrated for now
        passed_param_value = self.check_memory(passedParamAddress)

        # appends it so gosub can empty it
        self.parameterStack.append({'value': passed_param_value, 'address': parameterAddress})

        self.increase_current_quad_pointer()

    def gosub(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        futureTemporalToAssignReturn = currentQuad.leftOp
        quadToJump = currentQuad.resultTemp

        # Changing context
        # this was previously on the troublesome and useless ERA
        l = [None] * 10000
        t = [None] * 10000
        p = [None] * 10000

        self.localMemoryStack.append(self.LOCAL)
        self.pointerMemoryStack.append(self.POINTER)
        self.temporalMemoryStack.append(self.TEMPORAL)

        self.LOCAL = l
        self.TEMPORAL = t
        self.POINTER = p

        for parameter in self.parameterStack:
            self.set_value(parameter['value'], parameter['address'])

        self.parameterStack.clear()

        print(f'Function called, going to quad {quadToJump}')
        self.functionStack.append({'quadruple': self.quadPointer+1, 'address': futureTemporalToAssignReturn})
        self.quadPointer = quadToJump

    def ret(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        returnValueAddress = currentQuad.resultTemp

        # Get the return real value while we are still in the returning function's context
        returnValue = self.check_memory(returnValueAddress)

        # Change context
        previousLocalMemory = self.localMemoryStack.pop()
        previousTemporalMemory = self.temporalMemoryStack.pop()
        previousPointerMemory = self.pointerMemoryStack.pop()
        previousFunction = self.functionStack.pop()
        self.LOCAL = previousLocalMemory
        self.TEMPORAL = previousTemporalMemory
        self.POINTER = previousPointerMemory

        goBackQuadruple = previousFunction['quadruple']

        # Set the return value
        print(f'Returning {returnValue} and going back to quadruple {goBackQuadruple}')
        self.set_value(returnValue, previousFunction['address'])

        # Go back
        self.quadPointer = goBackQuadruple

    def endfunc(self):
        # Change context
        previousLocalMemory = self.localMemoryStack.pop()
        previousTemporalMemory = self.temporalMemoryStack.pop()
        previousPointerMemory = self.pointerMemoryStack.pop()
        previousFunction = self.functionStack.pop()
        self.LOCAL = previousLocalMemory
        self.TEMPORAL = previousTemporalMemory
        self.POINTER = previousPointerMemory

        # IF the previous function is expecting a return address and we reached ENDFUNC, we have a runtime error
        if previousFunction['address'] is not None:
            raise Exception('Error! Reached end of function without a return')

        goBackQuadruple = previousFunction['quadruple']
        # Go back
        print(f'Going back to quadruple {goBackQuadruple}')
        self.quadPointer = goBackQuadruple

    def verif(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        indexAddress = currentQuad.leftOp
        lowerLimitAddress = currentQuad.rightOp
        upperLimitAddress = currentQuad.resultTemp

        # Get what type of memory it is stored in, and get its true value
        indexValue = self.check_memory(indexAddress)

        # Get what type of memory it is stored in, and get its true value
        lowerLimitValue = self.check_memory(lowerLimitAddress)

        # Get what type of memory it is stored in, and get its true value
        upperLimitValue = self.check_memory(upperLimitAddress)

        print(f'Verifying that {indexValue} lies between {lowerLimitValue} and {upperLimitValue}')

        if upperLimitValue >= indexValue >= lowerLimitValue:
            print("The value is between the limits!")
        else:
            raise IndexError("Index out of range")

        self.increase_current_quad_pointer()

    def inverse(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        matrixStart = currentQuad.leftOp
        indexes = currentQuad.rightOp
        temporalStart = currentQuad.resultTemp

        # Get the matrixes indexes
        firstIndex = int(indexes.split(".").pop(-2))
        secondIndex = int(indexes.split(".").pop())

        # Create an empty matrix with the normal dimensions
        currentMatrix = np.empty([firstIndex,secondIndex])

        counter = 0

        # Fill in the matrix with its values from the addresses
        for x in range(firstIndex):
            for y in range(secondIndex):
                currentMatrix[x][y] = self.check_memory(matrixStart + counter)
                counter += 1


        invertedResult = np.linalg.inv(currentMatrix)

        counter = 0

        # Set the inverted
        for x in range(firstIndex):
            for y in range(secondIndex):
                self.set_value(invertedResult[x][y], temporalStart + counter)
                counter += 1

        self.increase_current_quad_pointer()

    def transpose(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        matrixStart = currentQuad.leftOp
        indexes = currentQuad.rightOp
        temporalStart = currentQuad.resultTemp

        # Get the matrixes indexes
        firstIndex = int(indexes.split(".").pop())
        secondIndex = int(indexes.split(".").pop(-2))

        # Create an empty matrix with the normal dimensions
        currentMatrix = np.empty([firstIndex,secondIndex])

        counter = 0

        # Fill in the matrix with its values from the addresses
        for x in range(firstIndex):
            for y in range(secondIndex):
                currentMatrix[x][y] = self.check_memory(matrixStart + counter)
                counter += 1

        transposedResult = currentMatrix.transpose()

        counter = 0

        # Set the inverted
        for x in range(secondIndex):
            for y in range(firstIndex):
                self.set_value(transposedResult[x][y], temporalStart + counter)
                counter += 1

        self.increase_current_quad_pointer()

    def determinant(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        matrixStart = currentQuad.leftOp
        indexes = currentQuad.rightOp
        temporalStart = currentQuad.resultTemp

        # Get the matrixes indexes
        firstIndex = int(indexes.split(".").pop(-2))
        secondIndex = int(indexes.split(".").pop())

        # Create an empty matrix with the normal dimensions
        currentMatrix = np.empty([firstIndex,secondIndex])

        counter = 0

        # Fill in the matrix with its values from the addresses
        for x in range(firstIndex):
            for y in range(secondIndex):
                currentMatrix[x][y] = self.check_memory(matrixStart + counter)
                counter += 1

        determinant_result = np.linalg.det(currentMatrix)

        self.set_value(determinant_result, temporalStart)

        self.increase_current_quad_pointer()

    def add_lists(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        leftOperand = currentQuad.leftOp

        rightOperandAddress = currentQuad.rightOp
        resultAddress = currentQuad.resultTemp
        listsSize = int(currentQuad.lQtOp.split(".").pop())
        leftOperandAddress = int(currentQuad.leftOp.split(".").pop(-2))

        for x in range(listsSize):
            # Get what type of memory leftOperandAddress is stored in, and get its true value
            leftValue = self.check_memory(leftOperandAddress+x)
            # Get what type of memory rightOperandAddress is stored in, and get its true value
            rightValue = self.check_memory(rightOperandAddress+x)

            # removes "" and '' from chars and strings
            if type(leftValue) is str and leftValue.startswith("\""):
                leftValue = leftValue[1:-1]
            # removes "" and '' from chars and strings
            if type(rightValue) is str and rightValue.startswith("\""):
                rightValue = rightValue[1:-1]

            # Get the real result of adding both operands together
            result = leftValue + rightValue
            print(f'{leftValue} + {rightValue} = {result}')
            # Check where to store the result and store it
            self.set_value(result, resultAddress+x)

        self.increase_current_quad_pointer()

    def subtract_lists(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        leftOperand = currentQuad.leftOp

        rightOperandAddress = currentQuad.rightOp
        resultAddress = currentQuad.resultTemp
        listsSize = int(currentQuad.leftOp.split(".").pop())
        leftOperandAddress = int(currentQuad.leftOp.split(".").pop(-2))

        for x in range(listsSize):
            # Get what type of memory leftOperandAddress is stored in, and get its true value
            leftValue = self.check_memory(leftOperandAddress+x)
            # Get what type of memory rightOperandAddress is stored in, and get its true value
            rightValue = self.check_memory(rightOperandAddress+x)
            # Get the real result of subtracting both operands together
            result = leftValue - rightValue
            print(f'{leftValue} - {rightValue} = {result}')
            # Check where to store the result and store it
            self.set_value(result, resultAddress+x)

        self.increase_current_quad_pointer()

    def divide_lists(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        leftOperand = currentQuad.leftOp

        rightOperandAddress = currentQuad.rightOp
        resultAddress = currentQuad.resultTemp
        listsSize = int(currentQuad.leftOp.split(".").pop())
        leftOperandAddress = int(currentQuad.leftOp.split(".").pop(-2))

        for x in range(listsSize):
            # Get what type of memory leftOperandAddress is stored in, and get its true value
            leftValue = self.check_memory(leftOperandAddress+x)
            # Get what type of memory rightOperandAddress is stored in, and get its true value
            rightValue = self.check_memory(rightOperandAddress+x)
            # Get the real result of dividing both operands together
            result = leftValue / rightValue
            print(f'{leftValue} / {rightValue} = {result}')
            # Check where to store the result and store it
            self.set_value(result, resultAddress+x)

        self.increase_current_quad_pointer()

    def multiply_lists(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        leftOperand = currentQuad.leftOp
        rightOperand = currentQuad.rightOp
        resultAddress = currentQuad.resultTemp

        leftOperandFirstIndex = int(leftOperand.split(".").pop(-2))
        leftOperandSecondIndex = int(leftOperand.split(".").pop())
        leftOperandAddress = int(leftOperand.split(".").pop(-3))

        rightOperandFirstIndex = int(rightOperand.split(".").pop(-2))
        rightOperandSecondIndex = int(rightOperand.split(".").pop())
        rightOperandAddress = int(rightOperand.split(".").pop(-3))

        # Create two empty matrixes with the normal dimensions
        leftMatrix = np.empty([leftOperandFirstIndex, leftOperandSecondIndex])
        rightMatrix = np.empty([rightOperandFirstIndex, rightOperandSecondIndex])

        counter = 0

        # Fill in the left matrix with its values from the addresses
        for x in range(leftOperandFirstIndex):
            for y in range(leftOperandSecondIndex):
                leftMatrix[x][y] = self.check_memory(leftOperandAddress + counter)
                counter += 1

        counter = 0
        # Fill in the right matrix with its values from the addresses
        for x in range(rightOperandFirstIndex):
            for y in range(rightOperandSecondIndex):
                rightMatrix[x][y] = self.check_memory(rightOperandAddress + counter)
                counter += 1

        resultMatrix = leftMatrix.dot(rightMatrix)

        counter = 0

        # Set the result matrix
        for x in range(len(resultMatrix)):
            for y in range(len(resultMatrix[0])):
                self.set_value(resultMatrix[x][y], resultAddress + counter)
                counter += 1

        self.increase_current_quad_pointer()

    def assign_lists(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        leftOperandAddress = currentQuad.leftOp
        rightOperandAddress = currentQuad.rightOp
        listSize = currentQuad.resultTemp

        for x in range(listSize):
            # Get what type of memory rightOperandAddress is stored in, and get its true value
            rightValue = self.check_memory(rightOperandAddress+x)
            # Check where to store the result and store it
            self.set_value(rightValue, leftOperandAddress+x)

        self.increase_current_quad_pointer()

    def equal_lists(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        leftOperand = currentQuad.leftOp

        rightOperandAddress = currentQuad.rightOp
        resultAddress = currentQuad.resultTemp
        listsSize = int(currentQuad.leftOp.split(".").pop())
        leftOperandAddress = int(currentQuad.leftOp.split(".").pop(-2))

        result = True

        for x in range(listsSize):
            # Get what type of memory leftOperandAddress is stored in, and get its true value
            leftValue = self.check_memory(leftOperandAddress+x)
            # Get what type of memory rightOperandAddress is stored in, and get its true value
            rightValue = self.check_memory(rightOperandAddress+x)

            if leftValue != rightValue:
                result = False
                break

        self.set_value(result, resultAddress)
        self.increase_current_quad_pointer()

    def not_equal_lists(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        leftOperand = currentQuad.leftOp

        rightOperandAddress = currentQuad.rightOp
        resultAddress = currentQuad.resultTemp
        listsSize = int(currentQuad.leftOp.split(".").pop())
        leftOperandAddress = int(currentQuad.leftOp.split(".").pop(-2))

        result = False

        for x in range(listsSize):
            # Get what type of memory leftOperandAddress is stored in, and get its true value
            leftValue = self.check_memory(leftOperandAddress+x)
            # Get what type of memory rightOperandAddress is stored in, and get its true value
            rightValue = self.check_memory(rightOperandAddress+x)

            if leftValue != rightValue:
                result = True
                break

        self.set_value(result, resultAddress)
        self.increase_current_quad_pointer()

    def print_array(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        arrayAddress = currentQuad.leftOp
        arraySize = currentQuad.rightOp

        for x in range(arraySize):
            value = self.check_memory(arrayAddress+x)
            if type(value) is str and (value.startswith("\"") or value.startswith("\'")):
                value = value[1:-1]
            print(f'printing:{value}:')

        self.increase_current_quad_pointer()

    def print_matrix(self):
        # Get the current quad, its operands and address
        currentQuad = self.current_quad()
        matrixAddress = currentQuad.leftOp
        firstIndex = currentQuad.rightOp
        secondIndex = currentQuad.resultTemp

        temporalMatrix = np.empty([firstIndex, secondIndex])

        counter = 0

        # Fill in the matrix with its values from the addresses
        for x in range(firstIndex):
            for y in range(secondIndex):
                temporalMatrix[x][y] = self.check_memory(matrixAddress + counter)
                counter += 1
            print(f'printing:{temporalMatrix[x]}:')

        self.increase_current_quad_pointer()
