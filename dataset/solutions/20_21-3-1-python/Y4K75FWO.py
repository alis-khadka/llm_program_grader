def knapSack(value, volume, capacity):
    assert len(value) == len(volume)
 
        
    for x in volume:
        assert x == round(x)

    # TODO
    n = len(volume)
    k = [[0 for x in range(capacity+1)] for x in range(n+1)]
    
    for i in range(n+1):
        for w in range(capacity+1):
            if i==0 or w ==0:
                k[i][w] = 0
            elif volume[i-1] <= w:
                k[i][w] = max(value[i-1]+k[i-1][w-volume[i-1]],k[i-1][w])
            else:
                k[i][w] = k[i-1][w]
                
    return k[n][capacity]