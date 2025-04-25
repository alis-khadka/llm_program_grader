import math

def solution(A):
    r = len(A)
    if 1 < r :
        p = math.floor((r)/2)
        A1 = A[0:p]
        A2 = A[p:r]
        A1 = solution(A1)
        A2 = solution(A2)
        A = A1 + A2
        merge(A,p,r)
    return A
def merge(A,p,r):
    n1 = p 
    n2 = r - p 
    L = list()
    R = list()
    for i in range(0, n1):
        L.append(A[i])
    for j in range(0,n2):
        R.append(A[p + j])
    L.append(3000000)
    R.append(3000000)
    i = 0; j = 0
    for  k in range(0,r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    return A