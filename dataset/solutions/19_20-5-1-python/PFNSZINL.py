def bfs(graph, start):   
    visited_nodes = []
    next_nodes = [start]
    while next_nodes != []:
        new_next_nodes = []
        for node in next_nodes:
            if not node in visited_nodes:
                visited_nodes.append(node)
            for child in graph[node]:
                if not child in visited_nodes:
                    new_next_nodes.append(child)
        next_nodes = new_next_nodes
    return visited_nodes