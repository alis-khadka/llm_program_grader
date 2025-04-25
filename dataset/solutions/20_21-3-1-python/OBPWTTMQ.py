def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)

    l = sorted(list(range(len(volume))), key=lambda i: -volume[i])
    volume = [volume[i] for i in l]
    value = [value[i] for i in l]
    
    max_value = 0
    total_volume = 0
    total_value = 0
    for i in range(len(volume)):
        if volume[i] <= capacity:
            total_volume = volume[i]
            total_value = value[i]
            for j in range(i+1,len(volume)):
                if (total_volume + volume[j] <= capacity):
                    total_volume += volume[j]
                    total_value += value[j]
            if total_value > max_value:
                max_value = total_value
    return max_value