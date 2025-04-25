def expo(a,b,c):
    if not b:
        return 1
    elif b == 1:
        return a % c
    elif b % 2 == 0:
        res = expo(a, (b // 2),c)
        return (res * res) % c
    else:
        return (expo(a, b-1, c) * a) % c
