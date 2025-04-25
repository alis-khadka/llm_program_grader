def expo(a,b,c):
    res=1
    if(b==0):
        return 1
    elif (b%2==0):
        x = expo(a,b//2,c)
        return x  *x % c
    else:
        return expo(a,b-1,c) * a % c
    return res