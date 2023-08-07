#11. Crear un programa que genere una lista de números pares entre 1 y 100.


def g_lista_par():
    lista_par = [numero for numero in range(2, 101) if numero % 2 == 0]
    return lista_par

lista_pares_generada = g_lista_par()
print("Lista de números pares: ")
print(lista_pares_generada)