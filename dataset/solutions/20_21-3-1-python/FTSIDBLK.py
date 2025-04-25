def knapSack(value, volume, capacity):
  n = len(value)
  K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

  for i in range(n + 1):
    for capacity in range(capacity + 1):
      if i == 0 or capacity == 0:
        K[i][capacity] = 0
      elif volume[i - 1] <= capacity:
        K[i][capacity] = max(value[i - 1] + K[i - 1][capacity - volume[i - 1]], K[i - 1][capacity])
      else:
        K[i][capacity] = K[i - 1][capacity]

  return K[n][capacity]