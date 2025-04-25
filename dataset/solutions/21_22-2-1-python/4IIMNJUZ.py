def calc(A,B):
    output = ""
    counts = {}
    
    for i in range(len(A)):
        if A[i] not in counts:
            counts[A[i]] = 0
        counts[A[i]] += 1
    
    for i in range(len(B)):
        if i not in counts:
            counts[i] = 0
        output += "1" if counts[i] <= B[i] else "0"
    return output