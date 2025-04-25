def Operation(x,y,operator):
    if operator == '+':
        return (x+y)
    elif operator == '-':
        return (x-y)
    elif operator == '*':
        return (x*y)
    elif operator == '/':
        return (x/y)

def Calculator(inputarray, stack):
    for value in inputarray:
        try:
            stack.push(int(value))
        except ValueError:
            pass  
        if (value == '+' or value == '-' or value == '*' or value == '/'): 
            y = int(stack.head())
            stack.pop()
            x = int(stack.head())
            stack.pop()
            stack.push(Operation(x,y,value))
    result = stack.head()
    return (result)