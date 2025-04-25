def expo(a,b,c):
    if b == 0:
        return 1 % c
    if b == 1:
        return a % c
    
    if b % 2 == 0:
        tmp = expo(a, b//2, c)
        return (tmp * tmp) % c
    else:
        return (expo(a, b-1, c) * a) % c
