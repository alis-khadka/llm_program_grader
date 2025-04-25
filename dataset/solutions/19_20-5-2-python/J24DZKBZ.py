def dfsRec(graph,start, visited):
    if visited[start] == False:
      visited[start] = True
      result = [start]
      for v in graph[start]:
        result += dfsRec(graph,v,visited)
      return result
    else:
      return []


def dfs(graph, start):
    visited = [False] * len(graph)
    result = dfsRec(graph, start, visited)
    return result