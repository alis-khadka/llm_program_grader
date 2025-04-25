def calc(f):
    def find(a, b):
        if a == b:
            return a
        p = (a+b) // 2
        if f(p):
            return find(a,p)
        else:
            return find(p+1, b)
    i = 1
    while not f(i):
        i *= 2
    return find(i//2, i)