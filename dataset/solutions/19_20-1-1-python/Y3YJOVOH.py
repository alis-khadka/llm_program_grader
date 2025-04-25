def LCM(a, b):
  if (a<b):
      a, b = b, a
  kgv = 1
  x = 1
  tst =1
  while tst != 0:
      kgv = b*x
      tst = kgv % a
      x +=1
  return (kgv)