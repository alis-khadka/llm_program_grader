def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert isinstance(x, int)

    l = sorted(range(len(volume)), key=lambda i: -volume[i])
    volume = [volume[i] for i in l]
    value = [value[i] for i in l]
    
    max_value = 0

    for i in range(len(volume)):
        total_volume = 0
        total_value = 0
        for j in range(i, len(volume)):
            if (total_volume + volume[j] <= capacity):
                total_volume += volume[j]
                total_value += value[j]
        max_value = max(total_value, max_value)

    return max_value