def calc(a,b):
    c = [0]
    res = []
    for i in range(len(a)):
        c.append(c[i] + a[i])
    for i in range(len(b)):
        res.append(c[b[i][1]+1] - c[b[i][0]])
    return res