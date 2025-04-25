def dfs(graph, start):
    color = []
    result = [start]
    for i in range(len(graph)):
        color.append(0)
    color[start] = 1
    for elem in graph[start]:
        if (color[elem] == 0):
            dfsbesuch(graph, elem, result, color)
    return result


def dfsbesuch(graph, curr, result, color):
    color[curr] = 1
    result.append(curr)
    for elem in graph[curr]:
        if color[elem] == 0:
            dfsbesuch(graph, elem, result, color)