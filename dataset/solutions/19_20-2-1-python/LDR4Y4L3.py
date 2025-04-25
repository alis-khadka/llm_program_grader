class Queue:
    """Klasse, die eine selbstgebaute Queue darstellt.
    """
    def __init__(self):
        self.array = []


    def isEmpty(self):
        """Prueft, ob die Queue leer ist.
        :return: True, wenn die Queue leer ist;
            False, sonst
        """
        if self.array == []:
            return True
        else: 
            return False

    def head(self):
        """Gibt den Wert des ersten Elements in der Queue
            zurueck.
        :return: Den Wert des ersten Elementes in der Queue
        """
        if self.isEmpty() == False:    
            return self.array[-1]

    def enqueue(self, x):
        """Haengt ein Element an die Queue an.
        :param x: Anzuhaengendes Element
        """
        self.array.insert(0, x)

    def dequeue(self):
        """Entfernt das erste Element aus der Queue
        :return: Erstes Element
        """
        #-1 = last element
#        lastElement = self.array[-1]
        return self.array.pop(-1)
#         lastElement
        
    def show(self):
  
        print(self.array)