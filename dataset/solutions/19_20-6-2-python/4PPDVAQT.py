def knapSack(val, vol, cap):
    assert len(val) == len(vol)

    for x in vol:
        assert x == round(x)
    matrix = [[0 for x in range(cap + 1)] for x in range(len(val) + 1)] 
    for j in range(cap + 1): 
        for i in range(len(val) + 1): 
            if i == 0 or j == 0: 
                matrix[i][j] = 0
            elif vol[i-1] <= j: 
                matrix[i][j] = max(val[i-1] + matrix[i-1][j-vol[i-1]],  matrix[i-1][j]) 
            else: 
                matrix[i][j] = matrix[i-1][j] 
  
    return matrix[len(val)][cap]