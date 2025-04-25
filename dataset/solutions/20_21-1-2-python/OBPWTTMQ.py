def merges(A,l,r):
    if l < r:
        p = (l + r) // 2
        merges(A,l,p)
        merges(A,p+1,r)
        merge(A,l,p,r)

def merge(A,l,p,r):
    n1 = p - l + 1
    n2 = r - p
    L = list()
    R = list()
    for i in range(n1):
        L.append(A[l+i])
    for i in range(n2):
        R.append(A[p+i+1])
    L.append(10**7) # da A[i] <= 10**6
    R.append(10**7) # da A[i] <= 10**6
    i = 0
    j = 0
    for k in range(l,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def solution(A):
    merges(A,0,len(A)-1)
    return A