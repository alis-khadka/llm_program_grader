def Calculator(inputarray, stack):
    
    for element in inputarray:
       
        if element != "-" and element != "+" and element != "*" and element != "/": 
            stack.push(int(element))
        else:
            right = stack.pop()
            left = stack.pop()           
            if element == '-':
                ergebnis = left - right
                
            if element == '+':
                ergebnis = left + right
            
            if element == '*':
                ergebnis = left * right
            
            if element == '/':
                ergebnis = left / right
            stack.push(ergebnis)

    return ergebnis