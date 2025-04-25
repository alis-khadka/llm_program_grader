def Calculator(inputarray, stack = []):
    inputarray = list(reversed(inputarray))
    # print(inputarray)
    ops = {'+': lambda x, y: x + y,
          '-': lambda x, y: x - y,
          '*': lambda x, y: x * y,
          '/': lambda x, y: x / y}
    while len(inputarray) != 0:
        current_element = inputarray.pop()
        # print(current_element)
        
        if current_element in ops.keys():
    
          # print("emptystack",stack.emptystack())
          if not stack.emptystack():
                second_num = stack.pop()
                # print('first:', first_num)
                first_num = stack.pop()
                # print('second :',second_num)
                result = ops[current_element](first_num,second_num)
                stack.push(result)
          else:
              print('there is nothing in stack')
              return 0
        else: 
          stack.push(int(current_element))
          # print(stack)

    return stack.pop()