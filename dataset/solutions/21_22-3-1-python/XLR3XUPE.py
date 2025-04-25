def opt(W):
  if len(W) == 1:
    return W[0]
  A = [0] * len(W)
  for i in range(0, len(W)):
    A[i] = max(A[i-1], W[i] + A[i-2])
  return A[len(W) - 1]