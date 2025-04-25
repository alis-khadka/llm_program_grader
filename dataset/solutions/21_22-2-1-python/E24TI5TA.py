def calc(A,B):
  
  zaehler = {}
  bearbeitet = ""    
  for i in range(len(A)):
    if A[i] not in zaehler:
      zaehler[A[i]] = 0
    zaehler[A[i]] += 1
  for i in range(len(B)):
    if i not in zaehler:
      zaehler[i] = 0
        
    bearbeitet += "1" if zaehler[i] <= B[i] else "0"
  return bearbeitet