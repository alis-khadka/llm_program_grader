class Queue(list):
    first = 0
    rear = 0
    """Klasse, die eine selbstgebaute Queue darstellt.
    """
    
    def isEmpty(self):
        if (self.first == self.rear):
            return True
        else:
            return False
        """Prueft, ob die Queue leer ist.
        :return: True, wenn die Queue leer ist;
            False, sonst
        """
        pass

    def head(self):
        return(self[self.first])
        """Gibt den Wert des ersten Elements in der Queue
            zurueck.
        :return: Den Wert des ersten Elementes in der Queue
        """
        pass

    def enqueue(self, x):
        if ((self.rear + 1) % 101 == self.first):
            print("Overflow!")
            return
        else:
            self.append(x)
            self.rear = (self.rear + 1) % 101
        """Haengt ein Element an die Queue an.
        :param x: Anzuhaengendes Element
        """
        pass

    def dequeue(self):
        if (self.first == self.rear):
            print("Underflow!")
            return
        else:
            x = self[self.first]
            self.first = (self.first + 1) % 101
            return x
        """Entfernt das erste Element aus der Queue
        :return: Erstes Element
        """
        pass