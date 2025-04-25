def GGT(a,b):
    if a < b:
        a, b = b, a
    r = a % b
    if r != 0:
        return GGT(b, r)
    else:
        return b


def LCM(a, b):
    return(a*b / GGT(a,b))