def calc(A, B):
    h = [0] * len(B)
    output = ""
    for n in range(len(A)):
        h[A[n]] += 1
    for i in range(len(B)):
        if h[i] <= B[i]:
            output = output + "1"
        else:
            output = output + "0"
    return output