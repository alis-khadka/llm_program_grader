def LCM(a, b):
  return int(a*b/GCD(a,b))

def GCD(a,b):
  if a%b == 0:
    return b
  else:
    new_a = b
    new_b = a%b
    return GCD(new_a, new_b)