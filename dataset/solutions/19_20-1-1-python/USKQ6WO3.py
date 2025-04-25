def LCM(a, b):
    return ( (a * b) / GCD(a, b) )
    
# GCD Implementierung aus Vorlesungsunterlagen
def GCD(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    if r > 0:
        return GCD(b, r)
    else:
        return b