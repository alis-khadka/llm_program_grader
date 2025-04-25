def calc(n):
    res = 1
    basis = 2
    while(n > 0):
        if((n % 2) == 1):
            res = (res * basis) % 1000000007
        basis = (basis * basis) % 1000000007
        n //= 2
    return res -1