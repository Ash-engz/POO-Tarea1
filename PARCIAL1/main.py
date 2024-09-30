from cliente_class import Cliente
from cuentaahorro import CuentaDeAhorro
from terjetacredito import TarjetaDeCredito
from tarjetadebito import TarjetaDeDebito
from chequeras import Chequera
from colaborador import Colaborador, BibliotecaColaboradores

class BibliotecaClientes:
    def __init__(self):
        self.clientes = [
            {"usuario": "carlos", "contraseña": "987654", "nombre": "Carlos Perez", "dpi": 1234567890101, "municipio": "Guatemala"},
            {"usuario": "maria", "contraseña": "654321", "nombre": "Maria López", "dpi": 1098765432101, "municipio": "Antigua"}
        ]

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_clientes(self):
        print("Lista de clientes existentes:")
        for cliente in self.clientes:
            print(f"Usuario: {cliente['usuario']}, Nombre: {cliente['nombre']}, DPI: {cliente['dpi']}, Municipio: {cliente['municipio']}")

    def verificar_cliente(self, usuario, contraseña):
        for cliente in self.clientes:
            if cliente['usuario'] == usuario and cliente['contraseña'] == contraseña:
                return cliente
        return None

class Main:
    def __init__(self):
        self.biblioteca_colaboradores = BibliotecaColaboradores()
        self.biblioteca_clientes = BibliotecaClientes()  
        self.agregar_colaboradores() 

    def agregar_colaboradores(self):
        self.biblioteca_colaboradores.agregar_colaborador(Colaborador("Juan", "01-01-1980", "Guatemala", "Gerente", 15000))
        self.biblioteca_colaboradores.agregar_colaborador(Colaborador("María", "02-02-1985", "Guatemala", "Asistente", 8000))

    def ejecutar(self):
        while True:
            respuesta = input("Bienvenido a SAPO.S.A. ¿ingresará cliente(a) o personal autorizado (b)? ")
            
            if respuesta.lower() == 'b':
                self.login_personal_autorizado()
            elif respuesta.lower() == 'a': 
                usuario_respuesta = input("¿Es usuario existente (a) o desea registrarse como nuevo usuario (b)? ")
                
                if usuario_respuesta.lower() == 'a':
                    usuario = input("Ingrese usuario: ")
                    contraseña = input("Ingrese su contraseña: ")

                    cliente = self.biblioteca_clientes.verificar_cliente(usuario, contraseña)
                    if cliente:
                        print(f"Ingreso exitoso, bienvenido '{cliente['nombre']}'")
                        self.menu_cliente()
                    else:
                        print("Los datos no coinciden. Intente nuevamente.")
                        
                elif usuario_respuesta.lower() == 'b':
                    nuevo_cliente = self.registrar_cliente()
                    if nuevo_cliente:
                        self.biblioteca_clientes.agregar_cliente(nuevo_cliente)
                        print(f"Usuario registrado exitosamente. Bienvenido, {nuevo_cliente['nombre']}")
                        self.menu_cliente()

    def login_personal_autorizado(self):
        usuario = input("Ingrese usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        if usuario == 'juan' and contraseña == '123456':
            print(f"Ingreso exitoso, bienvenido '{usuario}'")
            self.menu_personal_autorizado()
        else:
            print("Los datos no coinciden. Intente nuevamente.")

    def menu_personal_autorizado(self):
        while True:
            print("Ingrese la opción de su interés")
            respuesta = input("(a) información de cliente. (b) lista de clientes. (c) información colaborador (d) lista de colaboradores (e) salir: ")

            if respuesta.lower() == 'a':
                self.consultar_cliente()
            elif respuesta.lower() == 'b':
                self.biblioteca_clientes.mostrar_clientes()
            elif respuesta.lower() == 'c':
                self.consultar_colaborador()
            elif respuesta.lower() == 'd':
                self.biblioteca_colaboradores.mostrar_todos_los_colaboradores()
            elif respuesta.lower() == 'e':
                break

    def registrar_cliente(self):
        cliente = Cliente()
        return {
            "usuario": cliente.usuario,
            "contraseña": cliente.contraseña,
            "nombre": cliente.nombre,
            "dpi": cliente.dpi,
            "municipio": cliente.municipio
        }

    def menu_cliente(self):
        while True:
            print("Opciones del cliente:")
            respuesta = input("(a) Cuenta de Ahorro (b) Tarjeta de Crédito (c) Tarjeta de Débito (d) Chequera (e) salir: ")
            if respuesta.lower() == 'a':
                cuenta = CuentaDeAhorro()
                cuenta.mostrar_info()
            elif respuesta.lower() == 'b':
                tarjeta_credito = TarjetaDeCredito()
                tarjeta_credito.mostrar_info()
            elif respuesta.lower() == 'c':
                tarjeta_debito = TarjetaDeDebito()
                tarjeta_debito.mostrar_info()
            elif respuesta.lower() == 'd':
                chequera = Chequera()
                chequera.mostrar_informacion()
            elif respuesta.lower() == 'e':
                break

if __name__ == "__main__":
    main = Main()
    main.ejecutar()