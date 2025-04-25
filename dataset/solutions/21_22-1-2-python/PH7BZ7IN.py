def calc(f):
    n=1
    while(f(n)) == 0:
        n = n*2
    l = n//2
    r = n
    while(l<=r):
        m = (l+r)//2
        if(f(m) > 0 and (m == l or f(m -1)<=0)):
            return m
            
        if(f(m)<=0):
            l = m+1
        else:
            r = m-1