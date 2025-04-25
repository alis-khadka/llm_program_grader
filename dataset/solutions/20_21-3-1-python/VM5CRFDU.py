def knapSack(value, volume, capacity):
    assert len(value) == len(volume)
    for x in volume:
        assert x == round(x)

    n = len(value)
    opt = dict()
    for i in range(n+1):
        opt[i] = dict()
        opt[i][0] = 0
    for w in range(capacity+1):
        opt[0][w] = 0
    
    for i in range(1,n+1):
        for w in range(1,capacity+1):
            if volume[i-1] > w:
                opt[i][w] = opt[i-1][w]
            else:
                opt[i][w] = max(opt[i-1][w],\
                value[i-1] + opt[i-1][w-volume[i-1]])

    return opt[n][capacity]