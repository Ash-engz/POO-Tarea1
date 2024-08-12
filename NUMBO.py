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

print("Instrucciones: el juego consiste en una tabla de 6x6 en la cual el primer jugador elige la casilla que desea. Los números siguientes se deben colocar en la misma fila o columna, y debe tener un camino ininterrumpido, Cuando un jugador se queda sin movimientos pierde son 36 casillas .")

def fila_columna(tablero, fila, columna, fila_anterior, columna_anterior):
    if fila == fila_anterior:
        paso = 1 if columna > columna_anterior else -1
        for c in range(columna_anterior + paso, columna, paso):
            if tablero[fila][c] != 0:
                return False
    elif columna == columna_anterior:
        paso = 1 if fila > fila_anterior else -1
        for f in range(fila_anterior + paso, fila, paso):
            if tablero[f][columna] != 0:
                return False
    return True

def asignar_valores(tablero, valor, turno, fila_anterior, columna_anterior):
    while True:
        try:
            casilla = int(input(f"Jugador {turno}, ingrese el número de casilla para colocar {valor}: ")) - 1
            if casilla < 0 or casilla >= 36:
                print("los datos no coinciden. Intente de nuevo.")
                continue

            fila = casilla // 6
            columna = casilla % 6

            if tablero[fila][columna] == 0:
                if fila_anterior is not None and columna_anterior is not None:
                    if fila != fila_anterior and columna != columna_anterior:
                        print("Movimiento inválido. Debe colocar casilla en misma fila o columna.")
                        continue
                    if not fila_columna(tablero, fila, columna, fila_anterior, columna_anterior):
                        print("Movimiento inválido. la fila o columna debe estar libre .")
                        continue

                tablero[fila][columna] = valor
                return fila, columna 
            else:
                print("La casilla ocupada. Intente de nuevo.")
        except ValueError:
            print("loa datos no coinciden")

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
