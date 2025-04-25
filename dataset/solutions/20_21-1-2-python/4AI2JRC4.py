def solution(A):
    mergeSrt(A)
    return A

def mergeSrt(arr):
    if len(arr) > 1:
        # Mitte finden
        mid = len(arr)//2
    
        # Divide (and conquer later)
        L = arr[:mid]
        R = arr[mid:]
    
        # Rekursions-Fun (teile und s0rtiere Hälften)
        mergeSrt(L)
        mergeSrt(R)
    
        i = j = k = 0
    
        # Merge
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
    
        # Fehlende Elemente hinzufügen
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
    
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1