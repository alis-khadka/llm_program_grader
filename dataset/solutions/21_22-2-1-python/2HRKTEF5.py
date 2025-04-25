def calc(A,B):
    output = ""
    C = []
    C = [0 for i in range(len(B))]
    for i in A: C[i] +=1
    for i in range(len(B)):
        if C[i] <= B[i]:
            output = output + "1"
        else:
            output = output + "0"
    return output