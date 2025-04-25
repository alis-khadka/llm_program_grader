def knapSack(value, volume, capacity):
	n = len(value)
	A = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
	for i in range(n + 1):
		for w in range(capacity + 1):
			if i == 0 or w == 0:
				A[i][w] = 0
			elif volume[i - 1] <= w:
				A[i][w] = max(value[i-1]
                          + A[i-1][w-volume[i-1]],
                              A[i - 1][w])
			else:
				A[i][w] = A[i-1][w]

	return A[n][capacity]