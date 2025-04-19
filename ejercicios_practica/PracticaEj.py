class Mascotas:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    
    def presentarse(self):
        print(f"Hola, soy un {self.especie} y me llamo {self.nombre}, tengo {self.edad} años")

mascota1 = Mascotas("Max", "perro", 3)
mascota2 = Mascotas("Luna", "gato", 2)
mascota3 = Mascotas("Lucas", "pato", 52)

mascota1.presentarse()
mascota2.presentarse()
mascota3.presentarse()