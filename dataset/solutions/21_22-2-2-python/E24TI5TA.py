def calc(a,b):
  bearbeitet = []
  temp = [] 
  for i in range(0,len(a)):
    temp.append(a[i])
    if i > 0:
      temp[i] += temp[i-1] 
  for i in range(0,len(b)):
    if b[i][1] == b[i][0]:
      bearbeitet.append(a[b[i][0]])
    else:
      if b[i][0] > 0:
        bearbeitet.append(temp[b[i][1]] - temp[b[i][0]-1])
      else:
        bearbeitet.append(temp[b[i][1]])
        
  return bearbeitet