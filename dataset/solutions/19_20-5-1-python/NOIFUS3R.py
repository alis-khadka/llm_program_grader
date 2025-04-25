def bfs(graph, start):
    frontier = [start]
    visited = []
    
    while frontier:
        node = frontier.pop(0)
        if not node in visited:
            visited.append(node)
            
            neighbors = graph[node]
            
            for neighbor in neighbors:
                if not neighbor in visited:
                    frontier.append(neighbor)
    return visited