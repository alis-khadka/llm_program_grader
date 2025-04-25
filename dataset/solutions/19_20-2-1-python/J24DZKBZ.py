class Queue():
    def __init__(self):
        self.snake = [None]*101
        self.__head = 1
        self.rear = 1 
    def isEmpty(self):
        if self.__head == self.rear:
            return (True)
        else:
            return(False)

    def head(self):
        return(self.snake[self.__head])

    def enqueue(self, x):
        self.snake[self.rear] = x
        self.rear = (self.rear % 100) + 1

    def dequeue(self):
        self.__head += 1
        return(self.snake[self.__head-1])