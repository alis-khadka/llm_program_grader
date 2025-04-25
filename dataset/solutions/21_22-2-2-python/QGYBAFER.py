def calc(a,b):
    s = [0] * len(b)
    c = [0] * len(a)
    c[0] = a[0]
    for i in range(1,len(a)):
        c[i] = a[i] + c[i-1]
    for i in range(len(b)):
        l = ((b[i])[0])
        r = ((b[i])[1])
        if l == r:
            s[i] = a[l]
        elif l == 0:
            s[i] = c[r]
        else:
            s[i] = c[r] - c[l-1]
    return s