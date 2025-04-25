def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)
    
    n = len(value)
    k = [[0 for x in range(capacity + 1)] \
    for x in range(n + 1)]
    
    for i in range(n+1):
        for c in range(capacity + 1):
            if i == 0 or c == 0: 
                k[i][c] = 0
            elif volume[i-1] <= c: 
                k[i][c] = max(value[i-1] + k[i-1][c-volume[i-1]],\
                k[i-1][c])
            else:
                k[i][c] = k[i-1][c]
    return k[n][capacity]
    
#    zw = 0
    #for x in range(len(volume)): 
    #    if volume[x] + zw <= capacity: 
    #        zw += volume[x]
#    if not value and not volume:
#        return 0
        
#    if max(volume) <= capacity: 
#       zw += max(volume)
#        volume.pop(max(volume))
        
#    for x in range(len(volume)):
#        if volume[x] + zw <= capacity:
#            zw += value[x]
#    return zw