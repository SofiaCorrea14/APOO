#7-11

class Cbancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print(f"Depósito de {cantidad} realizado. Saldo Nuevo: {self.balance}")
        else:
            print("El depósito debe ser mayor que cero.")
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Retiro de {cantidad} realizado. Saldo Nuevo: {self.balance}")
        else:
            print("Fondos insuficientes.")
    
    def aplicar_cuota_manejo(self):
        cuota = 0.02 * self.balance
        self.balance -= cuota
        print(f"Se cobró un cargo por manejo del 2%. Saldo Nuevo: {self.balance}")
    
    def mostrar_detalles(self):
        print("Detalles:")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: {self.balance}")

#Ejemplo
cuenta = Cbancaria('55300032043', ['Amparo', 'Luisa'], 2000)

cuenta.mostrar_detalles()
cuenta.depositar(600)
cuenta.retirar(450)
cuenta.aplicar_cuota_manejo()
cuenta.mostrar_detalles()
