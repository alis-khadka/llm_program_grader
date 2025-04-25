def knapSack(value, volume, capacity):
    assert len(value) == len(volume)
    
    for x in volume:
        assert x == round(x)

    twod = [] 
    for i in range(0, len(volume)+1):
        new = []
        for j in range(0, capacity+1):
            new.append(0)
        twod.append(new)

    for i in range(1, len(volume)+1):
        for w in range(0, capacity+1):
            if volume[i-1] > w:
                twod[i][w] = twod[i-1][w]
            else:
                twod[i][w] = max(twod[i-1][w], value[i-1] + twod[i-1][w - volume[i-1]])

    return twod[len(volume)][capacity]