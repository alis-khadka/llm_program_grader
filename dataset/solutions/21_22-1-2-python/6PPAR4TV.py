def calc(f):
    r = 10
    if f(0):
        return 0
    if f(1):
        return 1
    while f(r) == 0:
        r = r*10
    l = r//10
    while l<r-1:
        p = l+(r-l)//2
        if f(p):
            r = p
        else:
            l = p
    return r
    pass