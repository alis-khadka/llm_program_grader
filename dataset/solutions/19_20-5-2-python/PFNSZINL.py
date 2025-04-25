def dfs(graph, start):
    return dsf_rekursive(graph, start, [])

def dsf_rekursive(graph, start, visited):
    visited.append(start)
    children = graph[start]
    for child in children:
        if not child in visited:
            dsf_rekursive(graph, child, visited)
    return visited