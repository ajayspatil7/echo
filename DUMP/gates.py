

def AND(a, b, c):
    return a and b and c


def OR(a, b, c):
    return a or b or c


def NOT(a):
    return int(not a)


def XOR(a, b):
    return int(a ^ b)


def NAND(a, b, c):
    return int(not (a and b and c))


def NOR(a, b, c):
    return int(not (a or b or c))


def XNOR(a, b):
    return int(not (a ^ b))


print(AND(1, 1, 1))
print(OR(1, 1, 1))
print(NOT(0))

print(NAND(1, 1, 1))
print(NOR(1, 1, 1))

print(XOR(1, 1))
print(XNOR(1, 1))



