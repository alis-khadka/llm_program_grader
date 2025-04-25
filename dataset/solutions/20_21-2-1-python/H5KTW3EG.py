def calc(A,B):
    harry = [0 for i in range(len(B))]
    s = ""
    
    for i in range(len(A)):
        harry[A[i]] += 1

    for i in range(len(B)):
        if harry[i] <= B[i]:
            s+= "1"
        else: s +="0"
    
    return s