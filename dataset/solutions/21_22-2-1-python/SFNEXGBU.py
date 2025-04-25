def calc(A,B):
    output = ""
    for a in A:
        B[a] -= 1
    for b in B:
        output += "0" if b < 0 else "1"
    return output