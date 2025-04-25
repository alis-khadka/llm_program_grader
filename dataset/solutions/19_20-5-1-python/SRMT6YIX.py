def bfs(graph, start):
    visited =[start]  
    Q = [start]
    while(Q):
        u = Q.pop()
        for n in graph[u]:
            if n not in visited:
                Q = [n] + Q
                visited.append(n)
    return visited