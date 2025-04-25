def calc(a,b):
    rAr = []
    rBr= []
    newValue = 0
    alen = len(a)-1
    for i in range(0, alen+1):
        newValue = newValue+ a[i]
        rAr.append(newValue)
    
    for interval in b:
        value = 0
        if(interval[0]==0):
            value = rAr[interval[1]]
        else:
            value = rAr[interval[1]] - rAr[interval[0]-1]
        rBr.append(value)
    return rBr