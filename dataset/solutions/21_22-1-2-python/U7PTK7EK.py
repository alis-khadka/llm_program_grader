def calc(binary_func):
    upper_border = 10**18 + 1
    lower_border = 1 - 1
    
    while True:

        middle = (upper_border + lower_border) // 2
        result = binary_func(middle)
        
        if result == True:
            upper_border = middle
            
        elif result == False:
            lower_border = middle

        if upper_border - lower_border <= 1:
            return upper_border