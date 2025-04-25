def calc(n):
  return hoch(2, int(n), 1000000007) - 1


def hoch(a, b, c):
  a %= c
  result = 1
  while (b > 0):
    if ((b & 1) == 1):
      result = (result * a) % c
    a = (a * a) % c
    b = b >> 1
  return result