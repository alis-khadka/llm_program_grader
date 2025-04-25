def calc(f):
    return binSearch(0, 10**18, f)
    
def binSearch(l, r, f):
    m = (l + r) // 2
    if f(m) == 1:
        if(f(m - 1) == 0):
            return m
        return binSearch(l, m - 1, f)
    return binSearch(m + 1, r, f)