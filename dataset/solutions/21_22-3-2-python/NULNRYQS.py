def calc(N,A):
    graph = [[] for i in range(N+1)]
    memo = [-1] * (N+1)
    graph[0] = [i for i in range(1, N+1)]
    for edge in A:
        start, end = edge
        graph[start].append(end)
    return dfs(0, graph, memo) - 1
    

def dfs(node, graph, memo):
    if len(graph[node]) == 0:
        return 0
    elif memo[node] != -1:
        return memo[node]
    else:
        sol = 0
        for child in graph[node]:
            sol = max(sol, dfs(child, graph, memo)+1)
        memo[node] = sol
        return memo[node]