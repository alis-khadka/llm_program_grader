def knapSack(value, volume, kap):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)

    Matrix = [[0]*(kap+1) for i in range(len(value)+1)]

    for i, j in enumerate(volume, 1):
        for weight in  range(1, kap+1):
            if j > weight:
                Matrix[i][weight]=Matrix[i-1][weight]
            else:
                Matrix[i][weight]= max(Matrix[i-1][weight], Matrix[i-1][weight-j]+value[i-1])
    #Zurückgabe der letzten Stelle der Matrix
    return Matrix[len(volume)][kap]