def calc(N, A):
    graph = [[] for _ in range(N + 1)]
    table = [-1] * (N + 1)
    graph[0] = [x for x in range(1, N + 1)]
    for edge in A:
        start, end = edge
        graph[start].append(end)
    return tiefenSuche(0, graph, table) - 1
    
def tiefenSuche(node, graph, table):
    if len(graph[node]) == 0:
        return 0
    elif table[node] != -1:
        return table[node]
    else:
        sol = 0
        for child in graph[node]:
            sol = max(sol, tiefenSuche(child, graph, table) + 1)
        table[node] = sol
        return table[node]