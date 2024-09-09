from Mamifero import Mamifero
from Perro import Perro

class Propietario(Mamifero):
    def __init__(self, nombre):
        super().__init__(tipo_de_mamifero=None)  
        self._nombre = nombre  
        self._perro = None  

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre 

    def asignar_perro(self, perro):
        self._perro = perro  

    def tiene_perro(self):
        return self._perro is not None  

    def pasear_perro(self):
        if self.tiene_perro():
            self._perro.ir_a_pasear()  
        else:
            print(f"{self.nombre} no tiene ningún perro asignado para pasear.")
