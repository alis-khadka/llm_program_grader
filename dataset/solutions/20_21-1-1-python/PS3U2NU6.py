def expo(a,b,c):
    number = 1
    while b:
        if b & 1:
            number = number * a % c
        b >>= 1
        a = a * a % c
    return number