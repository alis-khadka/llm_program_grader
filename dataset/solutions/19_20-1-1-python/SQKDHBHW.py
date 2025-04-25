def GCD(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    if r == 0:
        return b
    else:
        return GCD(r, b)

def LCM(a, b):
    return a * b / GCD(a, b)