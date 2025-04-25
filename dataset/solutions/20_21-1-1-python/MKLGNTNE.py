def expo(a,b,c):
    if b == 0:
        return 1
    if b == 1:
        return a

    if b % 2 == 0:
        result = expo(a, b/2, c)
        return (result * result) % c
    else:
        return (expo(a, b - 1, c) * a) % c;

    pass
