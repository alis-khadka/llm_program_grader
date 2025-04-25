def solution(A):
    if len(A) < 2:
        return A
    result = []          # moved!
    mid = int(len(A) / 2)
    y = solution(A[:mid])
    z = solution(A[mid:])
    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z[0])
            z.pop(0)
        else:
            result.append(y[0])
            y.pop(0)
    result += y
    result += z
    return result