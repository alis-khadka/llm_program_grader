def LCM(a, b):
    return (a * b) / GCD(a, b)

def GCD(a, b):
    if b > a:
        a, b = b, a
    while a % b > 0:
        r = a % b
        a = b
        b = r
    return b