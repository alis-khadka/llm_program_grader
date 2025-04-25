def solution(A):
    MergeSort(A,0,len(A)-1)
    return A


def MergeSort(A,l,r):
    if l<r:
        p = (l+r) // 2
        MergeSort(A,l,p)
        MergeSort(A,p+1,r)
        Merge(A,l,p,r)
    return

    
def Merge(A,l,p,r):
    L = A[l:p+1]
    R = A[p+1:r+1]
    L.append(float('inf'))
    R.append(float('inf'))
    i = j = 0
    for k in range(l,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return