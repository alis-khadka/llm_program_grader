class Queue:
    MAX_SIZE = 101
    def __init__(self):
      self._arr = [None] * Queue.MAX_SIZE
      self._start = 0
      self._end = 0
    
    def isEmpty(self):
        return self._start == self._end

    def head(self):
        return self._arr[self._start]

    def enqueue(self, x):
        if (self._end + 1) % Queue.MAX_SIZE == self._start:
          raise Exception('overflow')

        self._arr[self._end] = x
        self._end = (self._end + 1) % Queue.MAX_SIZE

    def dequeue(self):
      if self.isEmpty():
        raise Exception('underflow')

      e = self._arr[self._start]
      self._start = (self._start + 1) % Queue.MAX_SIZE
      return e