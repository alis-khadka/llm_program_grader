def calc(A,B):
    c = dict()
    ans = ""
    for a in A:
        if a not in c.keys():
            c[a] = 0
        c[a] += 1
    for i, b in enumerate(B):
        if i not in c.keys() or c[i] <= b:
            ans += "1"
        else:
            ans += "0"
            
    return ans