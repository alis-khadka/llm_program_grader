def opt(W):
    n = len(W)
    max_gewinn = [0] * n
    for i in range(n):
        if i == 0:
            max_gewinn[i] = W[i]
        elif i == 1:
            max_gewinn[i] = max(max_gewinn[i-1], W[i])
        else:
            max_gewinn[i] = max(max_gewinn[i-1], max_gewinn[i-2] + W[i])
            
    return max_gewinn[n-1]