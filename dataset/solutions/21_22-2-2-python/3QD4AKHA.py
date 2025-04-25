def calc(A,B):
    for i in range(1,len(A)):
        A[i]=A[i]+A[i-1]
    rB = list(B)
    for b in range(0,len(rB)):
        if rB[b][0] == 0:
            rB[b] = A[rB[b][1]]
        else:
            rB[b] = A[rB[b][1]]-A[rB[b][0]-1]
          
    return rB