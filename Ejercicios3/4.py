#4

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangulo:
    def __init__(self, esq_sup_izq, esq_inf_der):
        self.esq_sup_izq = esq_sup_izq
        self.esq_inf_der = esq_inf_der
    
    def calcular_perimetro(self):
        base = abs(self.esq_sup_izq.x - self.esq_inf_der.x)
        altura = abs(self.esq_sup_izq.y - self.esq_inf_der.y)
        perimetro = 2 * (base + altura)
        return perimetro
    
    def calcular_area(self):
        base = abs(self.esq_sup_izq.x - self.esq_inf_der.x)
        altura = abs(self.esq_sup_izq.y - self.esq_inf_der.y)
        area = base * altura
        return area
    
    def es_cuadrado(self):
        base = abs(self.esq_sup_izq.x - self.esq_inf_der.x)
        altura = abs(self.esq_sup_izq.y - self.esq_inf_der.y)
        return base == altura

#Ejemplo
punto_sup_izq = Punto(4, 2)
punto_inf_der = Punto(6, 3)
rectangulo = Rectangulo(punto_sup_izq, punto_inf_der)

perimetro = rectangulo.calcular_perimetro()
area = rectangulo.calcular_area()
es_cuadrado = rectangulo.es_cuadrado()


print(f"Esquina superior izquierda: ({rectangulo.esq_sup_izq.x}, {rectangulo.esq_sup_izq.y})")
print(f"Esquina inferior derecha: ({rectangulo.esq_inf_der.x}, {rectangulo.esq_inf_der.y})")
print(f"Perímetro del rectángulo: {perimetro}")
print(f"Área del rectángulo: {area}")
print(f"¿El rectángulo es un cuadrado? {es_cuadrado}")
