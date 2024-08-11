#el numero 1 se puede poner donde sea, el 2 se debe ponwe en la misma fila o columna 

#un jugador pierde cuando no puede colocar un numero de manera legarl 
#tiene que ser un camino ininterrumpido 
tablero = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

def imprimir_tablero(tablero):
    print("\n")
    print("Este es el tablero actual:")
    print("\n")
    for fila in tablero:
        tablero_cadena = ""
        for celda in fila:
            tablero_cadena += str(celda) + " "
        print(tablero_cadena)
    print()

print ("instrucciones: el juego consiste en una tabla de 6x6 en la cual el primer jugador elige la casilla que desea, los numeros siguientes se deben colocar en la misma fila o columna, debe tener un camino ininterrumpido, cuando un jugador se queda sin movimientos pierde")

def asignar_valores(tablero, valor, turno, fila_anterior, columna_anterior):
    while True:
        try:
            casilla = int(input(f"Jugador {turno}, ingrese el número de casilla (1-36) para colocar {valor}: ")) - 1
            if casilla < 0 or casilla >= 36:
                print("Número de casilla fuera de rango. Intente de nuevo.")
                continue

            fila = casilla // 6
            columna = casilla % 6

            if tablero[fila][columna] == 0:
                if fila_anterior is not None and columna_anterior is not None:
                    if fila != fila_anterior and columna != columna_anterior:
                        print("Movimiento inválido. Debe estar en la misma fila o columna que el número anterior.")
                        continue

                tablero[fila][columna] = valor
                return fila, columna 
            else:
                print("La casilla ya está ocupada. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")

def juego():
    valor = 1
    turno = 1  
    fila_anterior = None
    columna_anterior = None

    imprimir_tablero(tablero)
    
    while valor <= 36:
        fila_anterior, columna_anterior = asignar_valores(tablero, valor, turno, fila_anterior, columna_anterior)
        imprimir_tablero(tablero)
        turno = 2 if turno == 1 else 1
        valor += 1

    print("¡El juego ha terminado!")

juego()