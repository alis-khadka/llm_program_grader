def calc(A,B):
    
    a = ""
    
    C = {}
    for i in range(len(B)):
        C[i] = 0

    for i in A:
        C[i] += 1


    for i in range(len(B)):
        if C[i] <= B[i]:
            a += "1"
        else:
            a += "0"
    
    return a
    
    pass