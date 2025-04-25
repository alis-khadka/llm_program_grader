def Calculator(inputarray, stack):
    
    a = inputarray
    
    for i in range(0,len(a)):
        try:
            stack.push(int(a[i]))
        except ValueError:
            y = stack.pop()
            x = stack.pop()
            if a[i] == "+":
                stack.push(x+y)
            elif a[i] == "-":
                stack.push(x-y)
            elif a[i] == "*":
                stack.push(x*y)
            elif a[i] == "/":
                stack.push(x/y)
            else: 
                raise ValueError("Invalid string in inputarray.")
                
    result = str(stack.pop())
    
    if not stack.emptystack():
        raise ValueError("Incomplete calculation in inputarray.")
        
    return result