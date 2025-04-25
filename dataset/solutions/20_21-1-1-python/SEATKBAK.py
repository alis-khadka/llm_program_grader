def expo(a, b, c):
    res = 1
    a = a % c
    if (a == 0):
        return 0
    while (b > 0):
        if (b % 2) == 1:
            res = (res * a) % c
        b = b//2
        a = (a * a) % c
    return res