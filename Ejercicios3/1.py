#1

class Vehiculo:
    def __init__(self, vel_max, kilometraje):
        self.vel_max = vel_max
        self.kilometraje = kilometraje

#Ejemplo
vehiculo = Vehiculo(100, 400)
print(f"Velocidad máxima del vehículo: {vehiculo.vel_max}")
print(f"Kilometraje del vehículo: {vehiculo.kilometraje}")
