def bfs(graph, start):
    visited = [start]
    q = list()
    q.append(start)
    while len(q) != 0:
        u = q.pop(0)
        for i in graph[u]:
            if i not in visited:
                visited.append(i)
                q.append(i)
    return visited