def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)

    # Matrix mit leeren Einträgen, die im Verlauf "entwickelt" werden
    knapsack = [[0 for x in range(capacity + 1)] for x in range(len(value) + 1)]

    # für alle möglichen Werte [0, N]
    for i in range(len(value) + 1):
        # für alle Kapazitäten [0, capacity]
        for vol in range(capacity + 1):
            # Wert = 0 oder momentane Kapazität = 0: 0
            if i == 0 or vol == 0:
                knapsack[i][vol] = 0

            # falls Volumen des vorheringen Objekts <= momentanes Volumen
            elif volume[i - 1] <= vol:
                knapsack[i][vol] = max(
                    value[i - 1] + knapsack[i - 1][vol - volume[i - 1]],
                    knapsack[i - 1][vol],
                )
            else:
                # falls >= speichere vorheringen Wert im jetzigen Index
                knapsack[i][vol] = knapsack[i - 1][vol]

    # letzter Eintrag ist größmöglicher Gewinn
    return knapsack[len(value)][capacity]