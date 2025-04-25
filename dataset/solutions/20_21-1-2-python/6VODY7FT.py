import math

def solution(array):
    if len(array) > 1:
        p = len(array) // 2
        left = solution(array[:p])
        right = solution(array[p:])
        array = merge(left, right)
    return array


def merge(left, right):
    array = []
    left.append(math.inf)
    right.append(math.inf)
    i = 0
    j = 0
    for k in range(len(left)-1 + len(right)-1):
        if left[i] <= right[j]:
            array.append(left[i])
            i += 1
        else:
            array.append(right[j])
            j += 1
    return array