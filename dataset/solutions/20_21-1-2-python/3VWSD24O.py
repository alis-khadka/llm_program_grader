def solution(A):
    
    if len(A) <= 1:
        return A
        
    p = len(A) // 2
    A_l = solution(A[:p])
    A_r = solution(A[p:])
    B = merge(A_l, A_r)
    return B


def merge(A_l, A_r):
    
    
    n = len(A_l) + len(A_r)
    
    B = [None] * n
    
    A_l.append(10**7)
    A_r.append(10**7)
    
    i = 0
    j = 0
    for k in range(0,n):
        if A_l[i] <= A_r[j]:
            B[k] = A_l[i]
            i += 1
        
        else:
            B[k] = A_r[j]
            j += 1
            
    return B