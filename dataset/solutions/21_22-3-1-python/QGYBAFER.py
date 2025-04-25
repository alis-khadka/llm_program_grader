def opt(W):
    w = W.copy()
    g = [0] * len(W)
    g[0] = w[0]
    g[1] = max(w[0],w[1])
    for i in range(2,len(w)):
        g[i] = max(g[i-1],g[i-2]+w[i])
    return g[len(w)-1]