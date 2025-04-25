def bfs(graph, start):
    result: list = list()

    result.append(start)

    for element in result:
        for vertex in graph[element]:
            if not vertex in result:
                result.append(vertex)

    return result