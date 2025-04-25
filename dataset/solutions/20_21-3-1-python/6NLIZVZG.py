def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)

    # TODO
    l = sorted(list(range(len(volume))), key=lambda i: -volume[i])
    
    volume = [volume[i] for i in l]
    value = [value[i] for i in l]
    
    maxvalue = 0
    tvolume = 0
    tvalue = 0
    
    for i in range(len(volume)):
        if volume[i] <= capacity:
            tvolume = volume[i]
            tvalue = value[i]
            for j in range(i + 1, len(volume)):
                if (tvolume + volume[j] <= capacity):
                    tvolume += volume[j]
                    tvalue += value[j]
            if tvalue > maxvalue:
                maxvalue = tvalue

    return maxvalue

    return 0