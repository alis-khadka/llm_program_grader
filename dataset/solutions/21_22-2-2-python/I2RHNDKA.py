def calc(a,b):
    k=1
    c=b
    for i in range(len(b)):
        while k <= b[i][1]:
            a[k]=a[k]+a[k-1]
            k=k+1
        if b[i][0]>0:
            c[i]=a[b[i][1]]-a[b[i][0]-1]
        else:
            c[i]=a[b[i][1]]
    return c