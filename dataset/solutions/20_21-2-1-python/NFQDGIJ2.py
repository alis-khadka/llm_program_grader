def calc(A,B):
    C = [0] * (10**6+1)
    for i in range(0,len(A)):
        C[A[i]] += 1
    S = str()
    for j in range(0,len(B)):
        if C[j] <= B[j]:
            S += '1'
        else:
            S += '0'
    return S