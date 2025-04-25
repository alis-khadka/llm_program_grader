def expo(a, b, c):
    if b == 0:
        return 1
    if b == 1:
        return a % c
    if b == 2:
        return (a*a) % c

    if b % 2 == 0:  # even
        res = expo(a, b // 2, c)
        return (res * res) % c
    else:  # uneven
        return (expo(a, b-1, c) * a) % c
