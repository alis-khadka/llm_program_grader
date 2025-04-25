def Calculator(inputarray, stack):
    i = 0
    for i in inputarray:
        if i == "-":
            a = stack.pop()
            b = stack.pop()
            c = b - a
            stack.push(c)
        elif i == "+":
            a = stack.pop()
            b = stack.pop()
            c = b + a
            stack.push(c)
        elif i == "/":
            a = stack.pop()
            b = stack.pop()
            c = b / a
            stack.push(c)
        elif i == "*":
            a = stack.pop()
            b = stack.pop()
            c = b * a
            stack.push(c)
        else:
            stack.push(i)
    return stack.pop()