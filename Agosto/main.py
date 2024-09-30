

#from Clase import Clase
#from Clase2 import Clase2

#clase_objeto = Clase()





libros = {}

class Main:
    libros = {
        "Drácula": {"autor": "Bram Stoker", "estado": "disponible"},
        "Frankenstein": {"autor": "Mary Shelley", "estado": "disponible"},
        "El Resplandor": {"autor": "Stephen King", "estado": "disponible"},
        "Carrie": {"autor": "Stephen King", "estado": "disponible"},
        "La paciente silenciosa": {"autor": "Alex Michaelides", "estado": "disponible"},
        "El psicoanalista": {"autor": "John Katzenbach", "estado": "disponible"},
        "El espía que surgió del frío": {"autor": "John le Carré", "estado": "disponible"},
        "La chica del tren": {"autor": "Paula Hawkins", "estado": "disponible"},
        "Quedará el amor": {"autor": "Khaled Hosseini", "estado": "disponible"},
        "Terciopelo": {"autor": "Annie Lennox", "estado": "disponible"},
        "Cometas en el cielo": {"autor": "Khaled Hosseini", "estado": "disponible"},
        "Las hijas de la criada": {"autor": "Amy McKay", "estado": "disponible"},
        "Orgullo y prejuicio": {"autor": "Jane Austen", "estado": "disponible"},
        "Cumbres borrascosas": {"autor": "Emily Brontë", "estado": "disponible"},
        "El cuaderno de Noah": {"autor": "Nicholas Sparks", "estado": "disponible"},
        "La mujer del viajero en el tiempo": {"autor": "Audrey Niffenegger", "estado": "disponible"}
    }

    if __name__ == "__main__":
        print("Bienvenid@ a Librería Creaciones")
        respuesta = input("¿Quién desea ingresar? A. Personal autorizado o B. Cliente: ").strip().lower()

        def loginpersonal():
            username = input("Ingrese nombre de usuario: ")
            password = input("Ingrese contraseña: ")
            acceso = False

            # Verificar las credenciales
            if username == "pablo" and password == "libreriacreaciones":
                acceso = True
                print("¡Bienvenido Pablo!")
            else:
                print("Nombre de usuario o contraseña incorrectos.")

            if acceso:
                while True:
                    print("\n¿Qué le gustaría hacer?")
                    print("1. Agregar Libro")
                    print("2. Eliminar Libro")
                    print("3. Ver Estado de Libro")
                    print("4. Prestar Libro")
                    print("5. Devolver Libro")
                    print("6. Consultar Libro")
                    print("7. Ver Secciones")
                    print("8. Ver Información de Libro")  # Nueva opción
                    print("9. Salir")
                    respuesta = input("Ingrese la opción que desea: ")

                    if respuesta == '1':
                        agregar_libro()
                    elif respuesta == '2':
                        eliminar_libro()
                    elif respuesta == '3':
                        ver_estado_libro()
                    elif respuesta == '4':
                        prestar_libro()
                    elif respuesta == '5':
                        devolver_libro()
                    elif respuesta == '6':
                        consultar_libro()
                    elif respuesta == '7':
                        catalogo_libros()
                    elif respuesta == '8':  # Opción para ver información de libros
                        ver_informacion_libro()
                    elif respuesta == '9':
                        print("Saliendo del sistema de personal autorizado...")
                        break
                    else:
                        print("Opción no válida.")

        def agregar_libro():
            print("\nAgregar Libro:")
            genero = input("Ingrese el género del libro (1. Terror, 2. Suspenso, 3. Drama, 4. Romance): ")
            if genero in ['1', '2', '3', '4']:
                titulo = input("Ingrese el título del libro: ")
                if titulo in libros:
                    print("El libro ya existe en el catálogo.")
                else:
                    autor = input("Ingrese el nombre del autor: ")
                    libros[titulo] = {"autor": autor, "estado": "disponible"}
                    print(f"Libro '{titulo}' agregado correctamente.")
            else:
                print("Género no válido.")

        def eliminar_libro():
            print("\nEliminar Libro:")
            genero = input("Ingrese el género del libro (1. Terror, 2. Suspenso, 3. Drama, 4. Romance): ")
            if genero in ['1', '2', '3', '4']:
                titulo = input("Ingrese el título del libro a eliminar: ")
                if titulo in libros:
                    del libros[titulo]
                    print(f"Libro '{titulo}' eliminado correctamente.")
                else:
                    print("El libro no está en el catálogo.")
            else:
                print("Género no válido.")

        def ver_estado_libro():
            print("\nVer Estado de Libro:")
            titulo = input("Ingrese el título del libro: ")
            if titulo in libros:
                estado = libros[titulo]["estado"]
                if estado == "prestado":
                    print(f"El libro '{titulo}' está prestado. Estará disponible en 2 semanas.")
                else:
                    print(f"El libro '{titulo}' está disponible.")
            else:
                print("El libro no está en el catálogo.")

        def prestar_libro():
            print("\nPrestar Libro:")
            titulo = input("Ingrese el título del libro a prestar: ")
            if titulo in libros and libros[titulo]["estado"] == "disponible":
                libros[titulo]["estado"] = "prestado"
                print(f"El libro '{titulo}' ha sido prestado.")
            else:
                print("El libro no está disponible para préstamo o no está en el catálogo.")

        def devolver_libro():
            print("\nDevolver Libro:")
            titulo = input("Ingrese el título del libro a devolver: ")
            if titulo in libros and libros[titulo]["estado"] == "prestado":
                libros[titulo]["estado"] = "disponible"
                print(f"El libro '{titulo}' ha sido devuelto y está disponible.")
            else:
                print("El libro no está prestado o no está en el catálogo.")

        def consultar_libro():
            print("\nConsultar Libro:")
            titulo = input("Ingrese el título del libro a consultar: ")
            if titulo in libros:
                autor = libros[titulo]["autor"]
                estado = libros[titulo]["estado"]
                print(f"Título: {titulo}, Autor: {autor}, Estado: {estado}")
            else:
                print("El libro no está en el catálogo.")

        def ver_informacion_libro():
            print("\nInformación del Libro:")
            titulo = input("Ingrese el título del libro: ")
            if titulo in libros:
                autor = libros[titulo]["autor"]
                estado = libros[titulo]["estado"]
                print(f"Título: {titulo}, Autor: {autor}, Estado: {estado}")
            else:
                print("El libro no está en el catálogo.")

        def login_usuario():
            nombre_completo = input("Ingrese su nombre completo (ejemplo: Maria Zepeda): ")
            if nombre_completo != "Maria Zepeda":
                print("Nombre completo incorrecto.")
                return

            fecha_nacimiento = input("Ingrese su fecha de nacimiento (ejemplo: 04/08/2000): ")
            if fecha_nacimiento != "04/08/2000":
                print("Fecha de nacimiento incorrecta.")
                return

            numero_carnet = input("Ingrese su número de carnet (ejemplo: 11223344): ")
            if numero_carnet != "11223344":
                print("Número de carnet incorrecto.")
                return

            print("¡Bienvenid@ María!")
            while True:
                print("\n¿Qué le gustaría hacer?")
                print("1. Información de la librería")
                print("2. Catálogo de libros según sección/género")
                print("3. Ver estado de libro")
                print("4. Prestar libro")
                print("5. Devolver libro")
                print("6. Consultar libro")
                print("7. Ver información de libro")  # Nueva opción
                print("8. Salir")
                respuesta_usuario = input("Ingrese el número de la opción que desea: ")

                if respuesta_usuario == '1':
                    ver_informacion_libreria()
                elif respuesta_usuario == '2':
                    catalogo_libros()
                elif respuesta_usuario == '3':
                    ver_estado_libro()
                elif respuesta_usuario == '4':
                    prestar_libro()
                elif respuesta_usuario == '5':
                    devolver_libro()
                elif respuesta_usuario == '6':
                    consultar_libro()
                elif respuesta_usuario == '7':  # Opción para ver información de libros
                    ver_informacion_libro()
                elif respuesta_usuario == '8':
                    print("Saliendo del sistema de usuario...")
                    break
                else:
                    print("Opción no válida.")

        def ver_informacion_libreria():
            print("Información de la librería:")
            print("Dirección: 19 calle 4-35 zona 1, Guatemala, Guatemala")
            print("Número de teléfono: 89562743")
            print("Horario de atención: Lunes")
            print("Horario de atención: Lunes a Viernes de 6 am a 8 pm, Sábados de 6 am a 12 pm")

        def catalogo_libros():
            print("\nCatálogo de libros por sección:")
            print("1. Terror")
            print("2. Suspenso")
            print("3. Drama")
            print("4. Romance")
            seccion = input("Ingrese el número de la sección de su interés: ")
            if seccion == '1':
                print("Terror:")
                print("1. Drácula")
                print("2. Frankenstein")
                print("3. El Resplandor")
                print("4. Carrie")
                ver_informacion_libro()  # Añadido para permitir ver información de libros

            elif seccion == '2':
                print("Suspenso:")
                print("1. La paciente silenciosa")
                print("2. El psicoanalista")
                print("3. El espía que surgió del frío")
                print("4. La chica del tren")
                ver_informacion_libro()  # Añadido para permitir ver información de libros

            elif seccion == '3':
                print("Drama:")
                print("1. Quedará el amor")
                print("2. Terciopelo")
                print("3. Cometas en el cielo")
                print("4. Las hijas de la criada")
                ver_informacion_libro()  # Añadido para permitir ver información de libros

            elif seccion == '4':
                print("Romance:")
                print("1. Orgullo y prejuicio")
                print("2. Cumbres borrascosas")
                print("3. El cuaderno de Noah")
                print("4. La mujer del viajero en el tiempo")
                ver_informacion_libro()  # Añadido para permitir ver información de libros

            else:
                print("Sección no válida.")

    if respuesta == 'a':
        loginpersonal()
    elif respuesta == 'b':
        login_usuario()
    else:
        print("Opción no válida.")
