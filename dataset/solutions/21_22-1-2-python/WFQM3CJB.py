def calc(f):
    obereGrenze = 10e18
    untereGrenze = 1
    n = int((untereGrenze+obereGrenze)//2)
    while not (f(n) and not f(n-1)):
        n = int((untereGrenze+obereGrenze)//2)
        if f(n):
            obereGrenze = int(n)
        else:
            untereGrenze = int(n+1)
    return int(n)

#works if N < initial n value / mid(grenzen)