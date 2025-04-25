def dfs(graph, start):
    coloredGraph = []
    abgearbeiteteKnoten = []
    
    for u in graph:
        coloredGraph.append([u,0,None])
        # [Knoten, Farbe, Vorgänger]
        # Farbe 0 ist weiß, 1 ist grau, 2 ist schwarz
    
    if coloredGraph[start][1] == 0:
        abgearbeiteteKnoten = DFS_VISIT(abgearbeiteteKnoten, coloredGraph, start)

        
    return abgearbeiteteKnoten

def DFS_VISIT(abgearbeiteteKnoten, coloredGraph, u):
    coloredGraph[u][1] = 1 
    abgearbeiteteKnoten.append(u)
    for v in coloredGraph[u][0]:
        if coloredGraph[v][1] == 0:
            coloredGraph[v][2] = u
            abgearbeiteteKnoten = DFS_VISIT(abgearbeiteteKnoten, coloredGraph, v)
    coloredGraph[u][1] = 2
    
    return abgearbeiteteKnoten