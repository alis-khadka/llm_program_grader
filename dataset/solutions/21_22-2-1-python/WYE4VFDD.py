def calc(A,B):
    for a in A:
        B[a] -= 1
    return ''.join([str(int(b>=0)) for b in B])