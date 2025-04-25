def edelta_evaluate(edelta,i,j,u,v):
  if i == 0:
    return j
  if j == 0:
    return i
  if u[i-1] == v[j-1]:
    repcost = 0
  else:
    repcost = 1
  return min([edelta[i-1][j-1] + repcost,
              edelta[i-1][j] + 1,
              edelta[i][j-1] + 1])

def editDistance(u, v):
  m = len(u)
  n = len(v)
  edelta = [[None] * (n+1) for i in range(m+1)]
  for i in range(m+1):
    for j in range(n+1):
      edelta[i][j] = edelta_evaluate(edelta,i,j,u,v)
  return edelta[m][n]