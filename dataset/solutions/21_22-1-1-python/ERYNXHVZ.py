def calc(n):
    a=2; b=n; c=1000000007
    return expo(a,b,c) -1

def expo(a,b,c):
    if b==0:
        return 1%c
    elif b%2:
        return (a * expo(a,b-1,c)) %c
    else:
        a = expo(a,b // 2,c) % c
        return (a*a)%c