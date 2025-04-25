def solution(A):
    if len(A) < 2:
        return A 
  
    mitte = len(A) // 2
    links_array = solution(A[:mitte])
    rechts_array = solution(A[mitte:])
    return merge(links_array, rechts_array)
  
def merge(links, rechts):
    ergebnis = []
    i = 0
    j = 0
    while i < len(links) and j < len(rechts):
      if links[i] < rechts[j]:
          ergebnis.append(links[i])
          i += 1
      else: 
          ergebnis.append(rechts[j])
          j += 1 
    ergebnis += links[i:]
    ergebnis += rechts[j:]
  
    return ergebnis