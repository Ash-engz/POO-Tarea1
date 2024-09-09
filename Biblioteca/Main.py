from Libreria import Libreria
from Usuario import Usuario
from Libro import Libro

class Main:
    def __init__(self):
        self.mi_libreria = Libreria("14 ave 23-81 zona 4")

        libro1 = Libro("Drácula", "Bram Stoker")
        libro2 = Libro("Frankenstein", "Mary Shelley")
        libro3 = Libro("El Resplandor", "Stephen King")
        libro4 = Libro("Carrie", "Stephen King")
        libro5 = Libro("La paciente silenciosa", "ALEX MICHAELIDES")
        libro6 = Libro("El psicoanalista", "John Katzenbach")
        libro7 = Libro("El espía que surgió del frío", "Le Carre, John")
        libro8 = Libro("El cuaderno de Noah", "NICHOLAS SPARKS")
        libro9 = Libro("Cumbres borrascosas", "Emily Brontë")
        libro10 = Libro("Cometas en el cielo", "Khaled Hosseini")

        for libro in [libro1, libro2, libro3, libro4, libro5, libro6, libro7, libro8, libro9, libro10]:
            self.mi_libreria.agregar_libro(libro)

        self.juan = Usuario("12345", "Juan", "Pérez", "01/01/2000")
        self.maria = Usuario("44334", "Maria", "Miranda", "05/04/2006")
        self.pedro = Usuario("55667", "Pedro", "Ramírez", "12/09/1998")

        self.ejecutar_operaciones()

    def ejecutar_operaciones(self):
        print("Catálogo inicial:")
        self.mi_libreria.mostrar_catalogo()

        nuevo_libro = Libro("Nuevo Libro", "Nuevo Autor")
        print("\nAgregando un nuevo libro:")
        self.mi_libreria.agregar_libro(nuevo_libro)

        print(f"\n{self.juan.nombre} consulta la disponibilidad de 'Drácula':")
        self.juan.consultar_libro(self.mi_libreria, "Drácula")

        print(f"\n{self.juan.nombre} intenta prestar 'Drácula':")
        self.juan.prestar_libro(self.mi_libreria, "Drácula")

        print(f"\n{self.juan.nombre} consulta la disponibilidad de 'Drácula' después de prestarlo:")
        self.juan.consultar_libro(self.mi_libreria, "Drácula")

        print(f"\n{self.juan.nombre} devuelve 'Drácula':")
        self.juan.devolver_libro(self.mi_libreria, "Drácula")

        print(f"\n{self.juan.nombre} consulta la disponibilidad de 'Drácula' después de devolverlo:")
        self.juan.consultar_libro(self.mi_libreria, "Drácula")

        print(f"\n{self.juan.nombre} elimina 'Nuevo Libro':")
        self.mi_libreria.eliminar_libro("Nuevo Libro")

        print("\nCatálogo después de eliminar un libro:")
        self.mi_libreria.mostrar_catalogo()

if __name__ == "__main__":
    app = Main()
