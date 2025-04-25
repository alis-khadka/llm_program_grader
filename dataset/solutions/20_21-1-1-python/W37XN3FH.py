def expo(a,b,c):
    if b % 2 == 0:
        if b == 0:
            return 1
        x = expo(a,b/2,c)
        return x * x % c
    elif b % 2 == 1:
        return expo(a, b-1, c) * a % c