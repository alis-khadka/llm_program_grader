class Queue:
    def __init__(self):
        self.myArray = []

    def isEmpty(self):
        return not bool(self.myArray)

    def head(self):
        return self.myArray[-1]

    def enqueue(self, x):
        return self.myArray.insert(0,x)
        
    def dequeue(self):
        return self.myArray.pop()