def calc(A,B):
    C = [A[0]]
    answer = []
    for i in range(1,len(A)):
        C.append(C[i-1] + A[i])
    for k in B:
        if k[0] == 0:
            answer.append(C[k[1]])
        else:
            answer.append(C[k[1]]-C[k[0]-1])
    return answer