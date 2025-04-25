def calc(a,b):
    c = [0 for i in range(len(a) + 1)]
    val = 0
    for i in range(len(a)):
        val += a[i]
        c[i] = val
    result = [0 for i in range(len(b))]

    for i in range(len(b)):
        l, r = b[i]
        
        res = c[r] - c[l - 1]
        
        result[i] = res
    
    return result