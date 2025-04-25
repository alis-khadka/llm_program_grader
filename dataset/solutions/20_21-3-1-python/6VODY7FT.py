import numpy as np


def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)

    res = np.zeros(shape=(len(value)+1, capacity+1))

    for i in range(1, len(value)+1):
        for w in range(1, capacity+1):
            if volume[i-1] > w:
                res[i, w] = res[i - 1, w]
            else:
                res[i, w] = max(res[i - 1, w], value[i-1] + res[i - 1, w - volume[i-1]])
    result = res[len(value), capacity]
    return int(result) if result.is_integer() else result