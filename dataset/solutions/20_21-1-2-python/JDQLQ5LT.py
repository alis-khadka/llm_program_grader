def solution(A):
    i = 0
    j = 0
    if len(A) <= 1:
        return A
    newA=[]
    mid = int(len(A)/2)
    left = solution(A[:mid])
    right = solution(A[mid:])
    while(len(left) > i) and (len(right) > j):
        if left[i] > right[j]:
            newA.append(right[j])
            j += 1
        else:
            newA.append(left[i])
            i += 1
    newA += left[i:]
    newA += right[j:]
        
    return newA