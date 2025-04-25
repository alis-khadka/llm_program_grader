def longestPathDFS(N, adjfrom, adjto, i):
    q1 = [i]
    q2 = []
    c = [0] * (N + 1)
    d = [0] * (N + 1)

    d[i] = 0

    longestPath = 0

    while len(q1) > 0 or len(q2) > 0:
        if len(q1) > 0:
            j = q1.pop(0)

            viable = True
            for v in adjfrom[j]:
                if c[v] != 2:
                    viable = False

        else:
            j = q2.pop(0)
            viable = True
            for v in adjfrom[j]:
                if c[v] == 1:
                    viable = False

        if not viable:
            q2.append(j)
            continue

        if viable:
            c[j] = 2
            longestPath = max(d[j], longestPath)

            for v in adjto[j]:
                d[v] = max(d[v], d[j] + 1)

                if c[v] == 0:
                    c[v] = 1

                    q1.append(v)

    return longestPath


def calc(N, E):
    adjfrom = [0]
    adjto = [0]
    for i in range(N):
        adjfrom.append(list())
        adjto.append(list())

    for e in E:
        adjfrom[e[1]].append(e[0])
        adjto[e[0]].append(e[1])

    longestPath = 0
    for i, v in enumerate(adjfrom[1:], start=1):
        if len(v) == 0:
            longestPath = max(
                longestPath, longestPathDFS(N, adjfrom, adjto, i))

    return longestPath