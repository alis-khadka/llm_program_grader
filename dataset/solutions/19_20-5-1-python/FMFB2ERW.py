def bfs(graph, start):
    visit = list()
    queue = list()
    for i in graph[start]:
        queue.append(i)
    visit.append(start)
    while len(queue) > 0:
        temp = queue.pop(0)
        if temp not in visit:
            visit.append(temp)
            for j in graph[temp]:
                queue.append(j)
    return visit