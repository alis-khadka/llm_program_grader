def calc(n):
    return potenziere(n)-1
    
def potenziere(n):
    if n == 0:
        return 1
    if n%2==0:
        k = n//2
        a=potenziere(k)
        return a*a%1000000007
    else:
        return 2*potenziere(n-1)%1000000007