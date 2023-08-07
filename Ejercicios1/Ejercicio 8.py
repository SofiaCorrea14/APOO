#8. Crear una función que invierta el orden de los elementos en una lista dada.


def inv_lista(lista):
    longitud = len(lista)
    for i in range(longitud // 2):
        lista[i], lista[longitud - i - 1] = lista[longitud - i - 1], lista[i]

mi_lista = [8, 9, 10, 11, 12]
print("Lista:", mi_lista)

inv_lista(mi_lista)
print("Lista invertida:", mi_lista)