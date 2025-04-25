class Queue:
    """Klasse, die eine selbstgebaute Queue darstellt.
    """
    def __init__(self):
        self.elements: list = list()

    def isEmpty(self):
        """Prueft, ob die Queue leer ist.
        :return: True, wenn die Queue leer ist;
            False, sonst
        """
        if len(self.elements) == 0:
            return True
        return False

    def head(self):
        """Gibt den Wert des ersten Elements in der Queue
            zurueck.
        :return: Den Wert des ersten Elementes in der Queue
        """
        if len(self.elements) > 0:
            return self.elements[0]
        else:
            raise IndexError

    def enqueue(self, x):
        """Haengt ein Element an die Queue an.
        :param x: Anzuhaengendes Element
        """
        if len(self.elements) < 100:
            self.elements.append(x)
        else:
            raise IndexError

    def dequeue(self):
        """Entfernt das erste Element aus der Queue
        :return: Erstes Element
        """
        if len(self.elements) > 0:
            return self.elements.pop(0)
        else:
            raise IndexError