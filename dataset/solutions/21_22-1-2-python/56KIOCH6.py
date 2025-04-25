def calc(f):
    l=0
    r=int(1e18)
    while r-l:
        x=(l+r)//2
        if f(x):
            r=x
        else:
            l=x+1
    return l