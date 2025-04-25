def bfs(graph, start):
    # Init node properties
    colors = []
    depths = []
    predecessors = []
    order = []
    for i in range(len(graph)):
        colors.append('white')
        depths.append(float('nan'))
        predecessors.append(None)
    
    colors[start] = 'grey'
    depths[start] = 0
    # use a list as a queue
    queue = [start]
    
    while len(queue) > 0:
        u = queue.pop(0)
        order.append(u)
        current_edges = graph[u]
        for a in current_edges:
            if colors[a] == 'white':
                colors[a] = 'grey'
                depths[a] = depths[u] + 1
                predecessors[a] = u
                queue.append(a)
        colors[u] = 'black'
    return order