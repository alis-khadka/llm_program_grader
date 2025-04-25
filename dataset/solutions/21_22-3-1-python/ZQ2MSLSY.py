def opt(W):
    A = []
    A.append(W[0])
    A.append(max(W[0],W[1]))
    for i in range (2,len(W)):
        A.append(max(W[i]+A[i-2],A[i-1]))
    return max(A)