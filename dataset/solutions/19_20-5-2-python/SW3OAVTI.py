def dfs(graph, start):
    x = []
    x.append(start)
    result = []
    while len(x) > 0:
        current = x.pop()
        graph[current].reverse()
        x = x + graph[current]
        graph[current] = []
        if current not in result:
            result.append(current)
    return result