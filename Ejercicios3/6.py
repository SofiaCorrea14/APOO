#6

class Carta:

    CORAZONES = 'Corazones'
    DIAMANTES = 'Diamantes'
    PICAS = 'Picas'
    TREBOLES = 'Tréboles'
    
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

#Ejemplo
carta1 = Carta('5', Carta.DIAMANTES)
carta2 = Carta('J', Carta.TREBOLES)

print(f"Carta 1: Valor - {carta1.valor}, Pinta - {carta1.pinta}")
print(f"Carta 2: Valor - {carta2.valor}, Pinta - {carta2.pinta}")
