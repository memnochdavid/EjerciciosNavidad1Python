def tablero(n):
    return [["0" for _ in range(n)] for _ in range(n)]

def imprime_tablero(tablero):
    for fila in tablero:
        print(fila)

def comprueba_casilla(x, y, tablero):
    n = len(tablero)

    # filas y columnas
    for i in range(n):
        if tablero[x][i] == "R" or tablero[i][y] == "R":
            return False

    # diagonales
    for i in range(n):
        for j in range(n):
            if abs(x - i) == abs(y - j) and tablero[i][j] == "R":
                return False

    return True

def resuelve_n_reinas(tablero, fila=0):
    n = len(tablero)

    if fila == n:
        return True

    for columna in range(n):
        if comprueba_casilla(fila, columna, tablero):
            tablero[fila][columna] = "R"

            if resuelve_n_reinas(tablero, fila + 1):
                return True

            tablero[fila][columna] = "0"

    return False

#ejecuta
n = 4
tab = tablero(n)

if resuelve_n_reinas(tab):
    imprime_tablero(tab)
else:
    print("No hay solución")