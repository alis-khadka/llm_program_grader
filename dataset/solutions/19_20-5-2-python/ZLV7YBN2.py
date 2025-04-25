def dfsRec(graph, start, visited):
    if visited[start] == False:
        
      visited[start]=True
      result = [start]
    
      for elem in graph[start]:
        result += dfsRec(graph,elem, visited)
      return result
    return []  


def dfs(graph,start):
  visited = [False]*len(graph)
  return dfsRec(graph, start, visited)