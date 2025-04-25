def calc(A, B):
    outputStr = ""
    C = [0 for i in range(len(B))]

    for c in range(len(A)):
        C[A[c]] = C[A[c]] + 1

    for i in range(len(B)):
        
        if C[i] > B[i]:
            outputStr = outputStr + str(0)
        else:
            outputStr = outputStr + str(1)

    return outputStr