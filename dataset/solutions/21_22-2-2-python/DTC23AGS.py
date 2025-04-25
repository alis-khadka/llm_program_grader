def calc(a,b):
    part = [a[0]]
    res  = list()
    
    for i in range(1, len(a)):
        part.append(part[0]+a[i]) if i == 0 else part.append(part[i-1]+a[i])
    
    for i in range(len(a)):
        if (b[i][0] - 1) >= 0:
            res.append(part[b[i][1]] - part[b[i][0] - 1])
        else:
            res.append(part[b[i][1]])
                
    return res