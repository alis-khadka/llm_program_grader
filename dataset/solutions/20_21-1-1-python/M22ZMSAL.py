def expo(a,b,c):
    r=1
    if 1 & b:
        r=a
    while b:
        b>>=1
        a = (a*a)%c
        if b&1: r= (r*a)%c
    return r
    
pass