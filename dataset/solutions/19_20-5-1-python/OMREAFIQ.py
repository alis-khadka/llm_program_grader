import queue

def bfs(graph, start):
    q = queue.Queue()
    q.put(start)
    result = []
    while not q.empty():
        current = q.get()
        for i in graph[current]:
            q.put(i)
        graph[current] = []
        if current not in result: 
            result.append(current)
    return result