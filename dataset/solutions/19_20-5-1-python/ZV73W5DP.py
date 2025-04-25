def bfs(graph, start):
    color = []
    queue = []
    result = []
    for i in range(len(graph)):
        color.append(0)
    color[start] = 1
    queue.append(start)
    while queue != []:
        elem = queue.pop(0)
        for x in graph[elem]:
            if color[x] == 0:
                color[x] = 1
                queue.append(x)
        color[elem] = 1
        result.append(elem)
            
    return result