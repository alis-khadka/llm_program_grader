def knapSack(value, volume, capacity):
    if len(value) == 0 or len(volume) == 0:
        return 0
    matrix = [[0 for col in range(capacity+1)] for row in range(len(volume))]
    for row in range(len(volume)):  # going through the matrix we set up
        for col in range(capacity+1):
            if volume[row] > col:  # this is the check to see if the item can go into our knap-sack
                matrix[row][col] = matrix[row-1][col]  # get the item above and place
            else:
                matrix[row][col] = max(matrix[row-1][col], matrix[row-1][col-volume[row]]+ value[row])
    packed = []
    col = capacity
    for row in range(len(volume)-1,-1,-1): 
        if row == 0 and matrix[row][col] != 0:
            packed.insert(0,row)
        if matrix[row][col] != matrix[row-1][col]:
            packed.insert(0,row)
            col -= volume[row]
    return matrix[len(volume)-1][capacity]