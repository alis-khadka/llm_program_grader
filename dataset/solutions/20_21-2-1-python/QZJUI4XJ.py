def calc(A,B):
  sum_i = [0]*len(B)
  count = 0
  for wert in A:
    sum_i[wert] += 1
      


  s = ""   
  for pos in range(len(B)): 
    if sum_i[pos] <= B[pos]:
      s += "1"
    else: 
      s += "0"
  return s