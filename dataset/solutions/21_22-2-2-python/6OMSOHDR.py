def calc(a,b):
  res = []
  c = [] 
  for i in range(0,len(a)): # O(n)
    c.append(a[i])
    if i > 0:
      c[i] += c[i-1] 
    
  for i in range(0,len(b)): # O(n)
    if b[i][1] == b[i][0]:
      res.append(a[b[i][0]])
    else:
      if b[i][0] > 0:
        res.append(c[b[i][1]] - c[b[i][0]-1])
      else:
        res.append(c[b[i][1]])
        
  return res # total: O(n) + O(n) = O(n)