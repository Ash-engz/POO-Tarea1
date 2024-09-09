from Perro import Perro
from Propietario import Propietario

class Main:
    @staticmethod
    def ejecutar():
       
        perro1 = Perro(nombre="Oden", tipo_de_mamifero="Canino", tamaño_de_cabeza="Pequeña")
        perro2 = Perro(nombre="Max", tipo_de_mamifero="Canino", tamaño_de_cabeza="Grande")
        perro3 = Perro(nombre="oso", tipo_de_mamifero="Canino", tamaño_de_cabeza="mediana")
        perro4 = Perro(nombre="Doki", tipo_de_mamifero="Canino", tamaño_de_cabeza="Grande")

        propietario = Propietario(nombre="Marcela")
        propietario2 = Propietario(nombre="Carlos")

        propietario.asignar_perro(perro1)

        if propietario.tiene_perro():
            propietario.pasear_perro()  
        else:
            print(f"{propietario.nombre} no tiene un perro asignado.")

        propietario.asignar_perro(perro2)
        if propietario.tiene_perro():
            propietario.pasear_perro()  
        else:
            print(f"{propietario.nombre} no tiene un perro asignado.")

if __name__ == "__main__":
    Main.ejecutar()
