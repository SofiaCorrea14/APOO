#2.Escribir una función que calcule el área de un círculo dado su radio.

def c_area_circulo(radio):
    area = 3.141592653589793 * (radio ** 2)
    return area

radio_circulo = (int(input("Ingrese el radio del circulo: ")))
area_circulo = c_area_circulo(radio_circulo)
print("Área del círculo:", area_circulo)