def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    n = len(value)

    for x in volume:
        assert x == round(x)

    A = [[0 for x in range(capacity+1)] for y in range(n+1)]
    
    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if volume[i-1] > w:
                A[i][w] = A[i-1][w]
            else:
                A[i][w] = max(A[i-1][w], value[i-1] + A[i-1][w-volume[i-1]])

    return A[n][capacity]