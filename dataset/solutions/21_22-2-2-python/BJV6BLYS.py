def calc(a,b):
    c= [0]*(len(a)+1)
    for i in range(len(a)):
        c[i+1]=c[i]+a[i]
    return [c[i[1]+1]-c[i[0]] for i in b]