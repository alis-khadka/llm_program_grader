def calc(a,b):
    C = [0 for _ in range(len(a))]
    R = [0 for _ in range(len(a))]
    C[0] = a[0]
    for i in range(1, len(a)):
       
        C[i] = a[i] + C[i-1]
    
 
    for i in range(len(a)):
        l,r = b[i]
       
        if l == 0:
            m=0
        else:
            m = C[l-1]
        R[i] = C[r] - m
    return R