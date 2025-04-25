def dfs2(graph, start, visit):
    for i in graph[start]:
        if i not in visit:
            visit.append(i)
            dfs2(graph, i, visit)
    return visit

def dfs(graph, start):
    visit = list()
    visit.append(start)
    visit = dfs2(graph, start, visit)
    return visit