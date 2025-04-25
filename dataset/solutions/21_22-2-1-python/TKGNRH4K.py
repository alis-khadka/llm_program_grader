def calc(A,B):

  output = ""
  
  counts = {}
  
  for i in range(len(A)): # O(n)
    # counts[A[i]] += 1
    if A[i] not in counts:
      counts[A[i]] = 0
    counts[A[i]] += 1


  for i in range(len(B)): # O(m)
    if i not in counts:
      counts[i] = 0

    output += "1" if counts[i] <= B[i] else "0"

  return output # total : O(n) + O(m) = O(n+m)
    

assert calc([0,0],[0]) == "0"
assert calc([2,2,2,3,4],[0,1,2,1,3]) == "11011"
assert calc([3,4],[0,0,0,0,0]) == "11100"