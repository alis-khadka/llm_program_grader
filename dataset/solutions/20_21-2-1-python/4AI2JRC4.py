def calc(values, limits):
    amount = [0] * len(limits)

    for value in values:
        amount[value] += 1

    result = ''
    for i in range(len(limits)):
        result += '0' if amount[i] > limits[i] else '1'

    return result