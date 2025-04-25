def expo(a,b,c):
    return fast_exp(a,b,c)

def fast_exp(b, e, m):
    r = 1
    if e & 1:
        r = b
    while e:
        e >>= 1
        b = (b * b) % m
        if e & 1 : r = (r * b) % m
    return r
