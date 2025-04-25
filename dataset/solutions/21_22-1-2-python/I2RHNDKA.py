def calc(f):
    n=0
    r=10**18
    while r-n>=2:
        c=(n+r)//2
        if not f(c):
            n=c
        else:
            r=c
    return r