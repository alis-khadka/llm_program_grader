def getexponent(a, b, c):
    if b > 1:
        if b % 2 == 0:
            x = getexponent(a, b//2, c)
            return (x*x) % c
        else:
            return a * getexponent(a, b-1, c)
    else:
        return a
def expo(a, b, c):
    return getexponent(a, b, c) % c