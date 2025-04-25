import math

def solution(A):
    if len(A) == 1:
        return A
    
    arrA = solution(A[0:-len(A)//2])
    arrB = solution(A[(len(A)//2):len(A)])
    
    if not arrA:
        arrA = []
    if not arrB:
        arrB = []
    
    return merge(arrA, arrB)


def merge(A, B):
    c = []
    iA = 0
    iB = 0
    A.append(math.inf)
    B.append(math.inf)
    for i in range((len(A)+len(B))-2):
        if A[iA] <= B[iB]:
            c.append(A[iA])
            iA += 1
        else:
            c.append(B[iB])
            iB += 1
    return c