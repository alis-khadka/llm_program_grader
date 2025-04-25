def Calculator(inputarray, stack):
    for x in inputarray:
        if x not in ["+", "-", "*", "/"]:
            stack.push(int(x));
        elif x == "+":
            stack.push(stack.pop() + stack.pop());
        elif x == "-":
            stack.push(- stack.pop() + stack.pop());
        elif x == "*":
            stack.push(stack.pop() * stack.pop());
        elif x == "/":
            tmp = stack.pop()
            stack.push(int(stack.pop() / tmp));
    return stack.head();