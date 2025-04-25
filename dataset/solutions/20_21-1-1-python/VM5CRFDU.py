def expo(a,b,c):
    if b == 0:
        return 1 % c
    res = a % c
    b = b-1
    while b > 0:
        if b%2 != 0:
            b = b-1
            res = res*a % c
        else:
            a = (a*a) %c
            b = b//2
    return res