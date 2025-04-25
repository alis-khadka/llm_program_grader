def calc(A,B):
    output = ""
    for val in A:
        B[val] = B[val] - 1
    for item in B:
        if item >= 0:
            output += "1"
        else:
            output += "0"
    return output