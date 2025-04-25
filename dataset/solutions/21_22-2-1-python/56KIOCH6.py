def calc(A,B):
    for a in A:
        B[a] = B[a] - 1
    s = ''
    for b in B:
        if b < 0:
            s = s + '0'
        else:
            s = s + '1'
    return s