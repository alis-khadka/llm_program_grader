def dfs(graph, start):
    frontier = [start]
    visited = []
    
    while frontier:
        node = frontier.pop()
        if not node in visited:
            visited.append(node)
            
            neighbors = graph[node]
            
            for i in range(len(neighbors)):
                if not neighbors[-(i+1)] in visited:
                    frontier.append(neighbors[-(i+1)])
    return visited