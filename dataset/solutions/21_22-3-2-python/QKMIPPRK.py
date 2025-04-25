def calc(N,A):
    # Basisfälle: keine Knoten, ein Knoten oder zu viele Knoten
    if N <= 1 or N > 2500:
        return 0
    
    LP = [0] * N
    
    # Liste A nach dem Startpunkt e[0] einer Kante e neu sortieren
    E = sorted(A, key=lambda e:e[0])
        
    # längsten Pfad berechnen
    # maximale Distanz für jeden Knoten i abspeichern
    for edge in E:
        LP[edge[1]-1] = max(LP[edge[0]-1]+1, LP[edge[1]-1])
    return max(LP) # LP[len(E)]