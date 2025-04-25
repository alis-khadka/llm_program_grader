def calc(a,b):
    c = a.copy()
    liste = [0] * len(a)
    
    for i in range(1, len(a)):
        c[i] = a[i]+c[i-1]
        
    for i in range(0, len(a)):
        if b[i][0]>=1:
            liste[i]=c[b[i][1]]-c[b[i][0]-1]
        else:
            liste[i]=c[b[i][1]]
    return liste