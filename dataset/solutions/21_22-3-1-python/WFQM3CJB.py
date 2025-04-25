def opt(W):
    result = [0,0]
    result[0] = W[0]
    if W[1] >= W[0]:
        result[1] = W[1]
    else:
        result[1] = W[0]
    for i in range(2,len(W)):
        if result[i-2] + W[i] >= result[i-1]:
            result.append(result[i-2] + W[i])
        else:
            result.append(result[i-1])
    return result[len(result)-1]