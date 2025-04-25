def calc(A,B):
    anzahl_treffer = [0] * len(B)
    for zahl in A:
        anzahl_treffer[zahl] += 1
    
    result = ""
    for i in range(len(B)):
        if anzahl_treffer[i] <= B[i]:
            result += "1"
        else:
            result += "0"
    return result