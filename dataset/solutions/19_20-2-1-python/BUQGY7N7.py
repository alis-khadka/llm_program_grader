class Queue:
    """Klasse, die eine selbstgebaute Queue darstellt.
    """

    def __init__(self):
        self._queue = []

    def isEmpty(self):
        """Prueft, ob die Queue leer ist.
        :return: True, wenn die Queue leer ist;
            False, sonst
        """
        if len(self._queue) == 0:
            return True
        else:
            return False

    def head(self):
        """Gibt den Wert des ersten Elements in der Queue
            zurueck.
        :return: Den Wert des ersten Elementes in der Queue
        """
        return self._queue[0]

    def enqueue(self, x):
        """Haengt ein Element an die Queue an.
        :param x: Anzuhaengendes Element
        """
        self._queue.append(x)

    def dequeue(self):
        """Entfernt das erste Element aus der Queue
        :return: Erstes Element
        """
        return self._queue.pop(0)