def Calculator(inputarray, stack):
    i = 0
    erg = 0
    for  e in inputarray:
        if not (e == '+' or e =='-' or e=='*' or e=='/'):
            stack.push(int(e))
        else:
            if e == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.push(num1 + num2)
            elif e == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.push(num1 - num2)
            elif e == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.push(num1 * num2)
            elif e == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.push(num1 / num2)
    return stack.head()