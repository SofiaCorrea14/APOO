#5. Crear una función que convierta grados Fahrenheit a grados Celsius.

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
celsius = fahrenheit_a_celsius(fahrenheit)

print(f"{fahrenheit} grados Fahrenheit son {celsius:.2f} grados Celsius.")
