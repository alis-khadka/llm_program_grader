def expo(a, b, c):
    result = 1
    while(b > 0):
        if(b % 2 == 0):
            a = a * a % c
            b /= 2
        else:
            result = result * a % c
            b -= 1
    return result