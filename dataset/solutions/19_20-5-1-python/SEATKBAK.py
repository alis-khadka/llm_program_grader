def bfs(graph, start):
    queue = [start]
    checked = []
    
    
    while len(queue) > 0:
        current = queue.pop(0)
        for node in graph[current]:
            if node not in checked and node not in queue and node != current:
                queue.append(node)
        checked.append(current)
        
    return checked