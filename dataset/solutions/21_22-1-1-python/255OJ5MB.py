def calc(n):
    if (n < 1):
        return 0
    if (n == 1):
        return 1
    if (n % 2 == 0):
        u = (calc(n/2) + 1)
        return (u*u - 1) % 1000000007
    else: 
        return ((calc(n-1)+1)*2 -1) % 1000000007