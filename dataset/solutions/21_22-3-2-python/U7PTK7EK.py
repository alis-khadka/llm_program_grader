def calc(N, A):
    # create graph with children from edge list A
    graph = {i: {"children": [], "max_path": 0, "visited": False} for i in range(1, N+1)}

    for edge in A:
        graph[edge[0]]["children"].append(edge[1])

    # depth first search for graph where visited vertices are marked
    def dfs(i):
        graph[i]["visited"] = True

        for child in graph[i]["children"]:
            if not graph[child]["visited"]:
                dfs(child)

            graph[i]["max_path"] = max(graph[i]["max_path"], 1 + graph[child]["max_path"])
        

    for i in range(1, N+1):
        if not graph[i]["visited"]:
            dfs(i)

    return graph[max(graph, key=lambda i: graph[i]["max_path"])]["max_path"]