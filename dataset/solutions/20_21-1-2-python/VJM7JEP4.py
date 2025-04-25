def solution(A):
    return mergeSort(A, 0, len(A)-1)


def mergeSort(arr, l, r):
    if l < r:
        mid = (l + r-1) // 2

        mergeSort(arr, l, mid)
        mergeSort(arr, mid + 1, r)

        # merging
        tempL = arr[l:mid+1]
        tempR = arr[mid+1:r + 1]

        i = 0
        j = 0
        arrPos = l

        while i < len(tempL) and j < len(tempR):
            if tempL[i] < tempR[j]:
                arr[arrPos] = tempL[i]
                i = i + 1
            else:
                arr[arrPos] = tempR[j]
                j = j + 1
            arrPos = arrPos + 1

        # cleanup if i or j was bigger
        # if i is bigger
        for ix in range(len(tempL)-i):
            arr[arrPos] = tempL[i + ix]
            arrPos = arrPos + 1

        # if j is bigger
        for jx in range(len(tempR)-j):
            arr[arrPos] = tempR[j + jx]
            arrPos = arrPos + 1
    return arr