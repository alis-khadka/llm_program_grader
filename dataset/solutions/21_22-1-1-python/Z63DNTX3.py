def calc(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        result = (calc(n/2)) % 1000000007
        result = result*result+2*result
        return result % 1000000007
    else:
        return ((calc(n-1)*2+1)% 1000000007)% 1000000007