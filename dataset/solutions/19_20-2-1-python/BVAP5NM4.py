class Queue:
    """Klasse, die eine selbstgebaute Queue darstellt.
    """

    def __init__(self):
        self.maxe = 100
        self.arr = list()

    def isEmpty(self):
        """Prueft, ob die Queue leer ist.
        :return: True, wenn die Queue leer ist;
            False, sonst
        """
        if len(self.arr) == 0:
            return True
        else:
            return False

    def head(self):
        """Gibt den Wert des ersten Elements in der Queue
            zurueck.
        :return: Den Wert des ersten Elementes in der Queue
        """
        if self.isEmpty():
            return 'Error, Queue is empty'
        else:
            return self.arr[0]

    def enqueue(self, x):
        """Haengt ein Element an die Queue an.
        :param x: Anzuhaengendes Element
        """
        if len(self.arr) == self.maxe:
            return 'Error: Queue overflow'
        else:
            self.arr.append(x)

    def dequeue(self):
        """Entfernt das erste Element aus der Queue
        :return: Erstes Element
        """
        if self.isEmpty():
            return 'Queue is empty'
        else:
            first = self.arr.pop(0)
            return first