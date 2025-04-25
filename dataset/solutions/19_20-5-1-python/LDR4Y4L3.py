def bfs(graph, start):
    visited = [False] * (len(graph)) 
    queue = [] 
    result = []
    
    queue.append(start) 
    visited[start] = True
    
    while queue: 
      
        current_node = queue.pop(0) 
        result.append(current_node) 
      
        for i in graph[current_node]: 
            if visited[i] == False: 
                queue.append(i) 
                visited[i] = True
                                        
    return result