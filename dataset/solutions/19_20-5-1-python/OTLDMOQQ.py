def bfs(graph, start):
    order = []
    #Farben: 0=weiß, 1=grau
    farbe = [0 for i in graph]#alle weiß
    farbe[start] = 1
    order.append(start)
    q = [start]
    while q:
        u = q.pop(0)
        for v in graph[u]:
            if farbe[v] == 0:
                farbe[v] = 1
                q.append(v)
                order.append(v)
    
    return order