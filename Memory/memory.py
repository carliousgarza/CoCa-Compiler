from antlr4 import *


class Memory:
    def __init__(self):
        self.mem_temp_int = 0
        self.mem_temp_float = 2000
        self.mem_temp_string = 4000
        self.mem_temp_bool = 6000
        self.mem_temp_char = 8000

        self.mem_global_int = 10000
        self.mem_global_float = 12000
        self.mem_global_string = 14000
        self.mem_global_bool = 16000
        self.mem_global_char = 18000

        self.mem_local_int = 20000
        self.mem_local_float = 22000
        self.mem_local_string = 24000
        self.mem_local_bool = 26000
        self.mem_local_char = 28000

        self.mem_constant = 30000

        self.mem_pointers = 40000
