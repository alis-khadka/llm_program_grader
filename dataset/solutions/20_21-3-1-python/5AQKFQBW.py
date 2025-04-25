def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)

    n = len(value)

    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(1, n+1):

        for j in range(1, capacity+1):

            if volume[i-1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max( dp[i -1][j], dp[i - 1][j - volume[i - 1]] + value[i - 1])

    return dp[n][capacity]