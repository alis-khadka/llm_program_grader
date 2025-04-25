class Queue:
    """Klasse, die eine selbstgebaute Queue darstellt.
    """
    
    def __init__(self):
        """initialisiert die Schlange
        """
        #interne Darstellung der Schlange leere Liste Q initialisieren
        self.Q = []
        
        #Länge der Schlange als 0 initialisieren:
        self.length = 0

    def isEmpty(self):
        """Prueft, ob die Queue leer ist.
        :return: True, wenn die Queue leer ist;
            False, sonst
        """ 
        # die Schlange ist leer wenn sie eine Länge von 0 hat:
        if self.length == 0:
            return True
        else:
            return False

    def head(self):
        """Gibt den Wert des ersten Elements in der Queue
            zurueck.
        :return: Den Wert des ersten Elementes in der Queue
        """
        if self.length == 0:
            return None # None zurückgeben, wenn die Schlange leer ist
        else:
            return self.Q[0] # ansonsten das erste Listenelement zurückgeben

    def enqueue(self, x):
        """Haengt ein Element an die Queue an.
        :param x: Anzuhaengendes Element
        """
        self.Q.append(x)
        self.length += 1

    def dequeue(self):
        """Entfernt das erste Element aus der Queue
        :return: Erstes Element
        """
        if self.length >= 1:
            first = self.Q[0]
            for i in range(0, self.length - 1):
                self.Q[i] = self.Q[i + 1]
            del(self.Q[self.length - 1])
            self.length -= 1
            return first