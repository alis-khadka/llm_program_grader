def calc(N,A):

    adj = buildAdj(N,A)
    dynamic = [0] * (N + 1)
    visited = [False] * (N + 1)
    for i in range(N + 1):
        if not visited[i]:
            dfs(i, adj, dynamic, visited)
    result = 0
    for i in range(N + 1):
        result = max(result, dynamic[i])
    return result

def dfs(v, adj, dynamic, visited):
    visited[v] = True
    for i in range(len(adj[v])):
        if not visited[adj[v][i]]:
            dfs(adj[v][i], adj, dynamic, visited)
        dynamic[v] = max(dynamic[v], 1 + dynamic[adj[v][i]])

def buildAdj(N,A):
    adj = [[] for i in range(N+1)]
    for i in range(len(A)):
        adj[A[i][0]].append(A[i][1])
    return adj