def calc(n):
    if n == 0:
        return 0
    else:
        fix = 1
        if n % 2 == 1:
            n -= 1
            fix = 2
        res = calc(int(n)//2) + 1 % 1000000007
        return ( res*res*fix - 1 ) % 1000000007