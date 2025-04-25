def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)

    ratio = []
    i = 0
    for item in volume:
        if volume[i]>0:
            ratio.append([value[i] / volume[i], value[i], volume[i]])
        else:
            ratio.append([10000000, value[i], volume[i]])  # yes this is cheating, i know
        i = i + 1
    
    # sorts the items primarily by its ratio and secondly by their value
    ratio = sorted(ratio, key = lambda x:(-x[0],-x[1]))


    
    i = 0
    sack = []
    volumeSum = 0
    valueSum = 0
    # adding the items to the knapsack from the best to the worst ration until full:
    for item in ratio:
        if volumeSum + item[2] <= capacity:
            sack.append(i)
            volumeSum = volumeSum + item[2]
            valueSum = valueSum + item[1]
        i = i + 1

    return valueSum