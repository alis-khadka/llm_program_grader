def knapSack(value, volume, capacity):
    assert len(value) == len(volume)
    n = len(value)
    for x in volume:
        assert x == round(x)

    A = (n + 1) * [[0]]
    A[0] = (capacity + 1) * [0]
    for i in range(1, n + 1):
        A[i] = [0]
        for w in range(1, capacity + 1):
            a = A[i-1][w]
            if volume[i-1] > w:
                A[i] += [a]
            else:
                A[i] += [max(a, value[i-1] + A[i-1][w - volume[i-1]])]

    return A[n][capacity]