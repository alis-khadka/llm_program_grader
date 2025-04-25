# O(n*capacity)

def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)

    matrix = [[0] * (capacity + 1) for x in range(len(value) + 1)]
    
    for i in range(len(value) - 1, -1, -1):
        for j in range(1, capacity + 1):
            if volume[i] <= j:
                matrix[i][j] = max(value[i] + matrix[i+1][j-volume[i]],
                        matrix[i+1][j])
            else:
                matrix[i][j] = matrix[i+1][j]

    return matrix[0][capacity]