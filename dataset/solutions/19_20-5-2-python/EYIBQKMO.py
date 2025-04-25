def dfs(graph, start):
    s = []
    s.append(start)
    result = []
    while len(s) >0:
        current = s.pop()
        graph[current].reverse()
        s = s + graph[current]
        graph[current]=[]
        if current not in result:
            result.append(current)
    return result