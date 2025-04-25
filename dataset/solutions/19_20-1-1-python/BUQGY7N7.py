def LCM(a, b):
    return ((a*b) / (gcd(a, b)))
    
def gcd(a, b):
    if a < b:
        a, b = b, a 

    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)