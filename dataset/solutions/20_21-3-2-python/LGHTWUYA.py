def longestPathFrom(E, v, memo):
    lp = 0
    for x in E[v]:
        if x not in memo:
            memo[x] = longestPathFrom(E, x, memo)
        if memo[x] +1 > lp:
            lp = memo[x] + 1
    return lp


def calc(N, A):

    E = {}
    for v in range(1, N+1):
        E[v] = []

    for u, v in A:
        E[u].append(v)

    memo = {}
    lp = 0
    for v in range(1, N+1):
        p = longestPathFrom(E, v, memo)
        if p > lp:
            lp = p
    return lp