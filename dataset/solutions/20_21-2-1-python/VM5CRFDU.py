def calc(A,B):
    n = len(A)
    m = len(B)
    s = ''
    C = [0]*m
    for i in range(n):
        C[A[i]] += 1
    for j in range(m):
        if C[j] <= B[j]:
            s += '1'
        else:
            s += '0'
    return s