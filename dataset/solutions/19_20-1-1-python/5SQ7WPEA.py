def LCM(a, b):
    mult = a * b
    return mult/GCD(a, b)

def GCD(x, y):
    if x < y:
        x, y = y, x

    r = x % y
    if r != 0:
        return GCD(y, r)
    else:
        return y