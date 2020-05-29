class VirtualMachine:
    def __init__(self, quadruples, constantTable):
        self.currentQuadPointer = 0
        self.programQuadruples = quadruples
        self.GLOBAL = [10000]
        self.LOCAL = [10000]
        self.TEMPORAL = {}
        self.CONSTANT = constantTable
        self.operators = {
            "+": self.add,
            "-": self.subtract,
            "/": self.divide,
            "*": self.multiply,
            "GOTO": self.goto,
            "=": self.assign,
        }

    def begin(self):
        #This function begins running and executing all quadruples in the program

        counter = 0
        while self.currentQuadPointer < len(self.programQuadruples):
            current_quad = self.current_quad()
            operator = current_quad.operator
            self.operators.get(operator)()


    def increase_current_quad_pointer(self):
        #This function just increases the current quadruple pointer by one
        self.currentQuadPointer += 1

    def current_quad(self):
        #This function returns the current quadruple the pointer is pointing at
        return self.programQuadruples[self.currentQuadPointer]

    def check_memory(self, operand_address):
        #This function checks where the operand_address lies, and calls
        #check_type_and_return_true_value in order to return its true value to
        #the caller

        print(f'check_memory {operand_address}')
        if operand_address < 10000:
            print("temporal")
        elif operand_address < 20000:
            print("global")
        elif operand_address < 30000:
            print("local")
        elif operand_address < 40000:
            #Constant

            #Here .address is actually the value
            operand_value = self.CONSTANT[operand_address].address

            #Get the value of the operand in its real type(int, bool, string, etc.)
            true_value = self.check_type_and_return_true_value(operand_value, operand_address, "constant")

            return(true_value)
        elif operand < 50000:
            print("pointer")
        else:
            print("you should not get here")

    def check_type_and_return_true_value(self, operand, address, memory):
        #This function gets the value of an operand as a string, and turns it into
        #its true value, based on its address

        print(f'check_type_and_return_true_value {operand}, {address}, {memory}')
        if memory == "temporal":
            print("temp")
        elif memory == "global":
            print("global")
        elif memory == "local":
            print("local")
        elif memory == "constant":
            if self.CONSTANT[address].type == "int":
                return(int(operand))
            elif self.CONSTANT[address].type == "float":
                return(float(operand))
            elif self.CONSTANT[address].type == "string":
                return(str(operand))
            elif self.CONSTANT[address].type == "bool":
                if self.CONSTANT[address].address == "true":
                    return(True)
                else:
                    return(False)
            else:
                print("should be char?")
        else:
            print("pointer")

    def set_value(self, result, result_address):
        #This function receives a result, and a result address, in order to
        #save said result in the given result address

        print(f'setting value {result} -> Address({result_address})')
        if result_address < 10000:
            #Temporal Result
            self.TEMPORAL[result_address] = result
        elif result_address < 20000:
            print("result global")
        elif result_address < 30000:
            print("result local")
        elif result_address < 40000:
            print("result constant")
        elif result_address < 50000:
            print("result pointer")
        else:
            print("you should not get here")

    def add(self):
        #This function resolves an addition quadruple

        #Get the current quad, its operands and address
        current_quad = self.current_quad()
        left_operand_address = current_quad.leftOp
        right_operand_address = current_quad.rightOp
        result_address = current_quad.resultTemp
        print(f'{left_operand_address} + {right_operand_address} -> {result_address}')

        left_value = None
        right_value = None

        #Get what type of memory left_operand_address is stored in, and get its true value
        left_value = self.check_memory(left_operand_address)

        #Get what type of memory right_operand_address is stored in, and get its true value
        right_value = self.check_memory(right_operand_address)

        #Get the result of adding both operands together
        result = left_value + right_value

        print(f'{left_value} + {right_value} = {result} -> Address({result_address})')

        #Check where to store the result and store it
        self.set_value(result, result_address)

        self.increase_current_quad_pointer()

    def subtract(self):
        #This function resolves a subtraction quadruple

        #Get the current quad, its operands and address
        current_quad = self.current_quad()
        left_operand_address = current_quad.leftOp
        right_operand_address = current_quad.rightOp
        result_address = current_quad.resultTemp
        print(f'{left_operand_address} + {right_operand_address} -> {result_address}')

        left_value = None
        right_value = None

        #Get what type of memory left_operand_address is stored in, and get its true value
        left_value = self.check_memory(left_operand_address)

        #Get what type of memory right_operand_address is stored in, and get its true value
        right_value = self.check_memory(right_operand_address)

        #Get the result of adding both operands together
        result = left_value - right_value

        print(f'{left_value} - {right_value} = {result} -> Address({result_address})')

        #Check where to store the result and store it
        self.set_value(result, result_address)

        self.increase_current_quad_pointer()

    def multiply(self):
        #This function resolves a multiplication quadruple

        #Get the current quad, its operands and address
        current_quad = self.current_quad()
        left_operand_address = current_quad.leftOp
        right_operand_address = current_quad.rightOp
        result_address = current_quad.resultTemp
        print(f'{left_operand_address} + {right_operand_address} -> {result_address}')

        left_value = None
        right_value = None

        #Get what type of memory left_operand_address is stored in, and get its true value
        left_value = self.check_memory(left_operand_address)

        #Get what type of memory right_operand_address is stored in, and get its true value
        right_value = self.check_memory(right_operand_address)

        #Get the result of adding both operands together
        result = left_value * right_value

        print(f'{left_value} * {right_value} = {result} -> Address({result_address})')

        #Check where to store the result and store it
        self.set_value(result, result_address)

        self.increase_current_quad_pointer()

    def divide(self):
        #This function resolves a division quadruple

        #Get the current quad, its operands and address
        current_quad = self.current_quad()
        left_operand_address = current_quad.leftOp
        right_operand_address = current_quad.rightOp
        result_address = current_quad.resultTemp
        print(f'{left_operand_address} + {right_operand_address} -> {result_address}')

        left_value = None
        right_value = None

        #Get what type of memory left_operand_address is stored in, and get its true value
        left_value = self.check_memory(left_operand_address)

        #Get what type of memory right_operand_address is stored in, and get its true value
        right_value = self.check_memory(right_operand_address)

        #Get the result of adding both operands together
        result = left_value / right_value

        print(f'{left_value} / {right_value} = {result} -> Address({result_address})')

        #Check where to store the result and store it
        self.set_value(result, result_address)

        self.increase_current_quad_pointer()

    def goto(self):
        #This function resolves a goto quadruple

        print("goto quad")
        self.increase_current_quad_pointer()

    def assign(self):
        #This function resolves an assignation quadruple

        print("assign quad")
        self.increase_current_quad_pointer()
