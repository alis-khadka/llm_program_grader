def opt(values):
    value_array = [0] * len(values)
    value_array[0] = values[0]
    value_array[1] = values[1]

    for i in range(1,len(values)):
        if value_array[i-1] > values[i] + value_array[i-2]:
            value_array[i] = value_array[i-1]
        else: 
            value_array[i] = values[i] + value_array[i-2]

    return(value_array[-1])