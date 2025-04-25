def Calculator(inputarray, stack):
    for n in inputarray:
        if n == "+":
            y = int(stack.pop())
            x = int(stack.pop())
            stack.push(x+y)
        elif n == "-":
            y = int(stack.pop())
            x = int(stack.pop())
            stack.push(x-y)
        elif n == "*":
            y = int(stack.pop())
            x = int(stack.pop())
            stack.push(x*y)
        elif n == "/":
            y = int(stack.pop())
            x = int(stack.pop())
            stack.push(x/y)
        else:
            stack.push(int(n))
    return int(stack.pop())