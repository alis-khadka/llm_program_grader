def calc(A,B):
    for i in A:
        B[i] = B[i]-1
    output = ""
    for i in B:
        if i >= 0:
            output += "1"
        else:
            output += "0"
    return output