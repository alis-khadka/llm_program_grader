def calc(f):
    l = 0
    r = 1000000000000000000
    m = (r + l)//2
    
    while(0<=l & l<=r):
        m = ((r+l)//2)
        
        if(f(m) != 0):
            r = m - 1
        else:
            l = m + 1
            
    if(f(m)!= 0):
        return m
    else:
        return m + 1