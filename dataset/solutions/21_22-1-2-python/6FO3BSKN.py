def BinarySearch(l,r,f):
    m = (r-l)//2 + l
    if r == l:
        return l
    if f(m):
        return BinarySearch(l,m,f)
    if not f(m):
        return BinarySearch(m+1,r,f)

def calc(f):
    l = 1
    r = 1000000000000000000
    return BinarySearch(l,r,f)