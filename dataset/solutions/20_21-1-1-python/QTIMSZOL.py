def expo(a, b, c):
    summe = 1
    while b != 0:
        if b % 2 == 1:
            summe = (summe * a) % c
        b = b // 2
        a = (a * a) % c
    return summe 
