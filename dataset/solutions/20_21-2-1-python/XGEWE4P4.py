def calc(A,B):
    r = ''
    for n in A:
        B[n] -= 1
    for m in B:
        r += '1' if m >= 0 else '0'
    return r