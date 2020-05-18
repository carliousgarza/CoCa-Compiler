from antlr4 import *

class Memory:
    def __init__(self):
        print("Memory declared :)")
        self.global = 10000
        self.local = 20000
        self.constant = 30000
