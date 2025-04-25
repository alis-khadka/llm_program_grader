########## Loesung ##########
def dfs(graph, start):
    colors = []
    discovery_order = []
    for i in range(len(graph)):
        colors.append('white')
    time = -1
    
    (time, colors, discovery_order) = dfs_visit(start, graph, time, colors, discovery_order)
    return discovery_order

def dfs_visit(u, graph, time, colors, discovery_order):
    colors[u] = 'grey'
    time = time + 1
    discovery_order.append(u)
    current_edges = graph[u]
    for a in current_edges:
        if colors[a] == 'white':
            (time, colors, discovery_order) = dfs_visit(a, graph, time, colors, discovery_order)
    colors[u] = 'black'
    time = time + 1
    return (time, colors, discovery_order)