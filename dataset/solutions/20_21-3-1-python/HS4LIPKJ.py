def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)

    value = [0] + value
    volume = [0] + volume
    obj = len(value)

    tabelle = [[0 for x in range(capacity+1)] for y in range(obj)]

    for i in range(obj):
        for c in range(capacity+1):
            if volume[i] > capacity:
                tabelle[i][c] = tabelle[i-1][c]
            else:
                if c - volume[i] < 0:
                    tabelle[i][c] = tabelle[i-1][c]
                else:
                    tabelle[i][c] = max(tabelle[i-1][c], tabelle[i-1][c-volume[i]] + value[i])

    return tabelle[-1][-1]