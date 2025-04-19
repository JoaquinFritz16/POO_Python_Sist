class Libros:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def mostrar_info(self):
        print(f"\n Titulo: {self.titulo} // Autor: {self.autor} // Año: {self.año}")

lista_libros = []
libro1 = Libros("Mil años de soledad", "Gabriel Garcia Marquez", 1967)
libro2 = Libros("Cronica de una muerte anunciada", "Gabriel Garcia Marquez", 1981)
libro3 = Libros("El ingenioso hidalgo don Quijote de la Mancha", "Miguel de Cervantes", 1605)

lista_libros.append(libro1)
lista_libros.append(libro2)
lista_libros.append(libro3)

for libro in lista_libros:
    libro.mostrar_info()