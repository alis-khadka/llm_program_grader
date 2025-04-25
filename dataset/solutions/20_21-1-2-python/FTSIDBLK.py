def solution(A):
  n = len(A)
  return merge_srt(A, 0, n - 1)


def merge_srt(A, l, r):
  if l < r:

    p = (l + r) // 2

    merge_srt(A, l, p)
    merge_srt(A, p + 1, r)
    merge(A, l, p, r)
    return(A)


def merge(A, l, p, r):
  n1 = p - l + 1
  n2 = r - p

  L = [0] * (n1)
  R = [0] * (n2)

  for i in range(0, n1):
    L[i] = A[l + i]

  for j in range(0, n2):
    R[j] = A[p + 1 + j]

  i = 0
  j = 0
  k = l

  while i < n1 and j < n2:
    if L[i] <= R[j]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1
    k += 1

  while i < n1:
    A[k] = L[i]
    i += 1
    k += 1

  while j < n2:
    A[k] = R[j]
    j += 1
    k += 1