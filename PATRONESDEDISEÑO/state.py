#PATRON DE DISEÑO DE COMPORTAMIENTO: STATE 

class Estado:
    def login(self, usuario, contrasena):
        raise NotImplementedError("Método no implementado.")

    def logout(self):
        raise NotImplementedError("Método no implementado.")

class Desconectado(Estado):
    def login(self, usuario, contrasena):
        if usuario == "admin" and contrasena == "password123":
            print(f"{usuario} ha iniciado sesión.")
            return Conectado()
        else:
            print("Los datos no coinciden, no se pudo iniciar sesión.")
            return self

    def logout(self):
        print("Ya está desconectado.")

class Conectado(Estado):
    def logout(self):
        print("Ha cerrado sesión.")
        return Desconectado()

    def login(self, usuario, contrasena):
        print(f"{usuario} ya está logueado.")
        return self

class Login:
    def __init__(self):
        self.estado = Desconectado()

    def iniciar_sesion(self, usuario, contrasena):
        self.estado = self.estado.login(usuario, contrasena)

    def cerrar_sesion(self):
        self.estado = self.estado.logout()

login_system = Login()

login_system.iniciar_sesion("admin", "guate2024") 
login_system.iniciar_sesion("admin", "password123")  
login_system.cerrar_sesion()
login_system.cerrar_sesion()  
