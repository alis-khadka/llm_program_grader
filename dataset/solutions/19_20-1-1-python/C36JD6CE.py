def LCM(a, b):
    gcd = GCD(a, b)
    return (a * b) / gcd

def GCD(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    if r > 0:
        return GCD(b, r)
    else:
        return b