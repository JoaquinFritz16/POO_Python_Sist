class Herramientas:
    def __init__(self, nombre, marca, precio, cantidad):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.cantidad = cantidad

        
    def mostrar_datos(self):
        print(f"\n Nombre: {self.nombre}, Marca: {self.marca}, Precio: {self.precio}, Cantidad: {self.cantidad}")



lista_herramientas = []
cliente1 = Herramientas("Destornillador", "Stanley", 10.99, 5)
cliente2 = Herramientas("Martillo", "DeWalt", 15.49, 3)
cliente3 = Herramientas("Taladro", "Bosch", 99.99, 1)

lista_herramientas.append(cliente1)
lista_herramientas.append(cliente2)
lista_herramientas.append(cliente3)

for herramienta in lista_herramientas:
    herramienta.mostrar_datos()
