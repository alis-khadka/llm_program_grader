def editDistance(a, b):
    m = len(a)
    n = len(b)
    
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
  
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0: 
                dp[i][j] = j
            elif j == 0: 
                dp[i][j] = i
            elif a[i-1] == b[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace 
    return dp[m][n]