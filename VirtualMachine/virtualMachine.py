class VirtualMachine:
    def __init__(self, quadruples):
        self.currentQuadPointer = 0
        self.programQuadruples = quadruples

        # self.functionTable = {}
        # self.currentFunction = Function("global", "void", [], {})
        # self.constantTable = {}
        # self.operatorStack = []
        # self.operandStack = []
        # self.jumpStack = []
        # self.typesStack = []
        # self.tempStack = []
        # self.scube = SemanticCube()
        # self.fromVariableStack = []
        # self.functionStack = []
        # self.memory = Memory()
        # self.temporalStack = []

        self.GLOBAL = []
        self.LOCAL = []
        self.CONSTANT = []
        self.TEMPORAL = []

    def begin(self):
        counter = 1
        for quad in self.programQuadruples:
            print(f'{counter} - {quad.operator},{quad.leftOp}.{quad.rightOp}.{quad.resultTemp}')
            counter+=1
