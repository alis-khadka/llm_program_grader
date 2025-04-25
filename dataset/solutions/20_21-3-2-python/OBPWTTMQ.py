def dfs(node, graph, memo):
    if len(graph[node]) == 0:
        return 0
    elif memo[node] != -1:
        return memo[node]
    else:
        sol = 0
        for child in graph[node]:
            sol = max(sol, dfs(child, graph, memo) + 1)
        memo[node] = sol
        return memo[node]


def calc(N, A):
    graph = [[] for _ in range(N + 1)]
    memo = [-1] * (N + 1)
    graph[0] = [x for x in range(1, N + 1)]
    for edge in A:
        start, end = edge
        graph[start].append(end)
    return dfs(0, graph, memo) - 1