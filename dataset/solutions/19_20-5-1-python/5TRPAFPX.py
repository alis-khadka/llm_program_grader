#Knoten, die noch nicht in gefunden sind, sind weiß.
#Knoten in gefunden, die for noch nicht durchlaufen hat sind grau.
#Knoten in gefunden, die for schon durchlaufen hat sind schwarz.
def bfs(graph, start):
    gefunden = [start]
    for knoten in gefunden:
        for zielknoten in graph[knoten]:
            if not zielknoten in gefunden:
                gefunden.append(zielknoten)
    return gefunden