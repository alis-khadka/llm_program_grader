def solution(A):
    if len(A) < 2:
        return A
        
    mid = len(A) // 2
    left = solution(A[:mid])
    right = solution(A[mid:])
    
    return merge(left, right)
    
def merge(left, right):
    
    res = []
    aptr = 0
    bptr = 0
    while aptr < len(left) and bptr < len(right):
        if left[aptr] < right[bptr]:
            res.append(left[aptr])
            aptr += 1
        else:
            res.append(right[bptr])
            bptr += 1
    res += left[aptr:]
    res += right[bptr:]
    return res