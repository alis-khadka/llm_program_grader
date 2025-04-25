def calc(A,B):
    n = len(A) # O(1) Kardinalität der Geschenke
    m = len(B) # O(1) Kapazität
    s = [0] * m # O(1)
    count = [0] * (n + m + 1) #O(1)

    for j in range(n): # O(n)
        count[A[j]] = count[A[j]] + 1 #O(1)
    #print("Counting_List", count)
    
    for i in range(m): #O(m)
        if count[i] <= B[i]: #O(1)
            s[i] = 1 #O(1)
    new_s = "".join(str(s[i]) for i in range(m)) #O(m2)
    return new_s # Output: Ein binärer String s der Länge m ==> O(m) + O(m2) + O(n) = O(m + m2 + n)