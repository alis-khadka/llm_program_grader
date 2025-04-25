class Queue:
    """Klasse, die eine selbstgebaute Queue darstellt.
    """

    def __init__(self):
        self.list = []
        self.firstElement = 0
        self.firstEmpty = 0
        self.maxLength = 150

    def isEmpty(self):
        """Prueft, ob die Queue leer ist.
        :return: True, wenn die Queue leer ist;
            False, sonst
        """
        return self.firstElement == self.firstEmpty

    def isFull(self):
        x = self.__loopIndex(self.firstEmpty + 1)
        return x == self.firstElement

    def head(self):
        """Gibt den Wert des ersten Elements in der Queue
            zurueck.
        :return: Den Wert des ersten Elementes in der Queue
        """
        if not self.isEmpty():
            return self.list[self.firstElement]
        else:
            print("The Queue is empty.")

    def enqueue(self, x):
        """Haengt ein Element an die Queue an.
        :param x: Anzuhaengendes Element
        """
        if not self.isFull():
            if len(self.list) < self.maxLength + 1:
                self.list.append(x)
                self.firstEmpty += 1
            else:
                self.list[self.firstEmpty] = x
                self.firstEmpty += 1
            
            self.firstEmpty = self.__loopIndex(self.firstEmpty)
        else:
            print("Cannot enqueue to a full Queue.")

    def dequeue(self):
        """Entfernt das erste Element aus der Queue
        :return: Erstes Element
        """
        if not self.isEmpty():
            x = self.list[self.firstElement]
            self.firstElement += 1
            self.firstElement = self.__loopIndex(self.firstElement)
            return x
        else:
            print("Cannot dequeue from an empty Queue.")

    def __loopIndex(self, i):
        if i == self.maxLength + 1:
            i = 0
        return i