def Calculator(inputarray, stack):
    for x in range(0,len(inputarray)):
        if inputarray[x] == "+":
            y = stack.pop()
            z = stack.pop()
            stack.push(z+y)
        elif inputarray[x] == "-":
            y = stack.pop()
            z = stack.pop()
            stack.push(z-y)
        elif inputarray[x] == "*":
            y = stack.pop()
            z = stack.pop()
            stack.push(z*y)
        elif inputarray[x] == "/":
            y = stack.pop()
            z = stack.pop()
            stack.push(z/y)
        else:
            y = int(inputarray[x])
            stack.push(y)
    
    return stack.pop()