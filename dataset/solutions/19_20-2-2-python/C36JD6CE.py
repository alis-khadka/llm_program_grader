def Calculator(inputarray, stack):
    for element in inputarray:
        if element == "+":
            a = stack.pop()
            b = stack.pop()
            c = b + a
            stack.push(c)
        elif element == "-":
            a = stack.pop()
            b = stack.pop()
            c = b - a
            stack.push(c)
        elif element == "*":
            a = stack.pop()
            b = stack.pop()
            c = b * a
            stack.push(c)
        elif element == "/":
            a = stack.pop()
            b = stack.pop()
            c = b / a
            stack.push(c)
        
        else:
            stack.push(int(element))
                
    return stack.pop()