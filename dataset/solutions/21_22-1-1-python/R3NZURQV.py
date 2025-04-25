def calc(n):
    a = 1
    b = 2
    while n > 0:
        if n % 2 == 1:
            a = (a * b) % 1000000007
        b = (b * b) % 1000000007
        n //= 2
    return (a - 1) % 1000000007