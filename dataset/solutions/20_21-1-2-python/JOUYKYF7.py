import random


def solution(A):
    if len(A) < 2:
        return A

    s, e, g = [], [], []

    p = A[random.randint(0, len(A)-1)]

    for n in A:
        if n < p:
            s.append(n)
        elif n == p:
            e.append(n)
        else:
            g.append(n)

    return solution(s) + e + solution(g)