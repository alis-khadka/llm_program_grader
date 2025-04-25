class Queue:
    """Klasse, die eine selbstgebaute Queue darstellt.
    """

    
    def __init__(self):
        self.MAX = 100
        self.h = 0
        self.r = 0
        self.queue = [None]*self.MAX
    
    def isEmpty(self):
        """Prueft, ob die Queue leer ist.
        :return: True, wenn die Queue leer ist;
            False, sonst
        """
        if self.h == self.r:
            return True
        else:
            return False

    def head(self):
        """Gibt den Wert des ersten Elements in der Queue
            zurueck.
        :return: Den Wert des ersten Elementes in der Queue
        """
        
        return self.queue[self.h]

    def enqueue(self, x):
        """Haengt ein Element an die Queue an.
        :param x: Anzuhaengendes Element
        """
        if not (self.r + 1) % self.MAX == self.h:
            self.queue[self.r] = x
            self.r = (self.r + 1) % self.MAX

    def dequeue(self):
        """Entfernt das erste Element aus der Queue
        :return: Erstes Element
        """
        if not self.isEmpty():
            item = self.queue[self.h]
            self.h = (self.h + 1) % self.MAX
        return item