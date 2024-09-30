class PersonalAutorizado:
    
    def loginpersonal(self):
        username = input("Ingrese nombre de usuario: ")
        password = input("Ingrese contraseña: ")
        
        if username == "pablo" and password == "libreriacreaciones":
            print("¡Bienvenido Pablo!")
        else:
            print("Nombre de usuario o contraseña incorrectos.")