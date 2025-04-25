def calc(A,B):
    sums = []
    s = 0
    for transporte in A:
        start_end = [s]
        s += transporte
        start_end.append(s)
        sums.append(start_end)
    return [sums[r][1]-sums[l][0] for l,r in B]