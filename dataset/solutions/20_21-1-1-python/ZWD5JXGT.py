def expo(a,b,c):
    if b & 0b1 == 0b1:
        return (expo(a, b-1, c) * a) % c
    elif b == 0:
        return 1
    else:
        temp = expo(a, b // 2, c)
        return (temp * temp) % c
