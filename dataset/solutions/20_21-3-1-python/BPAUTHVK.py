def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)

    #Baue 2D Array für die Zwischenschritte
    Results = [[0 for i in range(capacity + 1)] for j in range(len(value) + 2)]
    #print (Results)
    for i in range(1 , len(value)+1): # geht die verschiedenen Elemente durch
        #print (i)
        for j in range(1 , capacity+1): # geht die verschiedenen Gewichte durch
            #print (j)
            if j < volume[i - 1]:
                 Results[i][j] = Results[i - 1][j]
            else:
                Results[i][j] = max(Results[i - 1][j] , value[i-1] + Results[i-1][ j - volume[i-1] ])
            #print (Results)



    return Results[len(value)][capacity]