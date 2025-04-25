def bfs(graph, start):
    Q=[]
    l=[]
    Q.append(start)
    l.append(start)
    while len(Q)>0:
        start=Q.pop(0)
        for i in range(len(graph[start])):
            if graph[start][i] not in l:
                Q.append(graph[start][i])
                l.append(graph[start][i])
    return (l)