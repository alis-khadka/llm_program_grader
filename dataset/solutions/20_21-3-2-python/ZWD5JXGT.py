def getSubPathLength(n, adjazenz, subPathLengths):
    if subPathLengths[n] == 0:
        maxLen = 0
        for b in adjazenz[n]:
           maxLen = max(getSubPathLength(b, adjazenz, subPathLengths) + 1, maxLen)
        subPathLengths[n] = maxLen
        return maxLen
    else:
        return subPathLengths[n]

def calc(N,A):
    adjazenz = []
    
    for n in range(N):
        adjazenz.append([])
    
    for a, b in A:
        adjazenz[a - 1].append(b - 1)
    
    subPathLengths = [0] * N
    
    for n in range(N):
        getSubPathLength(n, adjazenz, subPathLengths)
    
    maxLen = 0
    for length in subPathLengths:
        maxLen = max(maxLen, length)
    
    return maxLen