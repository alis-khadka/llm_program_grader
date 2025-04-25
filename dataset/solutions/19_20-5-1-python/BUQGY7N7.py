def bfs(graph, start):
    #Initialisierung
    colorList = [0] * len(graph)        #0:weiß, 1:grau, 2:schwarz
    distanceList = [-1] * len(graph)
    parentsList = [None] * len(graph)
    queue = []
    searchOrder = []

    distanceList[start] = 0
    colorList[start] = 1

    queue.append(start)
    searchOrder.append(start)

    #Suche
    while queue != []:
        u = queue.pop(0)

        for v in graph[u]:  #Alle Nachbarn von u
            if colorList[v] == 0:
                colorList[v] = 1
                distanceList[v] = distanceList[u] +1
                parentsList[v] = u

                queue.append(v)
                searchOrder.append(v)

        colorList[u] = 2

    return searchOrder