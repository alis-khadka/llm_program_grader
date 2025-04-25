def calc(n):
    if n == 0:
        return 0
    z = 2
    odd = 1
    while n != 1:
        if n % 2 != 0:
            n = (n-1)//2 % 1000000007
            odd = odd*z % 1000000007
        else:
            n = n//2 % 1000000007
        z = z*z % 1000000007
    res = z * odd - 1 % 1000000007
    return res % 1000000007