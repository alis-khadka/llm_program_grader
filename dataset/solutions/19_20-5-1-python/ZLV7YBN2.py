def bfs(graph, start):
    result, queue = [start],[start]
    
    while (len(queue) != 0):
        for elem in graph[queue.pop(0)]:
            if elem not in result:
                result.append(elem)
                queue.append(elem)
        
    return result