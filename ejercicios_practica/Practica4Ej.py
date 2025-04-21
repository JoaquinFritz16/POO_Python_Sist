import time
import random
class Veterinaria:
    def __init__(self, nombre, direccion, telefono, raza):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.raza = raza
    
    def mostrar_datos(self):
        print(f"\n Nombre: {self.nombre} Direccion: {self.direccion} Telefono: {self.telefono} Raza: {self.raza}")
    
    def __str__(self):
        return f"{self.nombre} | {self.direccion} | {self.telefono} | {self.raza}"
    
    def enviar_datos(self):
        print(f"\n Enviando datos de '{self.nombre}'")
        time.sleep(1)
    
        if random.random() < 0.5:
            print(f"\n Datos enviados con exito a '{self.nombre}'")
            return True
        else:
            print(f"\n Error al enviar datos de '{self.nombre}'")
            return False
    @staticmethod
    def eliminar_animal(lista_animales, nombre_animal):
        nombre_animal = nombre_animal.lower()

        for animal in lista_animales:
            if animal.nombre.lower() == nombre_animal:
                if not animal.enviar_datos():
                    print(f"Error al enviar datos de {animal.nombre}")
                    return

                lista_animales.remove(animal)
                print(f"\n El animal {nombre_animal} ha sido eliminado de la lista")
                print("Nueva Lista:")
                for a in lista_animales:
                    print("  -", a)
                return True
        print("No se encontro ningun animal con ese nombre, por favor revisar la lista")
    @staticmethod
    def agregar_animal(lista_animales):
        nombre = input("Nombre: ").strip()
        direccion = input("Direccion: ").strip()
        telefono = input("Telefono: ").strip()
        raza = input("Raza: ").strip()

        for animal in lista_animales:
            if animal.nombre.lower() == nombre.lower():
                print(f"El animal '{nombre}' ya existe en la lista")
                return
        
        new_animal = Veterinaria(nombre, direccion, telefono, raza)
        if not new_animal.enviar_datos():
            print("No se pudo enviar los datos del animal")
            return

        lista_animales.append(new_animal)
        print(f"\n El animal {nombre} ha sido agregado a la lista")
        print("Nueva Lista:")
        for a in lista_animales:
            print("  -", a)
        return True


if __name__ == "__main__":
    lista_animales = []
    animal1= Veterinaria("Perrito", "Calle 1", "1234567", "Pitbull")
    animal2= Veterinaria("Michi", "Calle 33", "1234567", "Ruso")
    animal3= Veterinaria("Goldi", "Calle 43 Sur", "2930234", "Poodle")

    lista_animales.append(animal1)
    lista_animales.append(animal2)
    lista_animales.append(animal3)



    print("Lista de animales:")
    for animal in lista_animales:
        time.sleep(0.6)
        animal.mostrar_datos()

    print("\n Agregar animal a la lista:")
    Veterinaria.agregar_animal(lista_animales)

    nombre = input("\n Ingrese el nombre del animal que desea eliminar: ")
    time.sleep(0.6)
    Veterinaria.eliminar_animal(lista_animales, nombre)

