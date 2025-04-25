def expo(a,b,c):
    
    res = 1
    
    if b > 1:
        if b%2 == 0:
            p = expo(a,b//2,c)
            res = p * p
        
        else:
            res = a * expo(a,b-1,c)
            
    elif b == 1:
        res = a
        
    return res%c