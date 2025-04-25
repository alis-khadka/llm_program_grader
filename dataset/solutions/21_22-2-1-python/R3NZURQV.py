def calc(A, B):
    C = []
    for i in range(10**6 + 1):
        C.append(0)
    for a in A:
        C[a] = C[a] + 1
    sol = ""
    for i in range(len(B)):
        if C[i] <= B[i]:
            sol += "1"
        else:
            sol += "0"
    return sol