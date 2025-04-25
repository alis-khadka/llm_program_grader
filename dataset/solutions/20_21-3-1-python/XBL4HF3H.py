def knapSack(value, volume, capacity):
    assert len(value) == len(volume)
    for x in volume:
        assert x == round(x)
    
    n = len(value) + 1
    W = capacity + 1
    if(W < 1): return 0
    A = [[0] * (W) for i in range(n)]

    for i in range(1, n):
        for w in range(1, W):
            if(volume[i - 1] > w):
                A[i][w] = A[i - 1][w]
            else:
                a = A[i - 1][w]
                b = value[i - 1] + A[i - 1][w - volume[i - 1]]
                A[i][w] = max(a, b)        

    return A[n - 1][W - 1]