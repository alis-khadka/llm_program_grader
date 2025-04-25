def editDistance(a, b):
    
    # gernerieren des zweidimensionalen Arrays zur Berechnung:
    
    array1 = []  # horizontale
    array2 = [None, None]  # vertikale
    
    for char in b:
        array2.append(char)

    array1.append(array2)
    array1.append([None])
    for i in range(len(array2)-1):  # hinzufügen der Nummern in der Vertikalen
        array1[1].append(i)
    
    j = 1
    for char in a:  # hinzufügen des Strings a und den Nummern in der horizontalen
        array1.append([None for i in range(len(array2))])
        array1[j+1][0] = char
        array1[j+1][1] = j 
        j = j + 1
        

    v = 2  # vertikaler Zähler
    h = 2  # horizontaler Zähler
    # Berechnung der Felder im Array
    while h <= len(array1) - 1:
        while v <= len(array1[0]) - 1:
            if array1[h][0] == array1[0][v]:
                array1[h][v] = array1[h-1][v-1]
            else:
                array1[h][v] = min(array1[h-1][v-1], array1[h][v-1], array1[h-1][v]) + 1 
            v = v + 1
        v = 2
        h = h + 1
    
    return array1[len(array1) - 1][len(array1[0]) - 1]  # das Feld in der linken unteren Ecke ist das Ergebnis