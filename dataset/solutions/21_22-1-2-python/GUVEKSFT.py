def calc(f):
    upper = int(1e18)
    lower = 0
    while True:
        test_val = ((upper - lower) // 2) + lower
        if f(test_val): #N ist kleiner oder gleich test_n
            upper = test_val
        else: #N ist größer 
            lower = test_val
        if upper - lower == 1:
            return upper