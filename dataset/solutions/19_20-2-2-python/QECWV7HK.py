def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def Calculator(inputarray, stack):
    for i in inputarray:
        if(isDigit(i)):
            stack.push(int(i))
        else:
            b = stack.pop()
            a = stack.pop()
            if(i == "+"):
                stack.push(a+b)
            elif(i == "-"):
                stack.push(a-b)
            elif(i == "*"):
                stack.push(a*b)
            elif(i == "/"):
                stack.push(a/b)
    return stack.pop()