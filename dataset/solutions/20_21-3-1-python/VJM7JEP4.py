def knapSack(value, volume, capacity):
    assert len(value) == len(volume) # Gleiche Anzahl an Volumen und Werten

    for x in volume:
        assert x == round(x) # Nur ganze Zahlen als Volumen
        
    assert capacity == round(capacity) # Nur ganze Zahlen als Maximalvolumen

    n = len(value)
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)] 


    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif volume[i - 1] <= w: 
                K[i][w] = max(value[i - 1] + K[i - 1][w - volume[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][capacity]