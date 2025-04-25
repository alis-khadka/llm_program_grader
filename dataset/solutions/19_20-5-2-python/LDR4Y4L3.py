def DFSUtilFunction(start, visited, result): 
  
    visited[start] = True
#    print(start, end = ' ') 
    result.append(start)

    for i in graph[start]: 
        if visited[i] == False: 
            start = i
            DFSUtilFunction(start, visited, result) 
            
def dfs(graph, start):
    result = []
    if len(graph)<2:
        result.append(start)
        return result
        
   
    result = []
    visited = [False] * (len(graph)) 
  
    DFSUtilFunction(start, visited, result)
    
    return result