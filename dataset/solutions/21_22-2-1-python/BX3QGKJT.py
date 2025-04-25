def calc(A,B):
    c = [0]*len(B)
    for i in range(len(A)):
        c[A[i]] = c[A[i]] +1
    s = ""
    for j in range(len(B)):
        if c[j] <= B[j]:
            s = s + "1"
        else:
            s = s + "0"
    return s