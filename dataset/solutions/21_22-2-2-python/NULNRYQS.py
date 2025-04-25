def calc(A: list, B: list):
    sums = [A[0]]
    for i in range(1,len(A)):
        sums.append(sums[i-1]+A[i])
        
    out = list()
    for t in B:
        if t[0] > 0:
            out.append(sums[t[1]] - sums[t[0] - 1])
        else:
            out.append(sums[t[1]])
            
    return out