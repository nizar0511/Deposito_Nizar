#Classe Punto
import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Metodo muovi

#Questo metodo modifica le coordinate del punto aggiungendo gli spostamenti dx e dy.

    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy

#Metodo distanza_da_origine

#La distanza dall’origine (0,0) si calcola con la formula della distanza euclidea:

#√(x² + y²)

    def distanza_da_origine(self):
        return math.sqrt(self.x**2 + self.y**2)


#Classe completa
import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        return math.sqrt(self.x**2 + self.y**2)