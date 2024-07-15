def multiply(a, b, /):
    try:
        return int(a) * int(b)
    except ValueError or TypeError:
        return "Atleast 1 argument is not a number"


def subtract(a, b, /):
    try:
        return int(a) - int(b)
    except ValueError or TypeError:
        return "Atleast 1 argument is not a number"


def divide(a, b, /):
    try:
        return int(a) / int(b)
    except ValueError:
        return "Atleast 1 argument is not a number"


def exponentiate(a, b, /):
    try:
        return int(a) ** int(b)
    except ValueError:
        return "Atleast 1 argument is not a number"


def randomn(a, b, /):
    import random
    return random.randrange(a, b)


def sround(n, d=1, /):
    return round(n / d) * d


def fibonacci(r: range | int = range(1, 10), /):
    if type(r) is int:
        r = range(0, r)
    a = 1
    b = 0
    length = r[-1]
    done = 0
    output = []
    while done != length:
        done += 1
        a, b = a + b, a
        output.append(a)

    return output[r[0]:r[-1]]


class AdvancedNum(float):
    def root(self, other, /):
        return other ** (1 / self)

    def successor(self, /):
        if int(self) == self:
            return int(self + 1)
        else:
            raise ValueError("can only get successors of integers")

    def predecessor(self, /):
        if int(self) == self:
            return int(self - 1)
        else:
            raise ValueError("can only get predecessors of integers")

    def type(self, /):
        if self == 0:
            return "natural"
        elif int(self) != self:
            return "rational"
        elif self >= 1:
            return "counting"
        elif self < 0:
            return "integer"

    def log(self, other, /):
        import math
        return math.log(other, self)
