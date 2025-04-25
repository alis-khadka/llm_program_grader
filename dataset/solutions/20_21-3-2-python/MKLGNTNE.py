def dfs(node, adj, dp, vis):
    vis[node] = True

    for i in range(0, len(adj[node])):
        if not vis[adj[node][i]]:
            dfs(adj[node][i], adj, dp, vis)

        dp[node] = max(dp[node], 1 + dp[adj[node][i]])


def calc(N, A):
    adj = [[] for i in range(N + 1)]
    for a in A:
        adj[a[0]].append(a[1])

    dp = [0] * (N + 1)
    vis = [False] * (N + 1)

    for i in range(1, N + 1):
        if not vis[i]:
            dfs(i, adj, dp, vis)

    ans = 0
    for i in range(1, N + 1):
        ans = max(ans, dp[i])

    return ans