def expo(a,b,c):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b%2 == 0:
        aa = expo(a,b//2,c)
        return(aa*aa)%c
    else:
        return(a * expo(a, b-1,c))%c
