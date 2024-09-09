from Libreria import Libreria
from Libro import Libro

class Usuario:
    def __init__(self, carnet, nombre, apellido, fecha_nacimiento):
        self.carnet = carnet
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento

    def prestar_libro(self, libreria, titulo):
        libreria.prestar_libro(titulo)

    def devolver_libro(self, libreria, titulo):
        for libro in libreria.catalogo:
            if libro.titulo == titulo:
                libreria.devolver_libro(libro)
                return
        print(f'El libro "{titulo}" no está en el catálogo.')

    def consultar_libro(self, libreria, titulo):
        libreria.consultar_libro(titulo)

    def agregar_libro(self, libreria, libro):
        libreria.agregar_libro(libro)

    def eliminar_libro(self, libreria, titulo):
        libreria.eliminar_libro(titulo)
