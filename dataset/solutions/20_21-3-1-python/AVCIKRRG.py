def knapSack(value, volume, capacity):
    assert len(value) == len(volume)

    for x in volume:
        assert x == round(x)

    table = []

    for i in range(0, len(value)+1):
        table.append([])
        for j in range(0, capacity+1):
            table[i].append(0)
    
    for item in range(0, len(value)):
        for weight in range(0, capacity+1):
            if volume[item] <= weight:
                if weight - volume[item] > 0:
                    table[item+1][weight] = max(value[item] + table[item][weight - volume[item]], table[item][weight])
                elif value[item] >= table[item][weight]:
                    table[item+1][weight] = value[item]
                else: 
                    table[item+1][weight] = table[item][weight]
            else:
                table[item+1][weight] = table[item][weight]

    return table[len(value)][capacity]