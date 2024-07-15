builtinround=round


def multiply(a, b, *c):
    try:
        return int(a) * int(b)
    except:
        return "Atleast 1 argument is not a number"
def subtract(a, b, *c):
    try:
        return int(a) - int(b)
    except ValueError:
        return "Atleast 1 argument is not a number"
def divide(a, b, *c):
    try:
        return int(a) / int(b)
    except ValueError:
        return "Atleast 1 argument is not a number"
def exponentiate(a, b, *c):
    try:
        return int(a) ** int(b)
    except ValueError:
        return "Atleast 1 argument is not a number"
def randomn(a,b):
    import random
    return random.randrange(a,b)
def round(n,d=1):
    return builtinround(n/d)*d

class advnum(float):
    def root(self, other):
        return other**(1/self)
    def successor(self):
        if int(self)==self:
            return int(self+1)
        else:
            raise ValueError("can only get successors of integers")
    def predecessor(self):
        if int(self)==self:
            return int(self-1)
        else:
            raise ValueError("can only get predecessors of integers")
    def type(self):
        if self==0:
            return "natural"
        elif int(self)!=(self):
            return "rational"
        elif self>=1:
            return "counting"
        elif self<0:
            return "integer"
    def log(self, other):
        import math
        return math.log(other,self)
del builtinround