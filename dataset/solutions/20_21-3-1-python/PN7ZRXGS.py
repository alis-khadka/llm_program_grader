def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)

    dp = [[0 for y in range(capacity+1)] for x in range(len(volume)+1)]

    for y in range(len(volume)+1):
        for x in range(capacity+1):
            if y == 0 or x == 0:
                dp[y][x] = 0
            elif volume[y-1] <= x:
                dp[y][x] = max(value[y-1]+dp[y-1][x-volume[y-1]], dp[y-1][x])
            else:
                dp[y][x] = dp[y-1][x]
    return dp[len(volume)][capacity]

    return 0