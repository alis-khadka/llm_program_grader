class Queue:
    """Klasse, die eine selbstgebaute Queue darstellt.
    """

    def __init__(self):
        self.list = []


    def isEmpty(self):
        """Prueft, ob die Queue leer ist.
        :return: True, wenn die Queue leer ist;
            False, sonst
        """
        return len(self.list) == 0


    def head(self):
        """Gibt den Wert des ersten Elements in der Queue
            zurueck.
        :return: Den Wert des ersten Elementes in der Queue
        """
        return self.list[0]

    def enqueue(self, x):
        """Haengt ein Element an die Queue an.
        :param x: Anzuhaengendes Element
        """
        #pruef ob die schlange schon maximale Elemente enthaelt
        if len(self.list) >= 100:
            return "Overflow"
        else:
            self.list.append(x)
        #enqueue

        pass

    def dequeue(self):
        """Entfernt das erste Element aus der Queue
        :return: Erstes Element
        """
        output = self.list[0]
        del self.list[0]
        return output