def calc(A,B):
    C = [0] * len(B)
    string = ''
    for a in A:
        C[a] += 1
    for i in range (0,len(B)):
        if B[i] >= C[i]:
            string+=str(1)
        else:
            string+=str(0)
    return string