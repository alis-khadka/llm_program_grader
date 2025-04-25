def expo(a, b, c):
    res = 1
    halter = a
    while b > 0:
        if b % 2 == 1:
            res = (res * halter) % c
        halter = (halter * halter) % c
        b = b // 2
    return res % c
