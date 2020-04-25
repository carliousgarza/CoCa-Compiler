from antlr4 import *


class semanticCube():
    def __init__(self):
        cube = {
            "int"{
                    "*"{
                        "int": "int",
                        "float": "float",
                        "char": "Error, can't multiply an integer with a char",
                        "string": "Error, can't multiply an integer with a string",
                        "bool": "Error, can't multiply an integer with a boolean"
                    },
                    "/"{
                        "int": "int",
                        "float": "float",
                        "char": "Error, can't divide an integer by a char",
                        "string": "Error, can't divide an integer by a string",
                        "bool": "Error, can't divide an integer by a boolean"
                    },
                    "+"{
                        "int": "int",
                        "float": "float",
                        "char": "Error, can't add an integer and a char",
                        "string": "Error, can't add an integer and a string",
                        "bool": "Error, can't add an integer and a boolean"
                    },
                    "-"{
                        "int": "int",
                        "float": "float",
                        "char": "Error, can't subtract an integer by a char",
                        "string": "Error, can't subtract an integer by a string",
                        "bool": "Error, can't subtract an integer by a boolean"
                    },
                    "<"{
                        "int": "int",
                        "float": "float",
                        "char": "Error, can't compare an integer with a char",
                        "string": "Error, can't compare an integer with a string",
                        "bool": "Error, can't compare an integer with a boolean"
                    },
                    ">"{
                        "int": "bool",
                        "float": "bool",
                        "char": "Error, can't compare an integer with a char",
                        "string": "Error, can't compare an integer with a string",
                        "bool": "Error, can't compare an integer with a boolean"
                    },
                    "<="{
                        "int": "bool",
                        "float": "bool",
                        "char": "Error, can't compare an integer with a char",
                        "string": "Error, can't compare an integer with a string",
                        "bool": "Error, can't compare an integer with a boolean"
                    },
                    ">="{
                        "int": "bool",
                        "float": "bool",
                        "char": "Error, can't compare an integer with a char",
                        "string": "Error, can't compare an integer with a string",
                        "bool": "Error, can't compare an integer with a boolean"
                    },
                    "=="{
                        "int": "bool",
                        "float": "bool",
                        "char": "Error, can't compare an integer with a char",
                        "string": "Error, can't compare an integer with a string",
                        "bool": "Error, can't compare an integer with a boolean"
                    },
                    "!="{
                        "int": "bool",
                        "float": "bool",
                        "char": "Error, can't compare an integer with a char",
                        "string": "Error, can't compare an integer with a string",
                        "bool": "Error, can't compare an integer with a boolean"
                    },
                    "="{
                        "int": "int",
                        "float": "Error, can't assign a float value to an integer",
                        "char": "Error, can't assign a char value to an integer",
                        "string": "Error, can't assign a string value to an integer",
                        "bool": "Error, can't assign a boolean value to an integer"
                    }
                },
            "float"{
                    "*"{
                        "int": "float",
                        "float": "float",
                        "char": "Error, can't multiply a float with a char",
                        "string": "Error, can't multiply a float with a string",
                        "bool": "Error, can't multiply a float with a boolean"
                    },
                    "/"{
                        "int": "float",
                        "float": "float",
                        "char": "Error, can't divide a float by a char",
                        "string": "Error, can't divide a float by a string",
                        "bool": "Error, can't divide a float by a boolean"
                    },
                    "+"{
                        "int": "float",
                        "float": "float",
                        "char": "Error, can't add a float and a char",
                        "string": "Error, can't add a float and a string",
                        "bool": "Error, can't add a float and a boolean"
                    },
                    "-"{
                        "int": "float",
                        "float": "float",
                        "char": "Error, can't subtract a float by a char",
                        "string": "Error, can't subtract a float by a string",
                        "bool": "Error, can't subtract a float by a boolean"
                    },
                    "<"{
                        "int": "bool",
                        "float": "bool",
                        "char": "Error, can't compare a float with a char",
                        "string": "Error, can't compare a float with a string",
                        "bool": "Error, can't compare a float with a boolean"
                    },
                    ">"{
                        "int": "bool",
                        "float": "bool",
                        "char": "Error, can't compare a float with a char",
                        "string": "Error, can't compare a float with a string",
                        "bool": "Error, can't compare a float with a boolean"
                    },
                    "<="{
                        "int": "bool",
                        "float": "bool",
                        "char": "Error, can't compare a float with a char",
                        "string": "Error, can't compare a float with a string",
                        "bool": "Error, can't compare a float with a boolean"
                    },
                    ">="{
                        "int": "bool",
                        "float": "bool",
                        "char": "Error, can't compare a float with a char",
                        "string": "Error, can't compare a float with a string",
                        "bool": "Error, can't compare a float with a boolean"
                    },
                    "=="{
                        "int": "bool",
                        "float": "bool",
                        "char": "Error, can't compare a float with a char",
                        "string": "Error, can't compare a float with a string",
                        "bool": "Error, can't compare a float with a boolean"
                    },
                    "!="{
                        "int": "bool",
                        "float": "bool",
                        "char": "Error, can't compare a float with a char",
                        "string": "Error, can't compare a float with a string",
                        "bool": "Error, can't compare a float with a boolean"
                    },
                    "="{
                        "int": "Error, can't assign an integer value to a float",
                        "float": "float",
                        "char": "Error, can't assign a char value to an float",
                        "string": "Error, can't assign a string value to an float",
                        "bool": "Error, can't assign a boolean value to an float"
                    }
                },
            "char"{
                    "*"{
                        "int": "Error, can't multiply a char with an integer",
                        "float": "Error, can't multiply a char with a float",
                        "char": "Error, can't multiply a char with a char",
                        "string": "Error, can't multiply a char with a string",
                        "bool": "Error, can't multiply a char with a boolean"
                    },
                    "/"{
                        "int": "Error, can't divide a char by an integer",
                        "float": "Error, can't divide a char by a char",
                        "char": "Error, can't divide a char by a char",
                        "string": "Error, can't divide a char by a string",
                        "bool": "Error, can't divide a char by a boolean"
                    },
                    "+"{
                        "int": "Error, can't add a char and an integer",
                        "float": "Error, can't add a char and a float",
                        "char": "Error, can't add a char and a char",
                        "string": "Error, can't add a char and a string",
                        "bool": "Error, can't add a char and a boolean"
                    },
                    "-"{
                        "int": "Error, can't subtract a char by an integer",
                        "float": "Error, can't subtract a char by a float",
                        "char": "Error, can't subtract a char by a char",
                        "string": "Error, can't subtract a char by a string",
                        "bool": "Error, can't subtract a char by a boolean"
                    },
                    "<"{
                        "int": "Error, can't compare a char with an integer",
                        "float": "Error, can't compare a char with a float",
                        "char": "Error, can't compare a char with a char using <",
                        "string": "Error, can't compare a char with a string",
                        "bool": "Error, can't compare a char with a boolean"
                    },
                    ">"{
                        "int": "Error, can't compare a char with an integer",
                        "float": "Error, can't compare a char with a float",
                        "char": "Error, can't compare a char with a char using >",
                        "string": "Error, can't compare a char with a string",
                        "bool": "Error, can't compare a char with a boolean"
                    },
                    "<="{
                        "int": "Error, can't compare a char with an integer",
                        "float": "Error, can't compare a char with a float",
                        "char": "Error, can't compare a char with a char using <=",
                        "string": "Error, can't compare a char with a string",
                        "bool": "Error, can't compare a char with a boolean"
                    },
                    ">="{
                        "int": "Error, can't compare a char with an integer",
                        "float": "Error, can't compare a char with a float",
                        "char": "Error, can't compare a char with a char using >=",
                        "string": "Error, can't compare a char with a string",
                        "bool": "Error, can't compare a char with a boolean"
                    },
                    "=="{
                        "int": "Error, can't compare a char with an integer",
                        "float": "Error, can't compare a char with a float",
                        "char": "bool",
                        "string": "Error, can't compare a char with a string",
                        "bool": "Error, can't compare a char with a boolean"
                    },
                    "!="{
                        "int": "Error, can't compare a char with an integer",
                        "float": "Error, can't compare a char with a float",
                        "char": "bool",
                        "string": "Error, can't compare a char with a string",
                        "bool": "Error, can't compare a char with a boolean"
                    },
                    "="{
                        "int": "Error,  can't assign an integer value to a char",
                        "float": "Error, can't assign a float value to an char",
                        "char": "char",
                        "string": "Error, can't assign a string value to an char",
                        "bool": "Error, can't assign a boolean value to an char"
                    }
                },
            "string"{
                    "*"{
                        "int": "Error, can't multiply a string with an integer",
                        "float": "Error, can't multiply a string with a float",
                        "char": "Error, can't multiply a string with a char",
                        "string": "Error, can't multiply a string with a string",
                        "bool": "Error, can't multiply a string with a boolean"
                    },
                    "/"{
                        "int": "Error, can't divide a string by an integer",
                        "float": "Error, can't divide a string by a char",
                        "char": "Error, can't divide a string by a char",
                        "string": "Error, can't divide a string by a string",
                        "bool": "Error, can't divide a string by a boolean"
                    },
                    "+"{
                        "int": "Error, can't add a string and an integer",
                        "float": "Error, can't add a string and a float",
                        "char": "Error, can't add a string and a char",
                        "string": "Error, can't add a string and a string",
                        "bool": "Error, can't add a string and a boolean"
                    },
                    "-"{
                        "int": "Error, can't subtract a string by an integer",
                        "float": "Error, can't subtract a string by a float",
                        "char": "Error, can't subtract a string by a char",
                        "string": "Error, can't subtract a string by a string",
                        "bool": "Error, can't subtract a string by a boolean"
                    },
                    "<"{
                        "int": "Error, can't compare a string with an integer",
                        "float": "Error, can't compare a string with a float",
                        "char": "Error, can't compare a string with a char",
                        "string": "Error, can't compare a string with a string using <",
                        "bool": "Error, can't compare a string with a boolean"
                    },
                    ">"{
                        "int": "Error, can't compare a string with an integer",
                        "float": "Error, can't compare a string with a float",
                        "char": "Error, can't compare a string with a char",
                        "string": "Error, can't compare a string with a string using >",
                        "bool": "Error, can't compare a string with a boolean"
                    },
                    "<="{
                        "int": "Error, can't compare a string with an integer",
                        "float": "Error, can't compare a string with a float",
                        "char": "Error, can't compare a string with a char",
                        "string": "Error, can't compare a string with a string using <=",
                        "bool": "Error, can't compare a string with a boolean"
                    },
                    ">="{
                        "int": "Error, can't compare a string with an integer",
                        "float": "Error, can't compare a string with a float",
                        "char": "Error, can't compare a string with a char",
                        "string": "Error, can't compare a string with a string using >=",
                        "bool": "Error, can't compare a string with a boolean"
                    },
                    "=="{
                        "int": "Error, can't compare a string with an integer",
                        "float": "Error, can't compare a string with a float",
                        "char": "Error, can't compare a string with a char",
                        "string": "bool",
                        "bool": "Error, can't compare a string with a boolean"
                    },
                    "!="{
                        "int": "Error, can't compare a string with an integer",
                        "float": "Error, can't compare a string with a float",
                        "char": "Error, can't compare a string with a char",
                        "string": "bool",
                        "bool": "Error, can't compare a string with a boolean"
                    },
                    "="{
                        "int": "Error,  can't assign an integer value to a string",
                        "float": "Error, can't assign a float value to an string",
                        "char": "string",
                        "string": "string",
                        "bool": "Error, can't assign a boolean value to an string"
                    }
                },
            "bool"{
                    "*"{
                        "int": "Error, can't multiply a boolean with an integer",
                        "float": "Error, can't multiply a boolean with a float",
                        "char": "Error, can't multiply a boolean with a char",
                        "string": "Error, can't multiply a boolean with a string",
                        "bool": "Error, can't multiply a boolean with a boolean"
                    },
                    "/"{
                        "int": "Error, can't divide a boolean by an integer",
                        "float": "Error, can't divide a boolean by a char",
                        "char": "Error, can't divide a boolean by a char",
                        "string": "Error, can't divide a boolean by a string",
                        "bool": "Error, can't divide a boolean by a boolean"
                    },
                    "+"{
                        "int": "Error, can't add a boolean and an integer",
                        "float": "Error, can't add a boolean and a float",
                        "char": "Error, can't add a boolean and a char",
                        "string": "Error, can't add a boolean and a string",
                        "bool": "Error, can't add a boolean and a boolean"
                    },
                    "-"{
                        "int": "Error, can't subtract a boolean by an integer",
                        "float": "Error, can't subtract a boolean by a float",
                        "char": "Error, can't subtract a boolean by a char",
                        "string": "Error, can't subtract a boolean by a string",
                        "bool": "Error, can't subtract a boolean by a boolean"
                    },
                    "<"{
                        "int": "Error, can't compare a boolean with an integer",
                        "float": "Error, can't compare a boolean with a float",
                        "char": "Error, can't compare a boolean with a char",
                        "string": "Error, can't compare a boolean with a string",
                        "bool": "Error, can't compare a boolean with a boolean using <"
                    },
                    ">"{
                        "int": "Error, can't compare a boolean with an integer",
                        "float": "Error, can't compare a boolean with a float",
                        "char": "Error, can't compare a boolean with a char",
                        "string": "Error, can't compare a boolean with a string",
                        "bool": "Error, can't compare a boolean with a boolean using >"
                    },
                    "<="{
                        "int": "Error, can't compare a boolean with an integer",
                        "float": "Error, can't compare a boolean with a float",
                        "char": "Error, can't compare a boolean with a char",
                        "string": "Error, can't compare a boolean with a string",
                        "bool": "Error, can't compare a boolean with a boolean using <="
                    },
                    ">="{
                        "int": "Error, can't compare a boolean with an integer",
                        "float": "Error, can't compare a boolean with a float",
                        "char": "Error, can't compare a boolean with a char",
                        "string": "Error, can't compare a boolean with a string,"
                        "bool": "Error, can't compare a boolean with a boolean using >="
                    },
                    "=="{
                        "int": "Error, can't compare a boolean with an integer",
                        "float": "Error, can't compare a boolean with a float",
                        "char": "Error, can't compare a boolean with a char",
                        "string": "Error, can't compare a boolean with a string",
                        "bool": "bool"
                    },
                    "!="{
                        "int": "Error, can't compare a boolean with an integer",
                        "float": "Error, can't compare a boolean with a float",
                        "char": "Error, can't compare a boolean with a char",
                        "string": "Error, can't compare a boolean with a string",
                        "bool": "bool"
                    },
                    "="{
                        "int": "Error,  can't assign an integer value to a boolean",
                        "float": "Error, can't assign a float value to an boolean",
                        "char": "Error, can't assign a char value to an boolean",
                        "string": "Error, can't assign a string value to an boolean",
                        "bool": "bool"
                    }
                }
            }
