def opt(W):
    
    if len(W) == 0:  # keine Standorte
        return 0

    gewinn = []
    gewinn.append(W[0])
    gewinn.append(max(gewinn[0], W[1]))

    for i in range(2, len(W)):
        # vorheriger Wert wurde genommen
        if gewinn[i - 1] != gewinn[i - 2]:
            gewinn.append(max(gewinn[i - 1], gewinn[i - 2] + W[i]))
        else: # vorheriger Wert wurde nicht genommen
            gewinn.append(gewinn[i - 1] + W[i])

    return gewinn[len(W) - 1]