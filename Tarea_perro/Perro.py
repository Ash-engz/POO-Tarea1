from Mamifero import Mamifero
from Cabeza import Cabeza

class Perro(Mamifero):
    def __init__(self, nombre, tipo_de_mamifero, tamaño_de_cabeza):
        super().__init__(tipo_de_mamifero) 
        self._nombre = nombre  
        self.cabeza = Cabeza(tamaño_de_cabeza)  

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre  

    def ir_a_pasear(self):
        print(f"{self.nombre} está dando un paseo.")  

    def obtener_tamaño_de_cabeza(self):
        return self.cabeza.obtener_tamaño()  

    def establecer_tamaño_de_cabeza(self, nuevo_tamaño):
        self.cabeza.establecer_tamaño(nuevo_tamaño)  
