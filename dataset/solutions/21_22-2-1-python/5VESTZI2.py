def calc(A,B):
    slist = []
    for i in range(len(A)):
        B[A[i]] -= 1
    for j in range(len(B)):
        if B[j] < 0:
            slist.append('0')
        else:
            slist.append('1')
    s = ''.join(slist)
    return s