def dfs(node, adj, dp, vis):
    vis[node] = True 
    for i in range(0, len(adj[node])):
        if not vis[adj[node][i]]: 
            dfs(adj[node][i], adj, dp, vis)
        dp[node] = max(dp[node], 1 + dp[adj[node][i]])
def calc(N,A):
    adj = [[] for i in range(N)]
    for i in range(len(A)):
        adj[A[i][0]-1].append(A[i][1]-1)
    dp = [0] * N
    vis = [False] * N 
    for i in range(N):
        if not vis[i]:
            dfs(i, adj, dp, vis)
    return max(dp)