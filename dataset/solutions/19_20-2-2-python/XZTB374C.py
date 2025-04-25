def Calculator(inputarray, stack):
    while len(inputarray) > 0:
        if inputarray[0] == "-":
            a = stack.pop()
            b = stack.pop()
            stack.push(b - a)
        elif inputarray[0] == "+":
            a = stack.pop()
            b = stack.pop()
            stack.push(a + b)
        elif inputarray[0] == "*":
            a = stack.pop()
            b = stack.pop()
            stack.push(a * b)
        elif inputarray[0] == "/":
            a = stack.pop()
            b = stack.pop()
            stack.push(b / a)
        else:
            stack.push(int(inputarray[0]))
        inputarray.pop(0)
    return stack.head()