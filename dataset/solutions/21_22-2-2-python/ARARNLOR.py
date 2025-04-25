def calc(a,b):
    n = len(a)
    result = [0 for _ in range(len(b))]
    accumulated = [0 for _ in range(n)]
    accumulated[0] = a[0]
    for i in range (1, n):
        accumulated[i] = accumulated[i-1] + a[i]
    
    for i in range(len(b)):
        if b[i][0] == 0:
            result[i] = accumulated[b[i][1]]
        else:
            result[i] = accumulated[b[i][1]] - accumulated[b[i][0] - 1]
    return result