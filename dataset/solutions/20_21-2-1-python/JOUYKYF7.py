def calc(A, B):
    s = ""
    count = {}
    for i in A:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i in range(len(B)):
        try:
            if count[i] <= B[i]:
                s += "1"
            else:
                s += "0"
        except KeyError:
            s += "1"
    return s