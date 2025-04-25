def dfs(graph, start):
    order = []
    farbe = [True for i in graph]
    order.extend(dfs_visit(graph, farbe, start))
    #for v, f in enumerate(farbe):
    #    if f:
    #        order.extend(dfs_visit(graph, farbe, v))
    ##################################################
    #ALSO EIGENTLICH IST DAS JA SO NICHT DIE VERSION #
    #DER TIEFENSUCHE AUS DEN FOLIEN...               #
    #DIE FINDET NÄMLICH AUCH DIE UNVERBUNDENEN KNOTEN#
    ##################################################
    return order
    
def dfs_visit(graph, farbe, u):
    farbe[u] = False
    order = [u]
    for v in graph[u]:
        if farbe[v]:
            order.extend(dfs_visit(graph, farbe, v))
    
    return order