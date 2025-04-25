def Calculator(inputarray, stack):
    for x in inputarray:
        try:
            c=int(x)
        except:
            b = stack.pop()
            a = stack.pop()
            if x == "+":
                c = a + b
            elif x == "-":
                c = a - b
            elif x == "*":
                c = a * b
            elif x == "/":
                c = a / b
        stack.push(c)
    return stack.pop()