def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)

    # TODO
    sol = [[0 for x in range(capacity + 1)] for x in range(len(value) + 1)]
    for i in range(1, len(value) + 1): 
        for w in range(1, capacity + 1):
            if (w < volume[i - 1]):
                sol[i][w] = sol[i - 1][w]
            else:
                sol[i][w] = max(sol[i - 1][w],value[i - 1] + sol[i - 1][w - volume[i - 1]])
    return sol[len(value)][capacity]