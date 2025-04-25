def calc(N,A):
    adj = [None] * N
    for v in range(N):
        adj[v] = []
    for a in A:
        v,w = a
        v -= 1
        w -= 1
        adj[v].append(w)

    l = 0
    cache = [None] * N
    for v in range(N):
        l = max(l, L(adj,v, cache))
    return l
    
def L(adj,v, cache):
    if cache[v] is not None:
        return cache[v]

    l = 0
    for w in adj[v]:
        l = max(l, 1+L(adj, w, cache))

    cache[v] = l
    return l