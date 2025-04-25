def calc(n):
    return (hoch(2,n) - 1) % 1000000007
    
def hoch(a,b):
    if b == 0:   
        return 1
    if b == 1:
        return a
    if (b % 2) == 0:
        zwi = hoch(a,b//2)
        return (zwi*zwi) % 1000000007
    else:
        return (hoch(a,b - 1)* a) % 1000000007