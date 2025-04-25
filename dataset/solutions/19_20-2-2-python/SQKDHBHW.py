def Calculator(inputarray, stack):
  for x in inputarray:
    if x == '+':
      stack.push(stack.pop() + stack.pop())
    elif x == '-':
      stack.push(-stack.pop() + stack.pop())
    elif x == '*':
      stack.push(stack.pop() * stack.pop())
    elif x == '/':
      a = stack.pop()
      stack.push(stack.pop() / a)
    else:
      stack.push(x)
  return stack.pop()