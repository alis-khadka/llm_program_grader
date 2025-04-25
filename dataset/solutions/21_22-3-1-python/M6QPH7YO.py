def opt(W):
    D = []
    for i in range(0, len(W)):
        if i == 0:
            D.append(W[i])
        elif i == 1:
            D.append(max(W[i], W[i-1]))
        else:
            if D[i-1] == D[i-2]:
                D.append(D[i-1]+W[i])
            else:
                D.append(max(D[i-2]+W[i], D[i-1]))
    return D[len(W)-1]