def GCD(a, b):
    if a < b:
        hilf = a
        a = b
        b = hilf
    r = a % b
    if r != 0:
        return GCD(b, r)
    else:
        return b
        
    
def LCM(a, b):
    c = GCD(a, b)
    return (a * b)/c