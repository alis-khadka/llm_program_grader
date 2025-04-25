def calc(A,B):
    s = ''
    n = max(max(A) + 1, len(B))
    C = [0]*n
    for j in range(0,len(A)):
        C[A[j]] += 1
    for j in range(len(B)):
        if C[j] <= B[j]:
            s += '1'
        else:
            s += '0'
    return s