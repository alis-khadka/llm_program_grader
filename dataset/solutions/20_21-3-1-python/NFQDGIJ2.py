import numpy as np
def knapSack(value, volume, capacity):
    len_vol = len(volume)
    assert len(value) == len_vol
    if capacity == 0 or len_vol == 0:
        return 0
    capacity += 1
    
    M = np.zeros((len_vol,capacity)) # initailisiere Matrix M     
    for v in range(len_vol):

        assert volume[v] == round(volume[v]) #Kontrolliert ob Volumen ganzzahlig ist
        
        for c in range(1,capacity):
            
            if volume[v] > c: #Gewicht zu Groß
                M[v,c] = M[v-1,c]
            else:
                
                if v == 0:
                    M[v,c] = value[v]
                else:
                    
                    M[v,c] = max(M[v-1,c],value[v] + M[v-1,c - volume[v]])
                    
    if int(M[len_vol-1,capacity-1]) == M[len_vol-1,capacity-1]:
        return int(M[len_vol-1,capacity-1])
    return M[len_vol-1,capacity-1]