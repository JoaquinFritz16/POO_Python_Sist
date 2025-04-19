class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"
    
vehiculo1 = Vehiculo("Ford", "Fiesta", 2020)
print(vehiculo1) 