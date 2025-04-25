def calc(A,B):
    n=len(A)
    m=len(B)
    s=''
    C=[]
    for i in range(0,m):
        C.append(0)
    for i in A:
        C[i]=C[i]+1
    for i in range(0,m):
        if B[i]<C[i]:
            s=s+'0'
        else:
            s=s+'1'
    return s