def calc(A,B):
    for i in range(len(A)):
        B[A[i]]-=1
    s=[]
    for j in range(len(B)):
        if(B[j]<0):
            s.append('0')
        else:
            s.append('1')
    return "".join(s)