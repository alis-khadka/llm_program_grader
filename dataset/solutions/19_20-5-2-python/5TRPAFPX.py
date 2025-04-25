#Knoten, die noch nicht in gefunden sind, sind weiß.
#Knoten, deren dfs_rek-Aufruf noch läuft sind grau.
#Knoten, deren dfs_rek-Aufruf abgeschlossen ist sind schwarz.
def dfs(graph, start):
    gefunden = []
    dfs_rek(graph, start, gefunden)
    return gefunden

def dfs_rek(graph, knoten, gefunden):
    gefunden.append(knoten)
    for zielknoten in graph[knoten]:
        if not zielknoten in gefunden:
            dfs_rek(graph, zielknoten, gefunden)