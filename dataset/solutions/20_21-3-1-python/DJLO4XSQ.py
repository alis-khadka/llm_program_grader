def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)

    n=len(value)
    table = [[0 for x in range(capacity + 1)] for x in range(n + 1)] 
 
    for i in range(n + 1): 
        for j in range(capacity + 1): 
            if i == 0 or j == 0: 
                table[i][j] = 0
            elif volume[i-1] <= j: 
                table[i][j] = max(value[i-1] + table[i-1][j-volume[i-1]],  
                table[i-1][j]) 
            else: 
                table[i][j] = table[i-1][j] 
   
    return table[n][capacity]