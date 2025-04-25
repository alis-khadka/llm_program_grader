def calc(a,b):
    c = [a[0]]
    for i in range(1,len(a)):
        c.append(a[i]+c[i-1])
    L = []
    for i in range(0,len(b)):
        if b[i][0] == 0:
            L.append(c[b[i][1]])
        else:
            L.append(c[b[i][1]]-c[b[i][0]-1])
    return L