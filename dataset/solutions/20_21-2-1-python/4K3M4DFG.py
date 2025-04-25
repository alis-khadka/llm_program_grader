def calc(A,B):
    k = len(B)
    str = ""
    count = 0
    C = [0] * k
    for j in A:
        C[A[count]] += 1 # zählt, wie oft j in A vorkommt
        count += 1
    for i in range(0,k):
        if C[i] <= B[i]:
            str += "1"
        else:
            str += "0"
    return str