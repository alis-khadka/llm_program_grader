import random

def solution(A):
    random.shuffle(A)
    return mergeSort(A)
    
def mergeSort(A):
    size = len(A)
    if size > 1:
        split = size // 2
        B = mergeSort(A[0:split])
        C = mergeSort(A[split:size])
        return merge(B, C)
    else:
        return A

def merge(A, B):
    x = 0
    y = 0
    w = 0
    out = [0] * (len(A) + len(B))
    while x < len(A) and y < len(B):
        if A[x] < B[y]:
            out[w] = A[x]
            x += 1
        else:
            out[w] = B[y]
            y += 1
        w += 1
    if x < len(A):
        out[w:] = A[x:]
    if y < len(B):
        out[w:] = B[y:]
    return out