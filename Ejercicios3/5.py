#5

import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
    
    def c_area(self):
        area = math.pi * self.radio ** 2
        return area
    
    def c_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro
    
    def p_pertenece(self, punto):
        dist_al_centro = math.sqrt((punto.x - self.centro.x)**2 + (punto.y - self.centro.y)**2)
        return dist_al_centro <= self.radio

#Ejemplo
centro = Punto(2, 6)
circulo = Circulo(centro, 4)

area = circulo.c_area()
perimetro = circulo.c_perimetro()


print(f"Centro: ({circulo.centro.x}, {circulo.centro.y})")
print(f"Radio: {circulo.radio}")
print(f"Área del círculo: {area}")
print(f"Perímetro del círculo: {perimetro}")

punto1 = Punto(2, 5)
punto2 = Punto(4, 7)

print(f"El punto ({punto1.x}, {punto1.y}) pertenece al círculo: {circulo.p_pertenece(punto1)}")
print(f"El punto ({punto2.x}, {punto2.y}) pertenece al círculo: {circulo.p_pertenece(punto2)}")
