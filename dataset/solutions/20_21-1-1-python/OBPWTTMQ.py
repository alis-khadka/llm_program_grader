def expo(a,b,c):
    if b == 0:
        return 1
    elif b % 2 == 0:
        e = expo(a,b//2,c)%c
        return (e*e)%c
    else:
        return ((expo(a,b-1,c)%c)*(a%c))%c
