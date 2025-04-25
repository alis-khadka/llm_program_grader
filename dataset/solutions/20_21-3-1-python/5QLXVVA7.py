def knapSack(value, volume, capacity):
    assert len(value) == len(volume)
    n = len(value)    
    for i in range(n):
        assert volume[i] == round(volume[i])

    res=[0]*(n+1)
    for x in range(len(res)):
        res[x] = ([0]*(capacity+1))
    for i in range(1,n+1):
            for w in range(1,capacity+1):
                if volume[i-1] > w:
                    res[i][w] = res[i-1][w]
                elif volume[i-1] <= w:
                    res[i][w]= max(res[i-1][w],value[i-1]+res[i-1][w-volume[i-1]])
    return res[n][capacity]