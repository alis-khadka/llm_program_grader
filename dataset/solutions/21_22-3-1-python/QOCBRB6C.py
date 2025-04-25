def opt(W):

    s = 0
    inc = W[0]
    exc = 0

    for i in range(1,len(W)):
        incn = exc + W[i]
        exc = max(exc, inc)
        inc = incn

    s = max(exc, inc)
    return s