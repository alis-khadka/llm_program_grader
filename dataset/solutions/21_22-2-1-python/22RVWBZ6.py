def calc(A,B):
    res = []
    c = B.copy()
    for i in range(len(A)):
        c[A[i]] -= 1 
    for i in range(len(B)):
        if c[i] >= 0:
            res.append(str(1))
        else:
            res.append(str(0))
    return "".join(res)