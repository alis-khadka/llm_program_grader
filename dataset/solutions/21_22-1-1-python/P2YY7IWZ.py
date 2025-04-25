def calc(n):
    b = 2
    m = 1000000007
    r = 1
    b = b % m
    while n > 0:
        if n % 2 == 1:
            r = (r * b) % m    
        b = b * b % m
        n = n//2
    return r-1