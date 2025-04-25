def GGT(a, b): 
    while a % b > 0:
        r = a % b
        a,b = b,r
    return b

def LCM(a, b):
    nenner = a * b
    zaehler = GGT(a,b)
    return nenner / zaehler