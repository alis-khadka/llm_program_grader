def dfs_help(graph, stack, visited):
    
    # if we have no nodes left to visit, return the result
    if len(stack) == 0:
        return visited
    
    # otherwise the stack has nodes left. 
    # add the top-most of these to the visited nodes and stack 
    # its neighbours that are not already visited. If they are
    # already stacked, move them to the top
    node = stack.pop()
    visited.append(node)
    for neighbour in reversed(graph[node]):
        if neighbour not in visited:
            if neighbour not in stack:
                stack.append(neighbour)
            else:
                stack.remove(neighbour)
                stack.append(neighbour)
        
    return dfs_help(graph, stack, visited)

def dfs(graph, start):
    return dfs_help(graph, [start], [])