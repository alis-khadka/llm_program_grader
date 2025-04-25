def calc(A,B):
    for i in range(len(A)-1):
        A[i+1] = A[i] + A[i+1]
    
    for i in range(len(B)):
        if B[i][0]==0:
            B[i] = A[B[i][1]]
        else:
            B[i] = A[B[i][1]] - A[B[i][0]-1]
    return B