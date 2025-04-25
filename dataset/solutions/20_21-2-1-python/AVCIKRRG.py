def calc(A,B):
    c = {}
    for i in A:
        if i not in c:
            c[i] = 0
        c[i] += 1
    s = ""
    for i in range(len(B)):
        if i not in c:
            c[i] = 0
        if c[i] <= B[i]:
            s += "1"
        else:
            s += "0"
    return s