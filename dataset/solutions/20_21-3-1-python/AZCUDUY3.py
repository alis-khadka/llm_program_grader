def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume: assert x == round(x)

    tabelle = [[0.0 for x in range(capacity + 1)] for x in range(len(value) + 1)]
    for i in range(len(value)+1): 
        for w in range(capacity+1):
            if i == 0 or w == 0:
                tabelle[i][w] = 0
            elif volume[i-1] <= w:
                if value[i-1] + tabelle[i-1][w-volume[i-1]] >= tabelle[i-1][w]:
                    tabelle[i][w] = value[i-1] + tabelle[i-1][w-volume[i-1]]
                else:
                    tabelle[i][w] = tabelle[i-1][w]
            else: 
                tabelle[i][w] = tabelle[i-1][w]
    return (tabelle[len(value)][capacity])