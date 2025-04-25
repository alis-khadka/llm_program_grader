def calc(n):
    if n == 0:
        return 0
    else:
        if n%2 == 0:
            n = (n//2)%1000000007
            res = (calc(n))%1000000007
            res = (res+1)%1000000007
            res = (res*res)%1000000007
            return (res-1)%1000000007
        else:
            n = (n-1)%1000000007
            res = calc(n)%1000000007
            res = (res*2)%1000000007
            return res+1