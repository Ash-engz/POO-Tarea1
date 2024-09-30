class Conyuge:
    def __init__(self, nombre, fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar_info(self):
        print(f"Cónyuge: {self.nombre}, Fecha de nacimiento: {self.fecha_nacimiento}")

class Colaborador:
    def __init__(self, nombre, fecha_nacimiento, municipio, puesto, salario, conyuge=None):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.municipio = municipio
        self.puesto = puesto
        self.salario = salario
        self.conyuge = conyuge  

    def mostrar_info(self):
        print(f"Colaborador: {self.nombre}, Puesto: {self.puesto}, Salario: {self.salario}")
        if self.conyuge:
            self.conyuge.mostrar_info()  

class BibliotecaColaboradores:
    def __init__(self):
        self.colaboradores = []

    def agregar_colaborador(self, colaborador):
        self.colaboradores.append(colaborador)

    def mostrar_todos_los_colaboradores(self):
        if not self.colaboradores:
            print("No hay colaboradores registrados.")
            return
        print("Lista de colaboradores:")
        for colaborador in self.colaboradores:
            colaborador.mostrar_info()

    def mostrar_colaborador(self, nombre):
        for colaborador in self.colaboradores:
            if colaborador.nombre.lower() == nombre.lower():
                colaborador.mostrar_info()
                return
        print("Colaborador no encontrado.")
