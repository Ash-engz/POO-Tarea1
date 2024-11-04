#PATRON DE DISEÑO ESTRUCTURAL: ADAPTADOR

class Antiguo:
    def verificar_credenciales(self, usuario, contraseña):
        return usuario == "admin" and contraseña == "12345"

class Nuevo:
    def validar_usuario(self, usuario, contraseña):
        return usuario == "admin" and contraseña == "password123"

class Adaptador:
    def __init__(self, sistema_autenticacion_nuevo):
        self.sistema_autenticacion_nuevo = sistema_autenticacion_nuevo

    def verificar_credenciales(self, usuario, contraseña):
        return self.sistema_autenticacion_nuevo.validar_usuario(usuario, contraseña)

class Login:
    def __init__(self, adaptador_autenticacion):
        self.adaptador_autenticacion = adaptador_autenticacion
        self.usuario = None

    def iniciar_sesion(self, usuario, contraseña):
        if self.usuario:
            print(f"{self.usuario} ya está logueado.")
            return False

        if self.adaptador_autenticacion.verificar_credenciales(usuario, contraseña):
            self.usuario = usuario
            print(f"{usuario} ha iniciado sesión.")
            return True
        else:
            print("Los datos no coinciden, no se pudo iniciar sesión.")
            return False

    def cerrar_sesion(self):
        if self.usuario:
            print(f"{self.usuario} ha cerrado sesión.")
            self.usuario = None
        else:
            print("No hay inicios de sesión.")


sistema_autenticacion_nuevo = Nuevo()
adaptador = Adaptador(sistema_autenticacion_nuevo)

sesion = Login(adaptador)

sesion.iniciar_sesion("admin", "12345")  
print("Usuario logueado:", sesion.usuario) 

sesion.cerrar_sesion()

print("Usuario logueado:", sesion.usuario) 
