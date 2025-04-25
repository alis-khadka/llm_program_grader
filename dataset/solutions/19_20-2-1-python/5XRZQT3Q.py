class Queue:
 def __init__(self):
  self.array = []
 def isEmpty(self):
  return len(self.array) == 0
 def head(self):
  return self.array[0]
 def enqueue(self, x):
  self.array.append(x)
 def dequeue(self):
  return self.array.pop(0)