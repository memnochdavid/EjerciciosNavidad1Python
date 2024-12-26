def tablero():
    return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]


def imprime_tablero(tablero):
    for fila in tablero:
        print(fila)


def es_valido(tablero, fila, columna, numero):
    # comprueba fila
    if numero in tablero[fila]:
        return False

    # comprueba columna
    for i in range(9):
        if tablero[i][columna] == numero:
            return False

    # subcuadrícula 3x3
    inicio_fila = (fila // 3) * 3
    inicio_columna = (columna // 3) * 3
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):
            if tablero[i][j] == numero:
                return False
    return True


def resuelve_sudoku(tablero):
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:  # vacío
                for numero in range(1, 10):  #  1 al 9
                    if es_valido(tablero, fila, columna, numero):
                        tablero[fila][columna] = numero  #se puede
                        if resuelve_sudoku(tablero):  # intenta resolver el siguiente paso
                            return True
                        tablero[fila][columna] = 0  # deshace el paso anterior
                return False  # si ningún número funciona, retornar falso (retroceso)

    return True  # gran éxito


# Ejecutar el programa
tablero_input = tablero()
print("Tablero inicial:")
imprime_tablero(tablero_input)

if resuelve_sudoku(tablero_input):
    print("\nTablero resuelto:")
    imprime_tablero(tablero_input)
