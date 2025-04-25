def calc(A,B):
    C=[]
    for i in range(0,len(B)):
        C.append(0)
    for i in range(0,len(A)):
        C[A[i]] = C[A[i]] + 1
    s =""
    for i in range(0,len(B)):
        if C[i] <= B[i]:
            s = s+"1"
        else:
            s = s+"0"
    return s
    pass