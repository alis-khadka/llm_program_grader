def calc(A,B):
    for i in range(0, len(A)):
        B[A[i]] -= 1 
    s = ""
    
    for i in range(0, len(B)):
        if B[i] < 0:
            s += "0"
        else:
            s += "1"
    return s