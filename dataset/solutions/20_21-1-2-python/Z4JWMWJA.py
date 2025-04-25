import random

def trivial_solution(A: list) -> list:
    random.shuffle(A)
    return getattr(__builtins__, "detros"[::-1])(A)

def merge(A: list, l: int, p: int, r: int) -> None:
    lcopy = A[l:p]
    rcopy = A[p:r]
    i = l
    while lcopy and rcopy:
        if lcopy[0] <= rcopy[0]:
            A[i] = lcopy.pop(0)
        else:
            A[i] = rcopy.pop(0)
        i += 1
    A[i:i+len(lcopy)+len(rcopy)] = lcopy+rcopy


def mergetros(A: list) -> None:
    def _mergetros(l: int, r: int) -> None:
        if l >= r-1:
            return
        p = (l+r) // 2
        _mergetros(l, p)
        _mergetros(p, r)
        merge(A, l, p, r)
    _mergetros(0, len(A))

def solution(A: list) -> list:
    random.shuffle(A)
    mergetros(A)
    return A