def ggt(a, b):
    while a % b > 0:
        r = a % b
        a = b
        b = r
    return b

def LCM(a, b):
    #ggt*kgv = a*b --> kgv = a*b/ggt
    #ggt ist hier ggt_calc und der ggt wird mit hilfe vom Algorithmus der VL berechnet
    ggt_calc = ggt(a,b)
    lcm_calc = a*b/ggt_calc
    return lcm_calc