def dfs(graph, start):
    results: list = list()

    results.append(start)
    results = dfs_visit(start, results, graph)

    return results


def dfs_visit(u, results, graph):

    for vertex in graph[u]:
        if not vertex in results:
            results.append(vertex)
            dfs_visit(vertex, results, graph)

    return results