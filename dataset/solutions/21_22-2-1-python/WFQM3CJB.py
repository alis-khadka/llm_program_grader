def calc(A,B):
    C = []
    s = ""
    for k in range(len(B)): #initializes Array with all 0 and length of B
        C.append(0)
    for i in A: #counts number of elements per category
        C[i] = C[i] + 1
    for j in range(len(B)): #creatings the output string
        if C[j] <= B[j]:
            s = s + "1"
        else:
            s = s + "0"
    return s