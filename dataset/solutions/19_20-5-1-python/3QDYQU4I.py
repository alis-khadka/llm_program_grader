def bfs_help(graph, queue, visited):
    
    # if we have no nodes left to visit, return the result
    if len(queue) == 0:
        return visited
    
    # otherwise the queue has nodes left. 
    # add the first of these to the visited nodes and queue its 
    # neighbours that are not already visited or queued
    node = queue.pop(0)
    visited.append(node)
    for neighbour in graph[node]:
        if neighbour not in visited and neighbour not in queue:
            queue.append(neighbour)
        
    return bfs_help(graph, queue, visited)

def bfs(graph, start):
    return bfs_help(graph, [start], [])