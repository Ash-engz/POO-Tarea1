from abc import ABC, abstractmethod

class Mamifero(ABC):
    def __init__(self, tipo_de_mamifero):
        self.tipo = tipo_de_mamifero  

    @property
    @abstractmethod
    def nombre(self):
        pass

    @property
    def tipo_de_mamifero(self):
        return self.tipo  

    def establecer_tipo(self, nuevo_tipo):
        self.tipo = nuevo_tipo  
