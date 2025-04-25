def merge(B,C):
    A=[]
    bN = len(B)
    cN = len(C)
    B.append(float('inf'))
    C.append(float('inf'))
    bI = 0
    cI = 0
    while(bI<bN or cI<cN):
        if B[bI]<=C[cI]:
            A.append(B[bI])
            bI+=1
        else:
            A.append(C[cI])
            cI+=1
    
    return A


def solution(A):
    n = len(A)//2
    if(len(A)==1):
        return A
    else:
        return merge(solution(A[:n]),solution(A[n:]))