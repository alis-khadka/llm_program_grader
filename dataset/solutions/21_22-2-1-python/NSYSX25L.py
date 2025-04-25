def calc(A,B):
    C = []
    i = 0
    while i < len(B):
        C.append(0)
        i += 1
    D = ""
    i = 0
    while i < len(A):
        C[A[i]] += 1
        i += 1
    i = 0
    while i < len(B):
        if B[i] >= C[i]:
            D += "1"
        else:
            D += "0"
        i += 1
    return D