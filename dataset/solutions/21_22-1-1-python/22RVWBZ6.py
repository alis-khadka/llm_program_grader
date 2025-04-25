def exp(n):
    if (n==1):
        return 2
    elif (n/2 % 2==0):
        j = exp(n/2)
        return j*j % 1000000007
    else:
        return exp(n-1)*2 % 1000000007

def calc(n):
    if (n==0):
        return 0
    return (exp(n)-1) % 1000000007