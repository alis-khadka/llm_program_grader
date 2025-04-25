def knapSack(value, volume, capacity):
    assert len(value) == len(volume)
    for x in volume:
        assert x == round(x)
    if len(value) == 0 or len(volume) ==0:
        return 0
    # TODO
    old_opt = [0]*(capacity+1)
    for thing in range(len(volume)):
        opt = old_opt[::]
        for weight in range(capacity+1):
            leftweight = weight - volume[thing]
            if leftweight >= 0:
                new_combi = old_opt[leftweight] + value[thing]
                if new_combi > opt[weight]:
                    opt[weight] = new_combi
        old_opt = opt
    return opt[capacity]