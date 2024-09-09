class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __repr__(self):
        return f'"{self.titulo}" por {self.autor}'
