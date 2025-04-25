def expo(a,b,c):
    r = 1
    a = a % c
    if (a == 0):
        return 0
    
    while (b > 0):
        if (b % 2 == 1):
            r = r * a % c
        b = b >> 1
        a = a * a % c
    
    return r