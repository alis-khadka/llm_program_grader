def dfs(node, adj, longestPathArray, visited):
    visited[node] = True

    for i in range(len(adj[node])):
        if not visited[adj[node][i]]:
            dfs(adj[node][i], adj, longestPathArray, visited)

        longestPathArray[node] = max(
            longestPathArray[node], 1 + longestPathArray[adj[node][i]])


def calc(N, A):
    adj = [[] for i in range(N + 1)]

    for i in range(len(A)):
        adj[A[i][0]].append(A[i][1])
        longestPathArray = [0] * (N + 1)

    visited = [False] * (N + 1)

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i, adj, longestPathArray, visited)

    longestPath = 0
    for i in range(1, N + 1):
        longestPath = max(longestPath, longestPathArray[i])
		
    return longestPath