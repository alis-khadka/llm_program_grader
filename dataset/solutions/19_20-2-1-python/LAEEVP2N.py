class Queue:
    """Klasse, die eine selbstgebaute Queue darstellt.
    """
    def __init__(self):
        self.queue = [];

    def isEmpty(self):
        """Prueft, ob die Queue leer ist.
        :return: True, wenn die Queue leer ist;
            False, sonst
        """
        if len(self.queue) == 0:
            return True;
        return False;

    def head(self):
        """Gibt den Wert des ersten Elements in der Queue
            zurueck.
        :return: Den Wert des ersten Elementes in der Queue
        """
        if self.isEmpty():
            print("Queue is empty");
        else:
            return self.queue[0];

    def enqueue(self, x):
        """Haengt ein Element an die Queue an.
        :param x: Anzuhaengendes Element
        """
        self.queue.append(x);

    def dequeue(self):
        """Entfernt das erste Element aus der Queue
        :return: Erstes Element
        """
        return self.queue.pop(0);