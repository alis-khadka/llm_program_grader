def knapSack(value, volume, capacity):
  assert len(value) == len(volume)

  n = len(value)
  heap = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

  for i in range(n + 1):
    for j in range(capacity + 1):
      if i == 0 or j == 0:
        heap[i][j] = 0
      elif volume[i-1] <= j:
        heap[i][j] = max(value[i-1] + heap[i-1][j-volume[i-1]], heap[i-1][j])
      else:
        heap[i][j] = heap[i-1][j]
  return heap[n][capacity]