def calc(f):
    n=1
    while(f(n) == 0):
        n*=2
    if(f(n-1) == 0):
        return n
    m=n
    c=4
    while f(n)==0 or f(n-1)==1:
        if f(n)==1:
            n=n-m//c
        else:
            n=n+m//c
        c*=2
    return n