def knapSack(val, wt, W):
	n = len(val)
	A = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0:
				A[i][w] = 0
			elif wt[i - 1] <= w:
				A[i][w] = max(val[i-1]
                          + A[i-1][w-wt[i-1]],
                              A[i - 1][w])
			else:
				A[i][w] = A[i-1][w]

	return A[n][W]