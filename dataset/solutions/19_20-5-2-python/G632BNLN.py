def dfs(graph, start):
    l=[]
    S=[]
    S.append(start)
    while len(S)>0:
        start=S.pop(len(S)-1)
        if start not in l:
            l.append(start)
        for i in range(len(graph[start])-1,-1,-1):
            if graph[start][i] not in l:
                S.append(graph[start][i])
    return (l)