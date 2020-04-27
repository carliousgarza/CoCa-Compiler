from antlr4 import *
from Compiler.function import *
from Compiler.variable import *
from Compiler.compiler import *

class Quadruple:
    def __init__(self, operator, leftOp, rightOp, resultTemp):
        self.operator = operator
        self.leftOp = leftOp
        self.rightOp = rightOp
        self.resultTemp = resultTemp
