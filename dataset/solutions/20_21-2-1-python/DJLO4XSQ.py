def calc(A, B):
    items = [0] * (len(B))
    output = ''
    for category in A:
        items[category] += 1
    for index, capacity in enumerate(B):
        if items[index] <= capacity:
            output += '1'
        else:
            output += '0'

    return output