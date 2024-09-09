class Libreria:
    def __init__(self, direccion):
        self.direccion = direccion
        self.catalogo = []
        self.secciones = ["Drama", "Terror", "Romance", "Suspenso", "Educativas"]

    def mostrar_catalogo(self):
        if not self.catalogo:
            print("El catálogo está vacío.")
        else:
            print("Catálogo de libros:")
            for libro in self.catalogo:
                print(f"- {libro}")

    def agregar_libro(self, libro):
        self.catalogo.append(libro)
        print(f'Libro "{libro.titulo}" agregado al catálogo.')

    def prestar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False
                print(f'Libro "{libro.titulo}" ha sido prestado. Se devolverá en 2 semanas.')
                return libro
        print(f'El libro "{titulo}" no está disponible o no existe en el catálogo.')
        return None

    def devolver_libro(self, libro):
        libro.disponible = True
        print(f'Libro "{libro.titulo}" ha sido devuelto.')

    def consultar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo == titulo:
                estado = "disponible" if libro.disponible else "no disponible"
                print(f'El libro "{libro.titulo}" está {estado}.')
                return
        print(f'El libro "{titulo}" no está en el catálogo.')

    def eliminar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo == titulo:
                self.catalogo.remove(libro)
                print(f'Libro "{titulo}" ha sido eliminado del catálogo.')
                return
        print(f'El libro "{titulo}" no se encontró en el catálogo.')
