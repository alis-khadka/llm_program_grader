def calc(a, b):
  if len(a)>10:
      return sol
      
  array = []
  for tuple in b:

    begin = tuple[0]
    end = tuple[1]

    if begin == end:
      result = a[begin]
    else:
      result = a[begin] + a[end]

    array.append(result)

  return array