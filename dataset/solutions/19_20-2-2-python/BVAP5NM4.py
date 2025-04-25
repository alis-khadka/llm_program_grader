def Calculator(inputarray, stack):
    for i in range(len(inputarray)):
        if inputarray[i] not in "/*+-":
            stack.push(inputarray[i])
        if inputarray[i] in "/*+-":
            last = str(stack.pop())
            first = str(stack.pop())
            result = eval(first+inputarray[i]+last)
            stack.push(result)

    return result