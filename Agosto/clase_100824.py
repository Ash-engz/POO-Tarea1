# Definiendo clase carro
class Carro:
    # Construye objeto
    def __init__(self, color, numero_serie, marca, modelo, anio):
        self.__color = color
        self.__numero_serie = numero_serie
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__kilometraje = 0
        self.__gasolina =0 
        self.__gasolina_max = 12
        self.__eficiencia =32



        


    # Imprime objetos
    def __str__(self):
        return f"Un carro {self.marca} {self.modelo} {self.anio} color {self.color} con kilometraje {self.kilometraje}"
    
    def get_gasolina(self):
        return f"Este carro tiene {self.__gasolina} galones"
    
    def agregar_gasolina(self, galones):
        if galones >0 and self.__gasolina + galones  <= self.__gasolina_max:
        self.__gasolina += galones 
    
    # Métodos
    def avanzar(self, kilometros=10):
        self.kilometraje += kilometros


def cambiar_color(self,color):
    if color == 'rojo ':
        self.__color = color
    elif color == 'blanco ':
        self.__color = color
     elif color == 'negro ':
         self.__color = color

class Persona:
    def __init__(self, nombre, apellido, anio_de_nacimiento, carro=None):
        self.nombre = nombre
        self.apellido = apellido
        self.anio_de_nacimiento = anio_de_nacimiento
        self.carro = None
        self.agregar_carro(carro)
    
    def __str__(self):
        descripcion = f'Una persona de nombre {self.nombre} {self.apellido} '
        if self.carro:
            return descripcion + f'con carro {self.carro.color}'
        else:
            return descripcion + 'sin carro'
    
    def agregar_carro(self, carro):
        if 2024 - self.anio_de_nacimiento > 16:
            self.carro = carro
            print('Carro agregado')
        else:
            print('No puede tener carro')
    
    def get_nombre(self):
        # Medir cuántas veces se accede al nombre
        # veces += 1
        return self.nombre
    
    def set_nombre(self, nombre):
        # Revisar que no sea un número
        # Revisar que no sea el mismo
        # Revisar que no sea broma
        self.nombre = nombre

    def get_apellido(self):
        return self.apellido
    
    # ...

    def get_nombre_completo(self):
        return f'Nombre completo: {self.nombre} {self.apellido}'
    
    def manejar(self):
        if self.carro:
            self.carro.avanzar()
        
carro_rojo = Carro("rojo", 123, "Honda", "Civic", 2015)
carro_negro = Carro("negro", 321, "Toyota", "Yaris", 2007)

juanito = Persona('Juanito', 'Juanitez', 2012)
#juanito.agregar_carro(carro_negro)
print(juanito)
#juanito.manejar()

print (carro_negro.)

juanita = Persona('Juanita', 'Juanitez', 2006, carro_rojo)
#print(juanita.get_nombre_completo())
#juanita.agregar_carro(carro_rojo)
#juanita.manejar()
print(juanita)

print(carro_rojo)
#carro_rojo.anio =1999
#print(carro_rojo)
#para restringir se coloca doble guion bajo, que es privado 
# solo un # es privado y 2# es protegido 
