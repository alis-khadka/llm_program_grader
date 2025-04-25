def LCM(a, b):
    if a < b:
        a, b = b, a
    return a*b/GCD(a,b)


def GCD(a,b):
    r = a % b
    if r != 0:
        return GCD(b, r)
    else:
        return b