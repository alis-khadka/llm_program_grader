class Queue:
	def __init__(self):
		self.length = 101
		self.mem = [None]*self.length
		self.first = 0
		self.last = 0

	def isEmpty(self):
		return self.first == self.last 

	def head(self):
		return self.mem[self.first]

	def enqueue(self, x):
		if ((self.last + 1) % self.length) == self.first:
			raise BufferError('Queue is full')
		else:
			self.mem[self.last] = x
			self.last = (self.last + 1) % self.length

	def dequeue(self):
		if self.first == self.last:
			 raise BufferError('Queue is empty')
		else:
			item = self.mem[self.first]
			self.mem[self.first] = None
			self.first = (self.first + 1) % self.length
			return item