#2-3

import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mostrar(self):
        print(f"Estas son las coordenadas del punto: ({self.x}, {self.y})")
    
    def mover(self, n_x, n_y):
        self.x = n_x
        self.y = n_y
    
    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)
        return distancia

#Ejemplo
punto1 = Punto(0, 5)
punto2 = Punto(6, 3)

punto1.mostrar()
punto1.mover(1, 6)
punto1.mostrar()

distancia = punto1.calcular_distancia(punto2)
print(f"Distancia entre los puntos: {distancia}")
