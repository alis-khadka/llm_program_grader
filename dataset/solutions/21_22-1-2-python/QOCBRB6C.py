def calc(f):
    
    l = 0 
    r = 1
    m = (l+r)//2
    
    while f(m) != 1:
        r = 2 * r
        m = (l+r)//2


    while l != r:


        if f(m) == 0:
            if l == m:
                m += 1
            l = m
            m = (l+r)//2
        else:
            r = m 
            m = (l+r)//2
            

    
    return m