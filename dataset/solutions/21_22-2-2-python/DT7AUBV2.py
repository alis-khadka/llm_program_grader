def calc(A,B):
    S = [0] * len(A)
    if len(A) >= 1:
        S[0] = A[0]
    for i in range(1, len(A)):
        S[i] = S[i-1] + A[i]
        
    C = [0] * len(A)
    for i in range(len(B)):
        l, r = B[i]
        C[i] = S[r]
        if l >= 1:
            C[i] -= S[l-1]
        
    return C