#! /usr/bin/env python3

def knapSack(value, volume, capacity):
    assert len(value) == len(volume)
    n = len(volume)
    best_combi_matrix = [[0 for x in range(capacity+ 1)] for x in range(n + 1)] 
    
   
    for x in volume:
        assert x == round(x)
    
    for i in range(n+1):
        
        for c in range(capacity+1):
            if i ==0 or c == 0: # gegenstaende nicht 2 mal hinzufügen
                best_combi_matrix[i][c] = 0
                
            elif volume[i-1] <= c:
                best_combi_matrix[i][c] = max(value[i-1] + best_combi_matrix[i-1][c-volume[i-1]], best_combi_matrix[i-1][c])
                
            else: 
                best_combi_matrix[i][c] = best_combi_matrix[i-1][c]
            #print(best_combi_matrix[i][c])
    return  best_combi_matrix[n][capacity]