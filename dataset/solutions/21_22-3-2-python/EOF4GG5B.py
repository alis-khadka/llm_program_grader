def calc(N, A):
  g = [[] for _ in range(N + 1)]
  m = [-1] * (N + 1)
  g[0] = [x for x in range(1, N + 1)]
  for e in A:
    start, end = e
    g[start].append(end)
  return dfs(0, g, m) - 1
  
def dfs(node, g, m):
  if len(g[node]) == 0:
    return 0
  elif m[node] != -1:
    return m[node]
  else:
    ergebnis = 0
    for child in g[node]:
      ergebnis = max(ergebnis, dfs(child, g, m) + 1)
    m[node] = ergebnis
    return m[node]