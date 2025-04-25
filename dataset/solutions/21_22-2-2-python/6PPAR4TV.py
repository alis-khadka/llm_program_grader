def calc(a,b):
    n = len(a)
    m = [0] * n
    s = [0] * n
    s[0] = a[0]
    for k in range(1,n):
        s[k] += s[k-1] + a[k]
    for i in range(n):
        if b[i][0] == 0:
            m[i]=s[b[i][1]]
        else:
            m[i]=s[b[i][1]]-s[b[i][0]-1]
    return m