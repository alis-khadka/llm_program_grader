def opt(w) :

    size = len(w)
    maxW = [0] * (size+1)
    next = 0
    
    for i in range(1, size+1) :
         
        if i <= 2 :
            maxW[i] = max(maxW[i - 1], w[next])
    
        else :
            maxW[i] = max(maxW[i - 2] + w[next], maxW[i - 1])
        next += 1
     
    return maxW[size]