def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    n = len(value)

    for x in volume:
        assert x == round(x)

    p = [0 for x in range(capacity + 1)]

    for i in range(0, n):
      for x in range(capacity, volume[i] - 1,-1):
        if p[x - volume[i]] + value[i] > p[x]:
          p[x] = p[x - volume[i]] + value[i]
    return p[capacity]