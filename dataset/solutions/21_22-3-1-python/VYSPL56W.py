def opt(W):
    m = W.copy()
    m[1] = max(m[0], m[1])
    for i in range(2, len(m)):
        m[i] = max(m[i-2] + m[i], m[i-1])
    return m[len(m)-1]