def solution(A):
    if len(A) > 1:

        # Finding the mid of the array
        mid = len(A) // 2

        # Dividing the array elements
        L = A[:mid]

        # into 2 halves
        R = A[mid:]

        # Sorting the first half
        solution(L)

        # Sorting the second half
        solution(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
            
        return A
    pass