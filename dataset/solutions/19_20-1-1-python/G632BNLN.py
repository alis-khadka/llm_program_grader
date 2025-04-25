def LCM(a, b):
  x=a
  y=b
  r = x % y
  if x<y:
      x, y = y, x
  while r > 0:
    y = r
    r = x % y
  return((a*b)/y)