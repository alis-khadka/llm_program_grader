def calc(A,B):
    n = len(A)
    m = len(B)
    kategorie = [0] * (m)
    result = ''
    for geschenk in A:
        kategorie[geschenk] += 1
    for i in range(m):
        if(kategorie[i] <= B[i]):
            result += '1'
        else:
            result += '0'
    return result