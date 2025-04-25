def calc(f):
    N = 10**18
    L = 0
    while 1:
        if f(N) == 1 and f(N - 1) == 0:
            return N
        if f(N):
            L = N
            N >>= 1
        else:
            N = (N + L) >> 1