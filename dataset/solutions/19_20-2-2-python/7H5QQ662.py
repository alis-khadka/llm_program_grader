def Calculator(inputarray, stack):
    x: int = 0
    y: int = 0
    
    for element in inputarray:
        if element == "*":
            x = stack.pop()
            y = stack.pop()
            stack.push(y*x)
        elif element == "/":
            x = stack.pop()
            y = stack.pop()
            stack.push(y/x)
        elif element == "+":
            x = stack.pop()
            y = stack.pop()
            stack.push(y+x)
        elif element == "-":
            x = stack.pop()
            y = stack.pop()
            stack.push(y-x)
        else:
            stack.push(int(element))
    return stack.pop()