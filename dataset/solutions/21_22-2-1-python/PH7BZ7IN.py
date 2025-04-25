def calc(A,B):
    s = ""
    count = [0] * 4 * 10 **6
    for i in range(0, len(A)):
        count[A[i]] += 1
    for i in range(0, len(B)):
        if count[i] <= B[i]:
            s += str(1)
        else:
            s += str(0)
    return s