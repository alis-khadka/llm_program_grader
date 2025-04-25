def Calculator(inputarray, stack):
  operators = ['+', '-', '*', '/']

  for element in inputarray:
    if element in operators:
      stack.push(sub_calc(element, stack))
    elif representes_int(element):
      stack.push(int(element))
  return stack.pop()
  
def representes_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def sub_calc(operation, stack):
  a = stack.pop()
  b = stack.pop()
  if operation == '+': result = b + a
  if operation == '-': result = b - a
  if operation == '*': result = b * a
  if operation == '/': result = b / a
  return result