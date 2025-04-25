def expo(a,b,c):
    if c == 1:
        return 0
    result = 1
    a = a%c
    while b > 0:
        if b%2 == 1:
            result = (result * a) % c 
        b = b >> 1
        a = (a*a) %c
    return result
