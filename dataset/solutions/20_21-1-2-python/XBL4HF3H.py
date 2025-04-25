SENTINEL = float("inf")     # Wächter

def merge(A, l, q, r):
    n1 = q - l + 1          # die Länge des linken Teils
    n2 = r - q              # -"-           rechten
    L = [None] * (n1+1)     # leere Teil-Listen erstellen, +1 für den Wächter
    R = [None] * (n2+1)     # 
    for i in range(n1):
        L[i] = A[l+i]       # Teil-Listen befüllen
    for i in range(n2):
        R[i] = A[q + 1 + i] 
    L[n1] = SENTINEL        # Wächter hinzufügen
    R[n2] = SENTINEL
    i,j = 0,0               # Zähler für Teil-Listen
    for k in range(l, r+1): # r+1, damit mit den Wächtern verglichen wird
        if(L[i] <= R[j]):   # der eigentliche Merge-Teil
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergeSort(A, l, r):
    if(l < r):
        m = (l + r) // 2    # Mitte bestimmen 
        mergeSort(A, l, m)  # Rekursion für die linke Seite
        mergeSort(A, m+1, r)# Rekursion für die rechte Seite
        merge(A, l, m, r)   # Zusammenfügen der beiden Seiten
    
def solution(A):
    l = 0                   # Index für das erste
    r = len(A) - 1          # und das letzte Element
    mergeSort(A, l, r)      # mergeSort starten
    return A