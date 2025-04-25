class Queue:
    """Klasse, die eine selbstgebaute Queue darstellt.
    """
    def __init__(self):
         self.queue = []
         
    def isEmpty(self):
        """Prueft, ob die Queue leer ist.
        :return: True, wenn die Queue leer ist;
            False, sonst
        """
        if(len(self.queue)< 1): return True
        
        return False
        
    def head(self):
        """Gibt den Wert des ersten Elements in der Queue
            zurueck.
        :return: Den Wert des ersten Elementes in der Queue
        """
        return self.queue[0]
        pass

    def enqueue(self,x):
        """Haengt ein Element an die Queue an.
        :param x: Anzuhaengendes Element
        """
        return self.queue.insert(len(self.queue), x)        

    def dequeue(self):
        """Entfernt das erste Element aus der Queue
        :return: Erstes Element
        """
        if(len(self.queue) < 1):return None
        
        return self.queue.pop(0)