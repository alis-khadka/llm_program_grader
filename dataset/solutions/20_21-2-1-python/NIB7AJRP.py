def calc(A,B):
    C = [0] * len(B)
    for x in range(0, len(A)):
        C[A[x]] += 1
    str = ""
    for x in range(0, len(B)):
        if C[x] > B[x]:
            str += "0"
        else:
            str += "1"
    return str