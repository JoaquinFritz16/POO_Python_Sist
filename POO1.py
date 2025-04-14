class Alumnos:
    def __init__(self, nombre, apellido, edad, curso):
        self.nombre = nombre.lower()
        self.apellido = apellido.upper()
        self.edad = edad
        self.curso = curso
        
    def programar(self):
        print(f"{self.nombre} {self.apellido} está programando.")

Alumnos1 = Alumnos("Juan", "Pérez", 20, "6toP")
Alumnos2 = Alumnos("Ana", "García", 22, "5toP")

Alumnos1.programar()
Alumnos2.programar()