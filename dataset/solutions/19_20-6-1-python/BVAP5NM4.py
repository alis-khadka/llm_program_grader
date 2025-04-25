def editDistance(a, b):
    m = len(a)
    n = len(b)
    edit_matrix = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        edit_matrix[i][0] = edit_matrix[i-1][0] + 1
    for j in range(1, n+1):
        edit_matrix[0][j] = edit_matrix[0][j-1] + 1
        for i in range(1, m+1):

            insert = edit_matrix[i][j-1] + 1
            delete = edit_matrix[i-1][j] + 1

            
            if a[i-1] == b[j-1]:
                replace = edit_matrix[i-1][j-1]
            else:
                replace = edit_matrix[i-1][j-1] + 1

            edit_matrix[i][j] = min(insert, delete, replace)
    return edit_matrix[m][n]