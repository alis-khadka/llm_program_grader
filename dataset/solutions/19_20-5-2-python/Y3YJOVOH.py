def dfs(graph, start):
    visited = list()
    besucht = list()
    for i in range(len(graph)):
        visited.append(False)
    def dfs_visit(start):
        visited[start] = True
        besucht.append(start)
        for v in graph[start]:
            if visited[v] == False:
                dfs_visit(v)
    dfs_visit(start)
    return (besucht)