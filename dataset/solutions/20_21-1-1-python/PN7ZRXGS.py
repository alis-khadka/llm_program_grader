def expo(a, b, c):
    res = 1
    b = b % c
    while(b>0):
        if(b % 2 == 1):
            res = (res*a) % c
        b = b//2
        a = (a*a) % c
    return res
