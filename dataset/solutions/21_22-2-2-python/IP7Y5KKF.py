def calc(A,B):
    C = [0]*len(B)
    S = [0]*len(B)
    S[0] = A[0]
    for s in range(len(B)-1):
        S[s+1] = S[s]+A[s+1] 
    for i in range(len(B)):
        if B[i][0] == 0:
            C[i] = S[B[i][1]]
        else:
            C[i] = S[B[i][1]]-S[B[i][0]-1]
    #print(C)
    return C
pass