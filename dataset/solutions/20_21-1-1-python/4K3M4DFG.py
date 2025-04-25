def expo(a,b,c):
    if b%2 == 0:
        if b == 0:
            return 1
        else: 
            d = expo(a,b//2,c)
            return (d*d)%c
    else: 
        if b == 0:
            return 1
        else:    
            return (a*expo(a,b-1,c))%c