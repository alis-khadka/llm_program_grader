def calc(A, B):
    length = len(B)
    C = [0 for _ in range(length)]
    s = ""
    for i in range(len(A)):
        C[A[i]] = C[A[i]] + 1

    for i in range(length):
        if B[i] >= C[i]:
            s += "1"
        else:
            s += "0"
    return s