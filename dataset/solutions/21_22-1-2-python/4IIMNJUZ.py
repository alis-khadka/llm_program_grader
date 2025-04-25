def calc(f):
    l = 0
    r = (10**18)+1
    
    while (l<r):
        m = (l+r) // 2
        if f(m) == 1:
            if f(m-1) == 0:
                return int(m)
            r = m - 1
        else:
            l = m + 1
    return int(l)