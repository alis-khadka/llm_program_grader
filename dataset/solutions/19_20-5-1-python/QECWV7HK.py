import queue

def bfs(graph, start):
    result = [start]
    color = [0] * len(graph)
    color[start] = 2
    q = queue.Queue(len(graph))
    q.put(start)
    while(not q.empty()):
        u = q.get()
        for v in graph[u]:
            if(color[v] == 0):
                color[v] = 1
                result += [v]
                q.put(v)
        color[u] = 2
    return result