class TemporalDimensionVariable:
    def __init__(self, address, first_index, second_index, type, size):
        self.address = address
        self.first_index = first_index
        self.second_index = second_index
        self.vartype = type
        self.size = size