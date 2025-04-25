def calc(A, B) -> str:
    result = ""
    occurences = {}
    for i in A:
        occurences[i] = occurences.get(i, 0) + 1

    for idx, val in enumerate(B):
        result += "0" if occurences.get(idx, 0) > val else "1"
    return result