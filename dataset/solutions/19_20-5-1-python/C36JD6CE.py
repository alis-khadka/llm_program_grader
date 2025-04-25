import queue

def bfs(graph, start):
    coloredGraph = []
    abgearbeiteteKnoten = []
    
    for u in graph:
        coloredGraph.append([u,0,-1,None])
        # [Knoten, Farbe, Distanz zum start, Vorgänger]
        # Farbe 0 ist weiß
    
    # Farbe von start auf 1 bzw. grau setzen:
    coloredGraph[start][1] = 1
    # Distanz zum start auf 0 setzen:
    coloredGraph[start][2] = 0
    
    Q = queue.Queue()
    Q.put(start)

    while not Q.empty():
        u = Q.get()
        abgearbeiteteKnoten.append(u)
        for v in coloredGraph[u][0]:
            if coloredGraph[v][1] == 0:
                coloredGraph[v][1] = 1
                coloredGraph[v][2] = coloredGraph[u][2]+1
                coloredGraph[v][3] = u
                Q.put(v)
        coloredGraph[u][1] = 2 # 2 representiert Schwarz
    
    
    return abgearbeiteteKnoten