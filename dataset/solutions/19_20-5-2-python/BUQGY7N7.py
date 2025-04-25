def dfs(graph, start):
    colorList = [0] * len(graph)        #0:weiß, 1:grau, 2:schwarz
    parentsList = [None] * len(graph)
    searchOrder = []
    time = 0
    finishTime = [-1] * len(graph)

    u = start
    colorList, parentsList, searchOrder, finishTime, time, = dfs_visit(
                graph, colorList, parentsList, searchOrder, finishTime, time, u)

    return searchOrder

def dfs_visit(graph, colorList, parentsList, searchOrder, finishTime, time, u):
    colorList[u] = 1
    time = time + 1
    searchOrder.append(u)

    for v in graph[u]:
        if colorList[v] == 0:
            parentsList[v] = u
            dfs_visit(graph, colorList, parentsList, searchOrder, finishTime, time, v)

    colorList[u] = 2
    time = time + 2
    finishTime[u] = time

    return colorList, parentsList, searchOrder, finishTime, time