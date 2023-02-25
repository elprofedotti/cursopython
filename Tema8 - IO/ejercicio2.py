from pickle import *

class Vehiculo:

    def __init__(self, modelo, color):
        self.color = color
        self.modelo=modelo

    def __str__(self):
        return self.modelo + " " + self.color


auto = Vehiculo("Mondeo", "Rojo")

archivo = open('objetoVehiculo', 'w+b')

dump(auto, archivo)

archivo.seek(0)
auto2 = load(archivo)

print(auto2)
archivo.close()