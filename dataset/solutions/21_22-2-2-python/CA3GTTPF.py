def calc(a,b):
    c= []
    for i in range(1,len(a)):
        a[i]+=a[i-1]
    for pair in b:
        if pair[0]>0:
            c.append(a[pair[1]]-a[pair[0]-1])
        else:
            c.append(a[pair[1]])
    
    return c