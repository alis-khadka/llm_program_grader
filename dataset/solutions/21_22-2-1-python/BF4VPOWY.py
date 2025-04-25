def calc(A, B):
  string = ''
  dictionary = {}

  for a in A:
    dictionary[a] = dictionary.get(a, 0) + 1

  for b in range(len(B)):
    number_i = dictionary.get(b)
    if not number_i or B[b] >= number_i:
      string += '1'
    else:
      string += '0'

  return string