def calc(A,B):
    C = [0]*len(B)
    s = list()
    for i in range(len(A)):
        C[A[i]] += 1
    for ii in range(len(B)):
        if C[ii] <= B[ii]:
                s.append('1')
        else: 
            s.append('0')
    s = ''.join(s)
    return s