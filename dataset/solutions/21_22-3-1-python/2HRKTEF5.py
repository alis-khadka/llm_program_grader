def opt(W):
    P = [W[0], max(W[0], W[1])]
    for i in range(2, len(W)):
        P.append(max(P[i-2]+W[i],P[i-1]))
    return P[len(P)-1]