def calc(a,b):
    m = len(a)
    h = [0]*m
    h[0] = a[0]
    for i in range(1,m):
        h[i] = h[i-1] + a[i]
    n = len(b) 
    x = [0]*n
    for j in range(n):
        if b[j][0] == 0:
            x[j] = h[b[j][1]]
        else:
            x[j] = h[b[j][1]] - h[b[j][0] - 1]
    return x