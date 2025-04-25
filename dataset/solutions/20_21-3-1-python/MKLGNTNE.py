def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)

    K = [[0 for x in range(capacity + 1)] for x in range(len(volume) + 1)]

    for i in range(len(volume) + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif volume[i - 1] <= w:
                K[i][w] = max(value[i - 1]
                              + K[i - 1][w - volume[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[len(volume)][capacity]