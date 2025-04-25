def calc(N, A):
  def DFS(v, graph, heap, seen):
    seen[v] = True
    for i in range(len(graph[v])):
      if not seen[graph[v][i]]:
        DFS(graph[v][i], graph, heap, seen)
      heap[v] = max(heap[v], 1 + heap[graph[v][i]])
  graph = [[] for i in range(N + 1)]
  for e in A:
    graph[e[0]].append(e[1])
  heap = [0] * (N + 1)
  seen = [False] * (N + 1)
  for v in range(1, N + 1):
    if not seen[v]:
      DFS(v, graph, heap, seen)
  return max(heap)