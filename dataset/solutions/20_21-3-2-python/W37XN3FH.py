def dfs(node, adj, dp, vis):
    vis[node] = True

    for i in range(0, len(adj[node])):
        if not vis[adj[node][i]]:
            dfs(adj[node][i], adj, dp, vis)

        dp[node] = max(dp[node], 1 + dp[adj[node][i]])


def addEdge(adj, tupel):
    adj[tupel[0]].append(tupel[1])


def calc(n, A):
    adj = [[] for i in range(n + 1)]

    for i in A:
        addEdge(adj, i)

    # Dp array
    dp = [0] * (n + 1)

    vis = [False] * (n + 1)

    # Call DFS for every unvisited vertex
    for i in range(1, n + 1):
        if not vis[i]:
            dfs(i, adj, dp, vis)

    ans = 0

    for i in range(1, n + 1):
        ans = max(ans, dp[i])

    return ans