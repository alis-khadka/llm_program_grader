def topologicalSort(v, visited, adjacent, stack):
    visited[v] = True

    for n in adjacent[v]:
        if not visited[n]:
            topologicalSort(n, visited, adjacent, stack)
    
    stack.append(v)

def calc(verticesAmount, edges):
    visited = [False for i in range(verticesAmount)]
    adjacent = [[] for i in range(verticesAmount)]
    connections = [0 for i in range(verticesAmount)]

    for a, b in edges:
        # add edges to adjacency list
        # convert indices from [1; N] to [0; N-1]
        adjacent[a-1].append(b-1)

    # topologically sort vertices
    stack = []
    for v in range(verticesAmount):
        if not visited[v]:
            topologicalSort(v, visited, adjacent, stack)
    
    # calculate distance to adjacent vertices in topological order
    for v in stack[::-1]:
        for n in adjacent[v]:
            connections[n] = max(connections[n], connections[v] + 1)

    return max(connections)