def expo(a,b,c):
    if b==0:
        res = 1
    elif b==1:
        res = a
    elif b%2 == 0:
        res = (expo(a,b//2,c))
        res = res*res
    else:
        res = expo (a,((b-1)//2),c)
        res = res*res*a
    return (res%c)
