# usuariolibreria.py
class Usuariolibreria:
    
    def login_usuario(self):
        username = input("Ingrese nombre de usuario: ")
        password = input("Ingrese contraseña: ")
        
        if username == "Maria" and password == "maria2024":
            print("¡Bienvenid@ María!")
            self.menu_cliente()
        else:
            print("Nombre de usuario o contraseña incorrectos.")
    
    def menu_cliente(self):
        print("¿Qué le gustaría hacer?")
        print("1. Ver secciones")
        print("2. Prestar libros")
        print("3. Devolver libros")
        print("4. Consultar libros")
        print("5. Ver información de usuario")
        print("6. Ver dirección y datos de librería")
