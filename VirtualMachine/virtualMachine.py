class VirtualMachine:
    def __init__(self, quadruples, constantTable):
        self.quadPointer = 0
        self.quadruples = quadruples

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
            "GOTO": self.goto,
            "=": self.assign,
            "print": self.print,
            "read": self.read,
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
                if value == "true":
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
                if value == "true":
                    return True
                else:
                    return False
            elif address < 10000:
                return str(value)

    def set_value(self, value, value_address):
        # This function receives a value and an address to store it in

        if value_address < 10000:
            self.TEMPORAL.insert(value_address, value)
            print(f'setting value {value} to temporal address({value_address})')

        elif value_address < 20000:
            print(f'setting value {value} to global address({value_address})')
            value_address -= 10000
            self.GLOBAL.insert(value_address, value)

        elif value_address < 30000:
            print(f'setting value {value} to local address({value_address})')
            value_address -= 20000
            self.LOCAL.insert(value_address, value)

        elif value_address < 40000:
            raise Exception("You should not be assigning stuff to constant address")

        elif value_address < 50000:
            print(f'setting value {value} to pointer address({value_address})')
            value_address -= 40000
            self.POINTER.insert(value_address, value)

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

        left_value = None
        right_value = None

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

        left_value = None
        right_value = None

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

        left_value = None
        right_value = None

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

        operand_value =  self.check_memory(operand_address)

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


    def goto(self):
        # This function resolves a goto quadruple

        print("goto quad")
        self.increase_current_quad_pointer()

