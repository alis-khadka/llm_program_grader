def Merge(l, r, A):
    
    l.append(10**6)
    r.append(10**6)
    
    i=0
    j=0
    
    for k in range(len(A)):
        if l[i] <= r[j]:
            A[k]=l[i]
            i+=1
        else:
            A[k]=r[j]
            j+=1

def solution(A):
    
    if len(A)>1:
        mid=len(A)//2
        L=A[:mid]
        R=A[mid:]
        
        solution(L)
        solution(R)
        Merge(L, R, A)
    return(A)