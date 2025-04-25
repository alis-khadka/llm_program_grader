def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)
    table = [[0 for x in range(capacity + 1)] for x in range(len(value) + 1)] 
  
    # Build table table[][] in bottom up manner 
    for i in range(len(value) + 1): 
        for w in range(capacity + 1): 
            if i == 0 or w == 0: 
                table[i][w] = 0
            elif volume[i-1] <= w: 
                table[i][w] = max(value[i-1] + table[i-1][w-volume[i-1]],  table[i-1][w]) 
            else: 
                table[i][w] = table[i-1][w] 
  
    return table[len(value)][capacity]