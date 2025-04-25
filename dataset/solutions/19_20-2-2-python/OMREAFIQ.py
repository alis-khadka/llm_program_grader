def Calculator(inputarray, stack):
  for x in inputarray:
    if x == '+':
      stack.push(stack.pop() + stack.pop())
    elif x == '-':
      stack.push(-stack.pop() + stack.pop())
    elif x == '*':
      stack.push(stack.pop() * stack.pop())
    elif x == '/':
      stack.push((1/stack.pop()) * stack.pop())
    else:
      stack.push(x)
  return stack.pop()