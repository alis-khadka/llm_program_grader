class Queue:
    def __init__(self):
        self.front = self.size = self.rear = 0
        self.Q = [None]*100
        

    def isEmpty(self):
        if self.size == 0:
            return (True)
        else:
            return (False)
        
    def head(self):
        return self.Q[self.front]
        
    def enqueue(self, item):
        if self.Q[self.front] == None:
            self.Q[self.front]=item
            self.size=self.size+1
        elif self.rear == 99:
            self.rear=0
            self.Q[self.rear]=item
            self.size=self.size+1
        else:
            self.rear = self.rear + 1
            self.Q[self.rear]=item
            self.size = self.size + 1
            
    def dequeue(self):
        self.front = self.front + 1
        self.size = self.size - 1
        return(self.Q[self.front - 1])