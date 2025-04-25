def calc(N, A):
    Results = [0 for i in range(N)] # Knoten i an der stelle i-1
    Vorgänger = [ [] for i in range(N)]   # Vorgängerliste von Knoten i steht an Stelle i-1
    for i in range(0, len(A)): # Laufzeit -> M
        element = A[i]
        Vorgänger[element[1]-1].append(element[0])   # füllt die Vorgängerliste jedes Knotens
    for i in range(0, N):     # Spaltenweise von links nach rechts durchwandern
        #print(i)
        #print(Results)
        if Vorgänger[i] != []:
            for v in Vorgänger[i]:
                Results[i] = max(Results[v-1] + 1, Results[i] )

    return(Results[N-1])