def calc(A,B):
    C=""
    for i in range(len(A)):
        B[A[i]]=B[A[i]]-1
    for i in range(len(B)):
        if B[i]>=0:
            C=C+"1"
        else:
            C=C+"0"
    return C