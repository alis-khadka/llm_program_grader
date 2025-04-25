def calc(a,b):
    array = []
    for i in range(1, len(a)):
        a[i] += a[i-1]
    for pairs in b:
        if pairs[0] > 0:
            array.append(a[pairs[1]]-a[pairs[0]-1])
        else:
            array.append(a[pairs[1]])
            
    return array