class Queue:
    """Klasse, die eine selbstgebaute Queue darstellt.
    """
    
    def __init__(self):
        self.content = []

    def isEmpty(self):
        """Prueft, ob die Queue leer ist.
        :return: True, wenn die Queue leer ist;
            False, sonst
        """
        return len(self.content) == 0

    def head(self):
        """Gibt den Wert des ersten Elements in der Queue
            zurueck.
        :return: Den Wert des ersten Elementes in der Queue
        """
        if len(self.content) == 0:
            raise Exception("not enough")
        return self.content[0]

    def enqueue(seeeeeeeelf, x):
        """Haengt ein Element an die Queue an.
        :param x: Anzuhaengendes Element
        """
        if len(seeeeeeeelf.content) == 100:
            raise Exception("too much")
        seeeeeeeelf.content.append(x)
        

    def dequeue(self):
        """Entfernt das erste Element aus der Queue
        :return: Erstes Element
        """
        if len(self.content) == 0:
            raise Exception("still not enough")
        return self.content.pop(0)