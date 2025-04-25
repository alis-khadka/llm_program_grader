def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)

    itemsLen = len(value)
    matrix = [[0 for i in range(capacity+1)] for w in range(itemsLen+1)]
    i = w = 0
    for i in range(1, itemsLen+1):
        for w in range(1, capacity+1):
            vi, wi = value[i-1], volume[i-1]
            if wi > w:
                matrix[i][w] = matrix[i-1][w]
            else:
                matrix[i][w] = max(matrix[i-1][w], vi + matrix[i-1][w-wi])
    return matrix[i][w]