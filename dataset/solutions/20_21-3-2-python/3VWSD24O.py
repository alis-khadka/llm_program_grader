def calc(N,A):
    knoten = list(range(1,N+1))
    D = [0 for i in range(N)]
    adj = dict()
    for a in A:
        if a[0] not in adj:
            adj[a[0]] = list()
        adj[a[0]].append(a[1])
    for u in knoten:
        if u in adj:
            for v in adj[u]:
                if D[v-1] < D[u-1] + 1:
                    D[v-1] = D[u-1]+1
    return max(D)