def Calculator(inputarray, stack):
    for input in inputarray:
        input = str(input)
        if input == "+" or input == "-" or input == "*" or input == "/":
            i = stack.pop()
            j = stack.pop()
            stack.push(eval(str(j)+input+str(i)))
        else:
            stack.push(int(input))
    return stack.pop()