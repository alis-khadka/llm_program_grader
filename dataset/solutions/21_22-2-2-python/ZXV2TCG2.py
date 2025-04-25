def calc(a,b):
    n = len(a)
    c=[]
    j=0
    k=0
    for i in range(0,n):
       k=k+a[i]
       c.append(k)
    d=[]
    for i in b:
        if i[0] == 0:
            j=c[i[1]]
        else:
            j=c[i[1]]-c[i[0]-1]
        d.append(j)
    return d