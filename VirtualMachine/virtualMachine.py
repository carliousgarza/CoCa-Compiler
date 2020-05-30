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
            "print": self.print,
            "read": self.read,
            "GOTOF": self.gotof,
            "GOTO": self.goto,
            "ERA": self.era,
            "RETURN": self.ret,
            "GOSUB": self.gosub,
            "ENDFUNC": self.endfunc,
            "PARAM": self.param,
            "VERIF": self.verif,
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

    def check_memory(self, operand_address):
        #This function checks where the operand_address lies, and calls
        #check_type_and_return_true_value in order to return its true value to
        #the caller

        if operand_address < 10000:
            value = self.TEMPORAL[operand_address]
            if value is None:
                raise Exception(f'Using an operand that has not been assigned a value yet')
            true_value = self.check_type_and_return_true_value(value, operand_address, "temporal")
            return true_value
        elif operand_address < 20000:
            operand_address -= 10000
            value = self.GLOBAL[operand_address]
            if value is None:
                raise Exception(f'Using an operand that has not been assigned a value yet')
            true_value = self.check_type_and_return_true_value(value, operand_address, "global")
            return true_value
        elif operand_address < 30000:
            operand_address -= 20000
            value = self.LOCAL[operand_address]
            if value is None:
                raise Exception(f'Using an operand that has not been assigned a value yet')
            true_value = self.check_type_and_return_true_value(value, operand_address, "local")
            return true_value
        elif operand_address < 40000:
            value = self.CONSTANT[operand_address].operand
            if value is None:
                raise Exception(f'Using an operand that has not been assigned a value yet')
            true_value = self.check_type_and_return_true_value(value, operand_address, "constant")
            return true_value
        elif operand_address < 50000:
            operand_address -= 40000
            addressValue = int(self.POINTER[operand_address])
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

    def set_value(self, value, value_address):
        # This function receives a value and an address to store it in

        if value_address < 10000:
            self.TEMPORAL[value_address] = value
            print(f'setting value {value} to temporal address({value_address})')

        elif value_address < 20000:
            print(f'setting value {value} to global address({value_address})')
            value_address -= 10000
            self.GLOBAL[value_address] = value

        elif value_address < 30000:
            print(f'setting value {value} to local address({value_address})')
            value_address -= 20000
            self.LOCAL[value_address] = value

        elif value_address < 40000:
            raise Exception("You should not be assigning stuff to constant address")

        elif value_address < 50000:
            value_address -= 40000
            if self.current_quad().operator != '=':
                print(f'setting {value} to pointer {value_address + 40000}')
                self.POINTER[value_address] = value
            else:
                print(f'extracting address value from pointer {value_address + 40000}')
                new_value_address = self.POINTER[value_address]
                self.set_value(value, new_value_address)
        else:
            raise Exception("You should not be here man!")

    def assign(self):
        # Get the current quad, and its addresses
        current_quad = self.current_quad()
        left_operand_address = current_quad.leftOp
        right_operand_address = current_quad.rightOp

        # Get what type of memory right_operand_address is stored in, and get its true value
        right_value = self.check_memory(right_operand_address)

        # removes "" and '' from chars and strings
        if type(right_value) is str and (right_value.startswith("\"") or right_value.startswith("\'")):
            right_value = right_value[1:-1]

        self.set_value(right_value, left_operand_address)

        self.increase_current_quad_pointer()

    def add(self):
        # Get the current quad, and its addresses
        current_quad = self.current_quad()
        left_operand_address = current_quad.leftOp
        right_operand_address = current_quad.rightOp
        result_address = current_quad.resultTemp
        # Get what type of memory left_operand_address is stored in, and get its true value
        left_value = self.check_memory(left_operand_address)
        # Get what type of memory right_operand_address is stored in, and get its true value
        right_value = self.check_memory(right_operand_address)

        if type(left_value) is str:
            left_value = left_value[1:-1]
            if type(right_value) is not str:
                raise Exception('DANGER! You should not be here')
            right_value = right_value[1:-1]

        # Get the real result of adding both operands together
        result = left_value + right_value

        print(f'{left_value} + {right_value} = {result}')

        # Check where to store the result and store it
        self.set_value(result, result_address)

        self.increase_current_quad_pointer()

    def subtract(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        left_operand_address = current_quad.leftOp
        right_operand_address = current_quad.rightOp
        result_address = current_quad.resultTemp

        # Get what type of memory left_operand_address is stored in, and get its true value
        left_value = self.check_memory(left_operand_address)
        # Get what type of memory right_operand_address is stored in, and get its true value
        right_value = self.check_memory(right_operand_address)

        # Get the result of adding both operands together
        result = left_value - right_value

        print(f'{left_value} - {right_value} = {result}')

        # Check where to store the result and store it
        self.set_value(result, result_address)

        self.increase_current_quad_pointer()

    def multiply(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        left_operand_address = current_quad.leftOp
        right_operand_address = current_quad.rightOp
        result_address = current_quad.resultTemp

        # Get what type of memory left_operand_address is stored in, and get its true value
        left_value = self.check_memory(left_operand_address)

        # Get what type of memory right_operand_address is stored in, and get its true value
        right_value = self.check_memory(right_operand_address)

        # Get the result of adding both operands together
        result = left_value * right_value

        print(f'{left_value} * {right_value} = {result}')

        # Check where to store the result and store it
        self.set_value(result, result_address)

        self.increase_current_quad_pointer()

    def divide(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        left_operand_address = current_quad.leftOp
        right_operand_address = current_quad.rightOp
        result_address = current_quad.resultTemp

        # Get what type of memory left_operand_address is stored in, and get its true value
        left_value = self.check_memory(left_operand_address)

        # Get what type of memory right_operand_address is stored in, and get its true value
        right_value = self.check_memory(right_operand_address)

        # Get the result of adding both operands together
        result = left_value / right_value

        print(f'{left_value} / {right_value} = {result}')

        # Check where to store the result and store it
        self.set_value(result, result_address)

        self.increase_current_quad_pointer()

    def print(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        operand_address = current_quad.leftOp

        operand_value = self.check_memory(operand_address)

        print(operand_value)

        self.increase_current_quad_pointer()

    def read(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        operand_address = current_quad.leftOp
        type_of_operand = current_quad.rightOp

        input_value = input()
        if type_of_operand == 'int':
            input_value = int(input_value)
        if type_of_operand == 'string':
            input_value = str(input_value)
        if type_of_operand == 'char':
            if len(input_value) > 1:
                raise Exception('Cannot input string to char')
            input_value = str(input_value)
        if type_of_operand == 'float':
            input_value = float(input_value)

        self.set_value(input_value, operand_address)

        print(f'Input {input_value} to {operand_address}')
        self.increase_current_quad_pointer()

    def greater_than(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        left_operand_address = current_quad.leftOp
        right_operand_address = current_quad.rightOp
        result_address = current_quad.resultTemp

        # Get what type of memory left_operand_address is stored in, and get its true value
        left_value = self.check_memory(left_operand_address)

        # Get what type of memory right_operand_address is stored in, and get its true value
        right_value = self.check_memory(right_operand_address)

        if left_value > right_value:
            self.set_value(True, result_address)
        else:
            self.set_value(False, result_address)

        self.increase_current_quad_pointer()

    def less_than(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        left_operand_address = current_quad.leftOp
        right_operand_address = current_quad.rightOp
        result_address = current_quad.resultTemp

        # Get what type of memory left_operand_address is stored in, and get its true value
        left_value = self.check_memory(left_operand_address)

        # Get what type of memory right_operand_address is stored in, and get its true value
        right_value = self.check_memory(right_operand_address)

        if left_value < right_value:
            self.set_value(True, result_address)
        else:
            self.set_value(False, result_address)

        self.increase_current_quad_pointer()

    def equal(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        left_operand_address = current_quad.leftOp
        right_operand_address = current_quad.rightOp
        result_address = current_quad.resultTemp

        # Get what type of memory left_operand_address is stored in, and get its true value
        left_value = self.check_memory(left_operand_address)

        # Get what type of memory right_operand_address is stored in, and get its true value
        right_value = self.check_memory(right_operand_address)

        if left_value == right_value:
            self.set_value(True, result_address)
        else:
            self.set_value(False, result_address)

        self.increase_current_quad_pointer()

    def greater_than_or_equal(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        left_operand_address = current_quad.leftOp
        right_operand_address = current_quad.rightOp
        result_address = current_quad.resultTemp

        # Get what type of memory left_operand_address is stored in, and get its true value
        left_value = self.check_memory(left_operand_address)

        # Get what type of memory right_operand_address is stored in, and get its true value
        right_value = self.check_memory(right_operand_address)

        if left_value >= right_value:
            self.set_value(True, result_address)
        else:
            self.set_value(False, result_address)

        self.increase_current_quad_pointer()

    def less_than_or_equal(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        left_operand_address = current_quad.leftOp
        right_operand_address = current_quad.rightOp
        result_address = current_quad.resultTemp

        # Get what type of memory left_operand_address is stored in, and get its true value
        left_value = self.check_memory(left_operand_address)

        # Get what type of memory right_operand_address is stored in, and get its true value
        right_value = self.check_memory(right_operand_address)

        if left_value <= right_value:
            self.set_value(True, result_address)
        else:
            self.set_value(False, result_address)

        self.increase_current_quad_pointer()

    def not_equal(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        left_operand_address = current_quad.leftOp
        right_operand_address = current_quad.rightOp
        result_address = current_quad.resultTemp

        # Get what type of memory left_operand_address is stored in, and get its true value
        left_value = self.check_memory(left_operand_address)

        # Get what type of memory right_operand_address is stored in, and get its true value
        right_value = self.check_memory(right_operand_address)

        if left_value != right_value:
            self.set_value(True, result_address)
        else:
            self.set_value(False, result_address)

        self.increase_current_quad_pointer()

    def and_op(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        left_operand_address = current_quad.leftOp
        right_operand_address = current_quad.rightOp
        result_address = current_quad.resultTemp

        # Get what type of memory left_operand_address is stored in, and get its true value
        left_value = self.check_memory(left_operand_address)

        # Get what type of memory right_operand_address is stored in, and get its true value
        right_value = self.check_memory(right_operand_address)

        if left_value and right_value:
            self.set_value(True, result_address)
        else:
            self.set_value(False, result_address)

        self.increase_current_quad_pointer()

    def or_op(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        left_operand_address = current_quad.leftOp
        right_operand_address = current_quad.rightOp
        result_address = current_quad.resultTemp

        # Get what type of memory left_operand_address is stored in, and get its true value
        left_value = self.check_memory(left_operand_address)

        # Get what type of memory right_operand_address is stored in, and get its true value
        right_value = self.check_memory(right_operand_address)

        if left_value or right_value:
            self.set_value(True, result_address)
        else:
            self.set_value(False, result_address)

        self.increase_current_quad_pointer()

    def gotof(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        conditional_address = current_quad.leftOp
        quadruple_to_jump = current_quad.resultTemp

        # Get what type of memory left_operand_address is stored in, and get its true value
        conditional_value = self.check_memory(conditional_address)

        if not conditional_value:
            self.quadPointer = quadruple_to_jump
        else:
            self.increase_current_quad_pointer()

    def goto(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        quadruple_to_jump = current_quad.resultTemp

        self.quadPointer = quadruple_to_jump

    def era(self):
        self.increase_current_quad_pointer()

    def param(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        passed_param_address = current_quad.leftOp
        parameter_address = current_quad.resultTemp

        # gets the param value from previous memory, as we have migrated for now
        passed_param_value = self.check_memory(passed_param_address)

        # appends it so gosub can empty it
        self.parameterStack.append({'value': passed_param_value, 'address': parameter_address})

        self.increase_current_quad_pointer()

    def gosub(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        future_temporal_to_assign_return = current_quad.leftOp
        quad_to_jump = current_quad.resultTemp

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

        while self.parameterStack:
            print(self.parameterStack.pop(), "removed from parameterStack")

        print(f'Function called, going to quad {quad_to_jump}')
        self.functionStack.append({'quadruple': self.quadPointer+1, 'address': future_temporal_to_assign_return})
        self.quadPointer = quad_to_jump

    def ret(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        return_value_address = current_quad.resultTemp

        # Get the return real value while we are still in the returning function's context
        return_value = self.check_memory(return_value_address)

        # Change context
        previous_local_memory = self.localMemoryStack.pop()
        previous_temporal_memory = self.temporalMemoryStack.pop()
        previous_pointer_memory = self.pointerMemoryStack.pop()
        previous_function = self.functionStack.pop()
        self.LOCAL = previous_local_memory
        self.TEMPORAL = previous_temporal_memory
        self.POINTER = previous_pointer_memory

        go_back_quadruple = previous_function['quadruple']

        # Set the return value
        print(f'Returning {return_value} and going back to quadruple {go_back_quadruple}')
        self.set_value(return_value, previous_function['address'])

        # Go back
        self.quadPointer = go_back_quadruple

    def endfunc(self):
        # Change context
        previous_local_memory = self.localMemoryStack.pop()
        previous_temporal_memory = self.temporalMemoryStack.pop()
        previous_pointer_memory = self.pointerMemoryStack.pop()
        previous_function = self.functionStack.pop()
        self.LOCAL = previous_local_memory
        self.TEMPORAL = previous_temporal_memory
        self.POINTER = previous_pointer_memory

        # IF the previous function is expecting a return address and we reached ENDFUNC, we have a runtime error
        if previous_function['address'] is not None:
            raise Exception('Error! Reached end of function without a return')

        go_back_quadruple = previous_function['quadruple']
        # Go back
        print(f'Going back to quadruple {go_back_quadruple}')
        self.quadPointer = go_back_quadruple

    def verif(self):
        # Get the current quad, its operands and address
        current_quad = self.current_quad()
        index_address = current_quad.leftOp
        lower_limit_address = current_quad.rightOp
        upper_limit_address = current_quad.resultTemp

        # Get what type of memory it is stored in, and get its true value
        index_value = self.check_memory(index_address)

        # Get what type of memory it is stored in, and get its true value
        lower_limit_value = self.check_memory(lower_limit_address)

        # Get what type of memory it is stored in, and get its true value
        upper_limit_value = self.check_memory(upper_limit_address)

        print(f'Verifying that {index_value} lies between {lower_limit_value} and {upper_limit_value}')

        if upper_limit_value >= index_value >= lower_limit_value:
            print("The value is between the limits!")
        else:
            raise IndexError("Index out of range")

        self.increase_current_quad_pointer()
