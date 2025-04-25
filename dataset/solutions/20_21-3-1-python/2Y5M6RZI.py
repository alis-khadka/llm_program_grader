def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)

    result=0
    while len(value)>0:
        best_index=0
        for j in range(len(value)):
            if value[j]>value[best_index]:
                best_index=j
        if volume[best_index]<=capacity:
            result+=value[best_index]
            capacity-=round(volume[best_index])
        value.pop(best_index)
        volume.pop(best_index)
    return result