def calc(A,B):
    C = []
    for i in range(1, len(A)):
        A[i] += A[i-1]
    for pair in B:
        if pair[0] > 0:
            C.append(A[pair[1]] - A[pair[0]-1])
        else:
            C.append(A[pair[1]])
    return C