def calc(f):
    n = 1
    while N > n:
        n = 2*n
    ceiling = n
    floor = n//2
    while N != ceiling:
        if N < ceiling:
            ceiling = (ceiling + floor)//2
        else:
            floor = ceiling
            ceiling = ceiling + floor//2
    return ceiling