#PATRON DE DISEÑO CREACIONAL: SINGLETON

class Iniciosion:  
    _instance = None  

    def __new__(cls):
        if cls._instance is None:  
            cls._instance = super().__new__(cls)
            cls._instance.user = None  
        return cls._instance  

    def get_logged_in_user(self):
        return self.user

    def login(self, username, password):
        if self.user:
            print(f"{self.user} ya está logueado.")
            return False
        
        if username == "admin" and password == "password123":
            self.user = username
            print(f"{username} sesión iniciada")
            return True
        else:
            print("Los datos no coinciden, no se pudo iniciar sesión.")
            return False

    def logout(self):
        if self.user:
            print(f"{self.user} sesión cerrada")
            self.user = None
        else:
            print("No hay inicios de sesión.")

session1 = Iniciosion()
session2 = Iniciosion()

print(session1 is session2) 

session1.login("admin", "guate2024")  
print("Usuario logueado:", session2.get_logged_in_user())  

session2.logout()

print("Usuario logueado:", session1.get_logged_in_user())  
