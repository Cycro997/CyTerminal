def l_and(a: bool | int, b: bool | int):
    return bool(a and b)


def l_not(a: bool | int):
    return bool(not a)


def l_or(a: bool | int, b: bool | int):
    return bool(a or b)


def nor(a: bool | int, b: bool | int):
    return bool(l_not(l_or(a, b)))


def nand(a: bool | int, b: bool | int):
    return bool(l_not(l_and(a, b)))


def xor(a: bool | int, b: bool | int):
    return bool(a ^ b)


def xnor(a: bool | int, b: bool | int):
    return bool(l_not(xor(a, b)))


def l_is(a: bool | int, b: bool | int):
    return bool(l_or(nor(a, b), l_and(a, b)))


def nis(a: bool | int, b: bool | int):
    return bool(l_not(l_is(a, b)))


def base2(b10: int):
    return bin(b10)
