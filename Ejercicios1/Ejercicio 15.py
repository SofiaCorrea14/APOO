#15. Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no

def si_palindromo(cadena):
    cadena = cadena.lower()
    cadena = ''.join(c for c in cadena if c.isalnum())  
    return cadena == cadena[::-1]


cadena = input("Ingrese una cadena de texto: ")

if si_palindromo(cadena):
    print("El texto es un palíndromo.")
else:
    print("El texto no es un palídromo")

def si_palindromo(cadena):
    cadena = cadena.lower()
    cadena = ''.join(c for c in cadena if c.isalnum())  
    return cadena == cadena[::-1]

#Solicitar al usuario ingresar una cadena de texto
cadena = input("Ingrese una cadena de texto: ")

if si_palindromo(cadena):
    print("La cadena es un palíndromo.")
else:
    print("El texto no es un palíndromo.")
    print("El texto no es un palíndromo.")