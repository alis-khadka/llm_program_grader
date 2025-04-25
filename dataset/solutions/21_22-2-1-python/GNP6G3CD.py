def calc(A,B):
    array = [0] * len(B)
    string = ""
    for i in A:
        array[i] += 1
    for (i,comp) in enumerate(B):
        if array[i] > comp:
            string += "0"
        else:
            string += "1"
    return string