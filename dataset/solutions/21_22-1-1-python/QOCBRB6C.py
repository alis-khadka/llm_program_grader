def calc(n):
    
    if n == 0:
        return 0
        
    elif n%2 == 0:
        a = calc(n//2) + 1
        
        return ((a * a) - 1)%1000000007
    elif n%2 == 1:
        a = calc(n-1) + 1
        return (2 * a - 1)%1000000007
    
    pass