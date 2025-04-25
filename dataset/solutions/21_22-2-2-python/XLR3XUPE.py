import copy

def calc(a_,b):
    d = [0] * len(b)
    a = copy.deepcopy(a_)
    for i in range(1, len(a)):
        a[i] += a[i-1]
    for i in range(len(b)):
        if(b[i][0] == 0):
            d[i]=a[b[i][1]]
        else:
            d[i]= a[b[i][1]] - a[b[i][0] - 1]
    return d