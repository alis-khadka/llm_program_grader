def calc(n):
    return submethod(n)-1
    
def submethod(b):
    if b == 0:
        return 1 % 1000000007
    elif b % 2:
        return (2*submethod(b-1) % 1000000007)
    else:
        temp = submethod(b //2) % 1000000007
        return (temp*temp) % 1000000007