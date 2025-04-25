def Merge(A,l,p,r):
    x = p-l+1
    y = r-p
    L = [0] * (x+1)
    R = [0] * (y+1)
    for i in range(0,x):
        L[i] = A[l+i]
    for j in range(0,y):
        R[j] = A[p+j+1]
    L[x] = float('inf')
    R[y] = float('inf')
    i = 0
    j = 0
    for k in range(l,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1
    

def MergeSort(A,l,r):
    if l < r:
        p = ((r+l)//2)
        MergeSort(A,l,p)
        MergeSort(A,p+1,r)
        Merge(A,l,p,r)

def solution(A):
    MergeSort(A,0, len(A)-1)
    return A