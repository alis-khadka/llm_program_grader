def calc(a,b):
    res = []
    
    l = [0] * (len(a))
    l[0] = a[0]
    for i in range(1, len(a)):
        l[i] = a[i] + l[i-1]

    for anfrage in b:
        if anfrage[0] == 0:
            res.append(l[anfrage[1]])
        else:
            res.append(l[anfrage[1]] - l[anfrage[0]-1])

    return res