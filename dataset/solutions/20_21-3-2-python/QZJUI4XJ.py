def calc(N,A):
    graph = []
    for x in range(N + 1):
        graph.append([])
    pfad = [-1] * (N + 1)
    graph[0] = [a for a in range(1, N + 1)]
    for k in A:
        key, value = k
        graph[key].append(value)
    return dfs(0, graph, pfad) - 1

def dfs(knoten, graph, pfad):
    n = len(graph[knoten])
    if n == 0:
        return 0
    elif pfad[knoten] != -1:
        return pfad[knoten]
    else:
        res = 0
        for child in graph[knoten]:
            res = max(res, dfs(child, graph, pfad) + 1)
        pfad[knoten] = res
        return pfad[knoten]