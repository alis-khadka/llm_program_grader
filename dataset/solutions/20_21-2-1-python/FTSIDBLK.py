def calc(A, B):
  string = ''
  d = {}
  for l in A:
    d[l] = d.get(l, 0) + 1

  for m in range(len(B)):
    try:
      number_i = d[m]
      if B[m] < number_i:
        string += '0'
      else:
        string += '1'
    except KeyError:
      string += '1'

  return string