def calc(f):
  if f(1):
    return 1
  if f(2):
    return 2
    
  zweierpotenz = 1
  zaehler = 0
  return recursion(f, zweierpotenz, zaehler)


def recursion(f, zweierpotenz, zaehler):
  if f(zweierpotenz):
    interval = [2**(zaehler - 1), 2**zaehler]
    return recursion2(f, interval)
  else:
    zweierpotenz *= 2
    zaehler += 1
    return recursion(f, zweierpotenz, zaehler)


def recursion2(f, interval):
  middle = (interval[0] + interval[1]) // 2

  if f(middle):
    if not f(middle - 1):
      return middle
    return recursion2(f, [interval[0], middle])
  else:
    return recursion2(f, [middle, interval[1]])