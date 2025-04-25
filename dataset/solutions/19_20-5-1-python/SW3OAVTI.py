import queue

def bfs(graph, start):
    a = queue.Queue()
    a.put(start)
    result = []
    while not a.empty():
        current = a.get()
        for x in graph[current]:
            a.put(x)
        graph[current] = []
        if current not in result:
            result.append(current)
    return result