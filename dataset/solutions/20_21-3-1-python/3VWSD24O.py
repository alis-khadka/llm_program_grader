import numpy as np

def knapSack(values, weights, knapsackWeight):
    assert len(values) == len(weights)
    for x in weights:
        assert x == round(x)
    n = len(weights)
    A = np.zeros((n+1,knapsackWeight+1))
    
    for i in range(1,n+1):
        for w in range(1, knapsackWeight+1):
            if weights[i-1]>w:
                A[i,w] = A[i-1,w]
            else:
                a1 = A[i-1,w]
                a2 =  values[i-1] + A[i - 1, int(w - weights[i-1])]
                A[i,w] = max(a1, a2)
    answer = A[n, knapsackWeight]
    if int(answer) == answer:
        return int(answer)
    else:
        return answer