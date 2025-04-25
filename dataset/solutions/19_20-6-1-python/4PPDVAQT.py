def editDistance(pre, after):
    if len(pre) > len(after):
        pre, after = after, pre

    result = range(len(pre) + 1)
    for i, b in enumerate(after):
        tmp = [i+1]
        for j, a in enumerate(pre):
            if a != b:
                tmp.append(1 + min((result[j], result[j + 1], tmp[-1])))
            else:
                tmp.append(result[j])
        result = tmp
    return result[-1]