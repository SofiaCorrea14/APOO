#6. Crear un programa que calcule la suma de los números en una lista dada.

def s_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma


lista = [5, 12, 55, 1, 35]


resultado = s_lista(lista)
print("Suma de los números de la lista: ", resultado)