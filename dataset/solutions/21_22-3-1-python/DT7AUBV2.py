def opt(W):
    if len(W) < 2:
        return W[0]
    
    a = W[0]
    b = max(W[0],W[1])
    for i in range(2,len(W)):
        c = max(W[i]+a, b)
        a = b
        b = c
            
    return b