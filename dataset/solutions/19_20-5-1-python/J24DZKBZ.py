def bfs(graph, start):
    
    result = list()
    queue = list()
    queue.append(start)
    result.append(start)
    visited = [False] * len(graph)
    visited[start] = True
    
    while len(queue) != 0:
        for v in graph[queue.pop(0)]:
            if not visited[v]:
                result.append(v)
                queue.append(v)
                visited[v] = True
        

        
    return result