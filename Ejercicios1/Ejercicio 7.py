#7. Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada

def encontrar_minimo_maximo(lista):
    if not lista:
        return None, None 

    minimo = maximo = lista[0]

    for numero in lista:
        if numero < minimo:
            minimo = numero
        if numero > maximo:
            maximo = numero

    return minimo, maximo

numeros = [23, 5, 67, 12, 89, 43, 9, 41, 56]

minimo, maximo = encontrar_minimo_maximo(numeros)

print(f"El número más pequeño es: {minimo}")
print(f"El número más grande es: {maximo}")