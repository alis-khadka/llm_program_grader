def exp(a,b,c):
    if b == 0:
        return 1 % c
    elif b % 2 == 1:
        return ((exp(a, b-1,c) % c) * (a % c)) % c
    else:
        x = (exp(a, b // 2,c) % c)
        return (x * x) % c

def expo(a,b,c):
    return exp(a,b,c) % c