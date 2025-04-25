def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)

  
    n = len(value)
    table = [[0 for x in range(capacity + 1)] for x in range(n + 1)] 
  
    
    for i in range(n + 1): 
        for c in range(capacity + 1): 
            if i == 0 or c == 0: 
                table[i][c] = 0
            elif volume[i-1] <= c: 
                table[i][c] = max(value[i-1] + table[i-1][c-volume[i-1]],  table[i-1][c]) 
            else: 
                table[i][c] = table[i-1][c] 
  
    return table[n][capacity]