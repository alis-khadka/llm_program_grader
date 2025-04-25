def solution(A):
    if len(A) < 2:
        return A

    mitte = len(A) // 2     
    left_A = solution(A[:mitte])
    right_A = solution(A[mitte:])

    return merge(left_A, right_A)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result