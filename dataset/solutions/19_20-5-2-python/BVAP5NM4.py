def dfs(graph, start):
    visited = list()
    dfs_visit(graph, visited, start)
    return visited


def dfs_visit(graph, visited, u):
    if u not in visited:
        visited.append(u)
        for i in graph[u]:
            dfs_visit(graph, visited, i)