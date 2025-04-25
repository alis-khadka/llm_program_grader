def calc(f,l=1,r=1000000000000000000):
    
    if l==r:
        return l
    m=(r+l)//2
    
    if f(m)==1:
        return calc(f,l,m)
    else:
        return calc(f,m+1,r)