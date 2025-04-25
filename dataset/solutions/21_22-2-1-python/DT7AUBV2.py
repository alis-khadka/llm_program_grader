def calc(A,B):
    C = [0] * len(B)
    for i in range(len(A)):
        C[A[i]] += 1
    
    s = ""
    for i in range(len(B)):
        if C[i] <= B[i]:
            s += "1"
        else:
            s += "0"
    
    return s