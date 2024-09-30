libros = {}

class Main:
    
    libros = {
        "Drácula": {"autor": "Bram Stocker", "estado": "disponible", "Descripcion": "A la edad de 50 años, Bram Stoker dio a conocer Drácula (1897), una de las novelas de terror más importantes de la historia, que da a conocer a una de las figuras legendarias y míticas de la cultura popular, el vampiro."},
        "Frankenstein": {"autor": "Mary Shelley", "estado": "disponible" , "Descripcion": "Novelista, ensayista, dramaturga y biógrafa inglesa, Mary Shelley logró el reconocimiento mundial por una de las obras más famosas de la literatura occidental: Frankenstein o el Prometeo moderno (1818)"},
        "El Resplandor": {"autor": "Stephen King", "estado": "disponible", "Descripcion": "El resplandor (título original The Shining) es la tercera novela de terror del escritor estadounidense Stephen King, publicada en 1977."},
        "Carrie": {"autor": "Stephen King.", "estado": "disponible", "Descripcion": "4 min. Carrie, Los chicos del maíz y El resplandor son tres de las decenas de títulos que ha creado el autor estadounidense Stephen King."},
        "La paciente silenciosa": {"autor": "ALEX MICHAELIDES", "estado": "disponible", "Descripcion": "La paciente silenciosa es una novela de suspense psicológico de 2019 escrita por el autor británico-chipriota Alex Michaelides. "},
        "El psicoanalista": {"autor": "John Katzenbach", "estado": "disponible", "Descripcion": "El psicoanalista es una novela escrita por John Katzenbach publicada en 2002. Este thriller psicológico es la novela más exitosa del autor."},
        "El espía que surgió del frío": {"autor": "Le Carre, John", "estado": "disponible", "Descripcion": "El espía que surgió del frío es una novela escrita por el británico John le Carré y publicada en 1963. El espía que surgió del frío. de John le Carré."},
        "La chica del tren": {"autor": "PAULA HAWKINS", "estado": "disponible", "Descripcion": "Rachel (Emily Blunt) es una mujer devastada por su reciente divorcio que dedica cada mañana de camino a su trabajo a fantasear sobre la vida de una pareja aparentemente perfecta que vive en una casa por la que su tren pasa cada día."},
        "Quedará el amor": {"autor": "Kellen, Alice", "estado": "disponible", "Descripcion": "No están destinados a ser una ecuación perfecta, pero son jóvenes y el amor lo arrolla todo a su paso. Así que esta historia comienza como otras muchas: él y ella se enamoran. Hay primeras palabras, primeras miradas y primeros besos. Y luego la guerra, la nada."},
        "Terciopelo": {"autor": "Juan Rivera Arroyo", "estado": "disponible", "Descripcion": "Es Terciopelo, un ladrón por destino y por vocación. Dirigido por su olfato exquisito, Terciopelo va persiguiendo por las calles de la ciudad algo que es mucho más que objetos costos. Nada puede resistirse a la investigación escrupulosa de su nariz."},
        "Cometas en el cielo": {"autor": "Khaled Hosseini", "estado": "disponible", "Descripcion": "Superando con creces el rotundo éxito de Cometas en el cielo, la segunda novela de Khaled Hosseini saltó de inmediato al primer puesto en todos los países donde se ha publicado."},
        "Las hijas de la criada": {"autor": "Sonsoles Ónega", "estado": "disponible", "Descripcion": "La novela, titulada Las hijas de la criada, es obra de la escritora y periodista Sonsoles Ónega, cuya trayectoria como novelista ya le ha valido más de un reconocimiento en el mundo literario. Con Después del amor, obtuvo el prestigioso Premio de Novela Fernando Lara en 2017."},
        "Orgullo y prejuicio": {"autor": "Jane Austen", "estado": "disponible", "Descripcion": "El lado más atrevido de Jane Austen, la autora de Orgullo y Prejuicio (y cómo contrasta con la sociedad recatada que describía)"},
        "Cumbres borrascosas": {"autor": "Emily Brontë", "estado": "disponible", "Descripcion": "Cumbres borrascosas, una de las novelas inglesas más relevantes del siglo XIX, narra la épica historia de Catherine y Heathcliff. Situada en los sombríos y desolados páramos de Yorkshire, constituye una asombrosa visión metafísica del destino, la obsesión, la pasión y la venganza."},
        "El cuaderno de Noah": {"autor": "NICHOLAS SPARKS.", "estado": "disponible", "Descripcion": "LA HISTORIA DE AMOR MÇS VENDIDA DE LOS ÚLTIMOS VEINTE AÑOS. Descubre la inolvidable y desgarradora historia de amor ambientada en la Carolina del Norte post Segunda Guerra Mundial sobre una joven de la alta sociedad y el chico que una vez le robó el corazón."},
        "La mujer del viajero en el tiempo": {"autor": "Audrey Niffenegger", "estado": "disponible", "Descripcion": "Una conmovedora historia de amor que desafía el paso del tiempo. Una fascinante y muy poco convencional historia de amor: Henry es bibliotecario y padece una extraña disfunción genética que le hace viajar involuntariamente en el tiempo; Clare, su mujer, es artista."}
    }

########################################################################################################################

if __name__ == "__main__":
    print("Bienvenid@ a Librería Creaciones")
    respuesta = input("¿Quién desea ingresar? A. Personal autorizado ó B. Cliente: ").strip().lower()

    def loginpersonal():
        username = input("Ingrese nombre de usuario: ")
        password = input("Ingrese contraseña: ")
        acceso = False
        
        if username == "pablo" and password == "libreriacreaciones":
            acceso = True
            print("¡Bienvenido Pablo!")
        else:
            print("Nombre de usuario o contraseña incorrectos.")
        
        while acceso:
            print("\n¿Qué le gustaría hacer?")
            print("1. Agregar Libro")
            print("2. Eliminar Libro")
            print("3. Ver Estado de Libro")
            print("4. Prestar Libro")
            print("5. Devolver Libro")
            print("6. Consultar Libro")
            print("7. Ver Secciones")
            print("8. Salir")
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
            elif respuesta == '8':
                print("Saliendo del sistema de personal...")
                break
            else:
                print("Opción no válida.")
            
            regresar = input("¿Desea regresar al menú? (s/n): ").strip().lower()
            if regresar != 's':
                print("Saliendo del sistema de personal...")
                break

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
        nombre_completo = input("Ingrese su nombre completo: ")
        if nombre_completo != "Maria Zepeda":
            print("Nombre completo incorrecto.")
            return
        
        fecha_nacimiento = input("Ingrese su fecha de nacimiento (ejemplo: dd/mm/yyyy): ")
        if fecha_nacimiento != "04/08/2000":
            print("Fecha de nacimiento incorrecta.")
            return
        
        numero_carnet = input("Ingrese su número de carnet (ejemplo: 78965412): ")
        if numero_carnet != "11223344":
            print("Número de carnet incorrecto.")
            return
        while True:
            print("\n¿Qué le gustaría hacer?")
            print("1. Información de la librería")
            print("2. Catálogo de libros según sección/género")
            print("3. Ver estado de libro")
            print("4. Prestar libro")
            print("5. Devolver libro")
            print("6. Consultar libro")
            print("7. Ver información de libro")
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
            elif respuesta_usuario == '7':
                ver_informacion_libro()
            elif respuesta_usuario == '8':
                print("Saliendo del sistema de usuario...")
                break
            else:
                print("Opción no válida.")

            regresar = input("¿Desea regresar al menú? (s/n): ").strip().lower()
            if regresar != 's':
                print("Saliendo del sistema de usuario...")
                break

    
    def ver_informacion_libreria():
        print("Información de la librería:")
        print("Dirección: 19 calle 4-35 zona 1, Guatemala, Guatemala")
        print("Número de teléfono: 89562743")
        print("Horario de atención: Lunes a Viernes de 6 am a 8 pm, Sábados de 6 am a 12 pm")
    
    def catalogo_libros():
        print("\nCatálogo de libros por sección:")
        print("1. Terror")
        print("2. Suspenso")
        print("3. Drama")
        print("4. Romance")
        seccion = input("Ingrese el número de la sección de su interés: ")

        ###########################################################################################################################
        if seccion == '1':
            print("Terror:")
            print("")
            print("1. Drácula: ")
            print("Autor: autorBram Stocker" )
            print("Descripcion: A la edad de 50 años, Bram Stoker dio a conocer Drácula (1897), una de las novelas de terror más importantes de la historia, que da a conocer a una de las figuras legendarias y míticas de la cultura popular, el vampiro.")
            print("")
            print("2. Frankenstein")
            print("autor: Mary Shelley")
            print("Descripcion: Novelista, ensayista, dramaturga y biógrafa inglesa, Mary Shelley logró el reconocimiento mundial por una de las obras más famosas de la literatura occidental: Frankenstein o el Prometeo moderno (1818)")
            print("")
            print("3. El Resplandor")
            print("autor: Stephen King")
            print("Descripcion: El resplandor (título original The Shining) es la tercera novela de terror del escritor estadounidense Stephen King, publicada en 1977.")
            print("")
            print("4. Carrie")
            print("autor: Stephen King.")
            print("")

        elif seccion == '2':
            print("Suspenso: ")
            print("1. La paciente silenciosa")
            print("2. El psicoanalista")
            print("3. El espía que surgió del frío")
            print("4. La chica del tren")


        elif seccion == '3':
            print("Drama: ")
            print("1. Quedará el amor")
            print("2. Terciopelo")
            print("3. Cometas en el cielo")
            print("4. Las hijas de la criada")
            

        elif seccion == '4':
            print("Romance: ")
            print("1. Orgullo y prejuicior")
            print("2. Cumbres borrascosas")
            print("3. El cuaderno de Noah")
            print("4. La mujer del viajero en el tiempo")



        else:
            print("Sección no válida.")
    

    if respuesta == 'a':
        loginpersonal()
    elif respuesta == 'b':
        login_usuario()
    else:
        print("Opción no válida.")


        