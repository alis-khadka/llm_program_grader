def opt(W):
    max_profit = [0] * len(W)
    max_profit[0:2] = [W[0], max(W[0], W[1])]

    for i in range(2, len(W)):
        max_profit[i] = max(W[i] + max_profit[i - 2], max_profit[i - 1])

    return max_profit[-1]