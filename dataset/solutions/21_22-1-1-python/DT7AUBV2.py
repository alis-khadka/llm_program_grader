def calc(n):
    x = (pow2(n)-1) % 1000000007
    return x
    
def pow2(n):
    if n == 0:
        return 1
    
    if n % 2 == 0:
        x = pow2(n//2)
        x = x * x % 1000000007
        return x
    
    x = pow2(n-1)
    x = (x << 1) % 1000000007
    return x