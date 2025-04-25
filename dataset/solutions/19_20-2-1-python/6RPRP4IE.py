class Queue:
    """Klasse, die eine selbstgebaute Queue darstellt.
    """
    def __init__(self):
        self.queue =list()
        self.maxSize = 100
        self.start = 0
        self.rear = 0

    def isEmpty(self):
        """Prueft, ob die Queue leer ist.
        :return: True, wenn die Queue leer ist;
            False, sonst
        """
        if(self.start==self.rear):
            return True
        return False

    def head(self):
        """Gibt den Wert des ersten Elements in der Queue
            zurueck.
        :return: Den Wert des ersten Elementes in der Queue
        """
        x = self.queue[self.start]
        return x

    def enqueue(self, x):
        """Haengt ein Element an die Queue an.
        :param x: Anzuhaengendes Element
        """
        if(self.size() >= self.maxSize):
            return ("Queue full")
        self.queue.append(x)
        self.rear+=1

    def dequeue(self):
        """Entfernt das erste Element aus der Queue
        :return: Erstes Element
        """
        if(self.size() <= 0):
            self.resetQueue()
            return ("Queue Empty")
        x = self.queue[self.start]
        self.start+=1
        return x
        
    def size(self):
        return self.rear - self.start
        
    def resetQueue(self):
        self.rear = 0
        self.start = 0
        self.queue = list()