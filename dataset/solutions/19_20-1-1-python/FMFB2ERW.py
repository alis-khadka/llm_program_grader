def GGT(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    if r == 0:
        return b
    else:
        return GGT (b, r)

def LCM(a, b):
    ggt = GGT(a, b)
    return a * b / ggt