def calc(A, B):
  string = ''
  dictionary = {}

  for n in A:
    dictionary[n] = dictionary.get(n, 0) + 1

  for m in range(len(B)):
    number_i = dictionary.get(m)
    if not number_i or B[m] >= number_i:
      string += '1'
    else:
      string += '0'

  return string