def expo(a,b,c):

    x = 1

    while (b > 0):

        if (b % 2 == 1):

            x = (x * a) % c

        a = (a * a) % c
        b = b // 2

    return x % c
