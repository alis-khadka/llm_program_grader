def solution(A):
    i = 0 
    k = 0 
    if len(A) <=1:
        return A
    sA = []
    mid = int(len(A)/2)
    a1 = solution(A[:mid])
    a2 = solution(A[mid:])
    while (len(a1) > i) and (len(a2) > k):
        if a1[i] > a2[k]:
            sA.append(a2[k])
            k += 1
        else: 
            sA.append(a1[i])
            i += 1
    sA += a1[i:]
    sA += a2[k:]
    
    return sA