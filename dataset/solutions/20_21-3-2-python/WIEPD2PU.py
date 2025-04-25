def calc(N,A):
    matrix = [[0 for i in range(N + 1)] for i in range(N + 1)]

    found = [0 for i in range(N + 1)]

    adj = [[False for i in range(N + 1)] for i in range(N + 1)]

    for a in A:
      adj[a[0]][a[1]] = True

    for i in range(1, N + 1):
      for j in range(1, N + 1):
        if adj[i][j]:
          if found[i] > 0:
            pass
          else:
            found[i] = max([matrix[n][i] for n in range(i + 1)]) + 1
          matrix[i][j] = found[i]
    res = max(found)
    return res