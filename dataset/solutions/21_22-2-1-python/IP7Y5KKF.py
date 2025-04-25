def calc(A, B):
    C = [0]*len(B)
    s = ""
    for i in A:
        C[i] += 1
    for i in range(len(B)):
        s = s + str(int(C[i] <= B[i]))
    return s
pass