def exp(a,n):
    if(n == 0):
        return 1
    if(n%2 ==0):
        return  exp((a*a)% 1000000007,n//2)
    else:
        return (exp((a*a)% 1000000007,(n-1)//2) * a)
        
def calc(n):
    return (exp(2,n)-1)%1000000007