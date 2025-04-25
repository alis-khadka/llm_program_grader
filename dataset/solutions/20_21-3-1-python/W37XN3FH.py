def knapSack(val, wei, cap):
    assert len(val) == len(wei)

    n = len(val) #count of arguments
    table = [[0 for x in range(cap + 1)] for x in range(n + 1)]  #initialize calculate table with 0 "borders"

    for i in range(n + 1):
        for j in range(cap + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif wei[i-1] <= j:
                table[i][j] = max(val[i - 1]
                                  + table[i - 1][j - wei[i-1]], table[i-1][j])
            else:
                table[i][j] = table[i-1][j]
    return table[n][cap]