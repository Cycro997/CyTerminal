def AND(a: bool, b: bool):
    return bool(a and b)
def NOT(a: bool):
    return bool(not a)
def OR(a: bool, b: bool):
    return bool(a or b)
def NOR(a: bool, b: bool):
    return bool(NOT(OR(a,b)))
def NAND(a: bool, b: bool):
    return bool(NOT(AND(a,b)))
def XOR(a: bool, b: bool):
    return bool(a ^ b)
def XNOR(a: bool, b: bool):
    return bool(NOT(XOR(a, b)))
def IS(a: bool, b: bool):
    return bool(OR(NOR(a, b), AND(a, b)))
def NIS(a: bool, b: bool):
    return bool(NOT(IS(a, b)))