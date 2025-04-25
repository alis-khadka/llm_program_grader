class Queue:
    """Klasse, die eine selbstgebaute Queue darstellt.
    """
    
    def __init__(self):
        self.queue_items = []

    def isEmpty(self):
        """Prueft, ob die Queue leer ist.
        :return: True, wenn die Queue leer ist;
            False, sonst
        """
        return len(self.queue_items) is 0

    def head(self):
        """Gibt den Wert des ersten Elements in der Queue
            zurueck.
        :return: Den Wert des ersten Elementes in der Queue
        """
        return self.queue_items[0]

    def enqueue(self, x):
        """Haengt ein Element an die Queue an.
        :param x: Anzuhaengendes Element
        """
        if len(self.queue_items) >= 100:
            raise Exception('Queue too long')
        else:
            self.queue_items.append(x)

    def dequeue(self):
        """Entfernt das erste Element aus der Queue
        :return: Erstes Element
        """
        first_element = self.head()
        self.queue_items = self.queue_items[1:]
        return first_element