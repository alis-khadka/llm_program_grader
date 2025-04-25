def calc(A,B):
    c = []
    for i in range(len(B)):
        c.append(0)
    for i in range(len(A)):
        c[A[i]] += 1
    res = []
    for i in range(len(B)):
        res.append(0)
    for i in range(len(B)):
        if B[i] >= c[i]:
            res[i] = '1'
        else:
            res[i] = '0'
    return ''.join(res)