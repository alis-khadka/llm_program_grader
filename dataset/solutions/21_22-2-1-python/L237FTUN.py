def calc(A,B):
    C = [0] * len(B)
    for i in A:
        C[i] += 1
    s = ""
    for (i, cap) in enumerate(B):
        if C[i] > cap:
            s += "0"
        else:
            s += "1"
    return s