def dfs(i, vis, adj, dp):
    vis[i] = True

    for j in adj[i]:
        if not vis[j]:
            dfs(j, vis, adj, dp)

        dp[i] = max(dp[i], dp[j]+1)


def calc(n, a):
    dp = [0] * (n+1)
    vis = [False] * (n+1)

    adj = [[] for _ in range(n+1)]

    for edge in a:
        adj[edge[0]].append(edge[1])

    for i in range(n):
        if not vis[i]:
            dfs(i, vis, adj, dp)

    ans = 0
    for i in dp:
        ans = max(ans, i)

    return ans