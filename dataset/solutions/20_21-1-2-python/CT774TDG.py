import random

def top_down_merge(a: list, begin: int, middle: int, end: int, b: list) -> None:
    i, j = begin, middle

    for k in range(begin, end):
        if (i < middle and (j >= end or a[i] <= a[j])):
            b[k] = a[i]
            i = i + 1
        else:
            b[k] = a[j]
            j = j + 1


def top_down_split_merge(b: list, begin: int, end: int, a: list) -> None:
    if (end - begin <= 1):
        return
    else:
        middle = (end + begin) // 2
        top_down_split_merge(a, begin, middle, b)
        top_down_split_merge(a, middle, end, b)
        top_down_merge(b, begin, middle, end, a)


def _solution(a: list, b: list, n) -> list:
    random.shuffle(a)
    b = a.copy()
    top_down_split_merge(b, 0, n, a)
    return a


def solution(a: list) -> list:
    return _solution(a, [], len(a))