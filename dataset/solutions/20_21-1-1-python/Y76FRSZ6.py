def expo(a,b,c):
    n = 1
    while b > 0:
        while b % 2 == 0:
            a = (a * a) % c
            b //= 2
        n = (n * a) % c
        b -= 1
    return n
