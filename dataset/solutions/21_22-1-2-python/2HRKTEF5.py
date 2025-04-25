def calc(f):
    u = 1
    o = 10**18
    while o-u>=2:
        t = (u+o)//2
        if f(t):
            o = t
        else:
            u = t+1
    while not f(u):
        u = u+1
    return u