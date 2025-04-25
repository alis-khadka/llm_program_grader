def solution(A):
    return merge_Sort(A, 0, len(A) - 1)

def merge_Sort(array, left, right):
    if left == right:
        return [array[left]]
    middle = (left + right) // 2
    a = merge_Sort(array, left, middle)
    b = merge_Sort(array, middle + 1, right)
    return merge(a, b)

def merge(a, b):
    res = list()
    while len(a) > 0 or len(b) > 0:
        if len(b) == 0 or (len(a) > 0 and a[0] < b[0]):
            res.append(a.pop(0))
        else:
            res.append(b.pop(0))
    return res