#14. Escribir una función que calcule la media aritmética de una lista de números


def media_aritmetica(lista):
    if len(lista) == 0:
        return None
    suma = sum(lista)
    media = suma / len(lista)
    return media

mi_lista = [1, 2, 3, 4, 5]
resultado_media = media_aritmetica(mi_lista)
print("Media aritmética de la lista:", resultado_media)