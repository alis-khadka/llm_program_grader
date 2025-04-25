def bfs(graph, node, mList):
    if len(graph[node]) == 0:
        return 1
    if mList[node] != -1:
        return mList[node]
    nList = [0]
    for child in graph[node]:
        nList.append(bfs(graph, child, mList) + 1)
    mList[node] = max(nList)
    return max(nList)

def calc(N, A):
    graph = [[] for _ in range(N + 1)]
    memo = [-1] * (N + 1)
    graph[0] = [x for x in range(1, N + 1)]
    for edge in A:
        start, end = edge
        graph[start].append(end)
    return bfs(graph, 0, memo) - 2