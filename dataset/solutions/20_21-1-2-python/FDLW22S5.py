def solution(A):
    return mergeSort(A)
    
def mergeSort(A):
    if len(A) > 1:
 
        piv = len(A)//2
 
        L = A[:piv]
        R = A[piv:]
 
        mergeSort(L)
        mergeSort(R)
 
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i = i + 1
            else:
                A[k] = R[j]
                j = j + 1
            k = k + 1
 
        while i < len(L):
            A[k] = L[i]
            i = i + 1
            k = k + 1
 
        while j < len(R):
            A[k] = R[j]
            j = j + 1
            k = k + 1

    return A