import queue

def dfs(graph, start):
    result = []
    discovered = [False] * len(graph)
    stack = []
    stack.append(start)
    while(stack):
        u = stack.pop()
        if(not discovered[u]):
            discovered[u] = True
            result.append(u)
            for v in reversed(graph[u]):
                stack.append(v)
    return result