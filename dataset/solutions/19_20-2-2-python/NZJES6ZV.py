def Calculator(inputarray, stack):
    for c in inputarray:
        num = None
        operand = None
        try:
            num = int(c)
            stack.push(num)
            
        except ValueError:
            operand = c
            num2 = stack.pop()
            num1 = stack.pop()
            result = None
            if operand == '+':
                result = num1 + num2
            elif operand == '-':
                result = num1 - num2
            elif operand == '*':
                result = num1 * num2
            elif operand == '/':
                result = num1 // num2
            
            stack.push(result)
    return stack.pop()