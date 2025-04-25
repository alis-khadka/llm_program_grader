def calc(n):
    if n==0:
        return 0
    x=expo(2,n)
    return x-1
def expo(b,n):
    if n==1:
        return b
    if n%2==0:
        a=expo(b,n//2)
        a=(a*a)%1000000007
        return a
    a=expo(b,(n-1)//2)
    a=(a*a*b)%1000000007
    return a