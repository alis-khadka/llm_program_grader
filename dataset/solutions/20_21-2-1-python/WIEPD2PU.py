def calc(A, B):
  size_A = len(A)
  budget = B
  s = ''
  for present in A:
    budget[present] -= 1

  for balance in budget:
    if balance < 0:
      s = s + '0'
    else:
      s = s + '1'
  return s