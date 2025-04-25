def bfs(graph, start):
    visited = list()
    for i in range(len(graph)):
        visited.append(False)
    Q = list()
    visited[start] = True
    Q.append(start)
    deqed = list()
    while len(Q) > 0:
        u = Q.pop(0)
        deqed.append(u)
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                Q.append(v)
    return (deqed)