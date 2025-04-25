def opt(W):
    res = [W[0], max(W[0], W[1]), 0]
    for i in range(2, len(W)):
        res[i%len(res)] = max(res[(i-1)%len(res)], res[(i-2)%len(res)]+W[i])
    
    return max(res)