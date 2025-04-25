def topologicalSort(u, vis, adjacent, stack):
    vis[u] = True

    for v in adjacent[u]:
        if not vis[v]:
            topologicalSort(v, vis, adjacent, stack)

    stack.append(u)

def calc(N, A):
    vis = [False for i in range(N)]
    adj = [[] for i in range(N)]
    edges = [0 for i in range(N)]

    for u, v in A:
        adj[u - 1].append(v - 1)

    stack = []
    for u in range(N):
        if not vis[u]:
            topologicalSort(u, vis, adj, stack)

    for u in stack[::-1]:
        for v in adj[u]:
            edges[v] = max(edges[v], edges[u] + 1)

    return max(edges)