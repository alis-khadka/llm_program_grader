def dfs(graph, start, visited = list()):
    if not visited:
        visited = [start]
    for u in graph[start]:
        if u not in visited:
            visited.append(u)
            dfs(graph, u, visited)
    return visited