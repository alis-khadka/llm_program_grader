class Queue:
    """Klasse, die eine selbstgebaute Queue darstellt.
    """
    def __init__(self):
        self.schlange = []
        self.headIdx = 0
        self.rearidx = 0
        
        
    def isEmpty(self):
        """Prueft, ob die Queue leer ist.
        :return: True, wenn die Queue leer ist;
            False, sonst
        """
        if self.headIdx == self.rearidx:
            return True
        else:
            return False

    def head(self):
        """Gibt den Wert des ersten Elements in der Queue
            zurueck.
        :return: Den Wert des ersten Elementes in der Queue
        """
        return self.schlange[int(self.headIdx)]

    def enqueue(self, x):
        """Haengt ein Element an die Queue an.
        :param x: Anzuhaengendes Element
        """
        self.schlange.append(x)
        self.rearidx +=1

    def dequeue(self):
        """Entfernt das erste Element aus der Queue
        :return: Erstes Element
        """
        tmp = self.schlange.pop(self.headIdx)
        self.rearidx -=1
        return tmp