def knapSack(vol, gew, W):
    n = len(vol)
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif gew[i-1] <= w:
                K[i][w] = max(vol[i-1]
                          + K[i-1][w-gew[i-1]],  
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]