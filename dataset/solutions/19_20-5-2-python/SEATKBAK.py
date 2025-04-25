def dfs(graph, start):
    stack = [start]
    checked = []
    
    while len(stack) > 0:
        current = stack[-1]
        if current not in checked:
            checked.append(current)
        all_neighbor_visited = True
        for node in graph[current]:
            if node not in checked and node not in stack and node is not current:
                stack.append(node)
                all_neighbor_visited = False
                break
        if all_neighbor_visited:
            stack.pop()
        
    return list(checked)