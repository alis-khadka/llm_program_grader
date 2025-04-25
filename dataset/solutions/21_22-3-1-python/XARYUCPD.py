def opt(W):
    M = [0]*len(W)
    for i in range(len(W)):
        if i < 2: M[i] = W[i]
        elif i == 2: M[i] = M[0] + W[2] 
        else: M[i] = max(M[i-2], M[i-3]) + W[i]
    return max(M)