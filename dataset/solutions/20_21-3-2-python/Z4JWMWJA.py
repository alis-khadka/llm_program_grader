def dfs(node, graph, memo):
    if memo[node] is not None:
        return memo[node]
    ye = 0
    for child in graph[node]:
        ye = max(ye, dfs(child, graph, memo)+1)
    memo[node] = ye
    return ye

def calc(N, A):
    graph = [[] for _ in range(N+1)]
    graph[0] = list(range(1, N+1))
    memo = [None] * (N+1)
    for start, end in A:
        graph[start].append(end)
    return dfs(0, graph, memo)-1