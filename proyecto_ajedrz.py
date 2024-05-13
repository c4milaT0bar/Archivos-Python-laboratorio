#aquí se crea un tablero con casillas vacias
def crear_tablero(filas, columnas):
    return [[0 for _ in range(columnas)] for _ in range(filas)]

#aqui agregamos las piezas, la posicion sera la coordenada dada y el color el asignado
def agregar_pieza(tablero, posicion, color):
    fila, columna = posicion
    tablero[fila][columna] = color

#aqui estamos definiendo todos los posible movimientos del caballo en el ajedrez
def obtener_movimientos_caballo(fila, columna, tablero):
    deltas = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
    movimientos = []
    for delta_fila, delta_columna in deltas:
        nueva_fila, nueva_columna = fila + delta_fila, columna + delta_columna
        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
            if tablero[nueva_fila][nueva_columna] == 0:
                movimientos.append((nueva_fila, nueva_columna))
    return movimientos

filas = 7
columnas = 7

tablero = crear_tablero(filas, columnas)

while True:
    tipo_pieza = input("Ingrese la posición de la pieza (por ejemplo, a1, e4, f8, etc.): ")
    if tipo_pieza.lower() == 'fin':
        break
    fila_pieza = int(tipo_pieza[1]) - 1
    columna_pieza = ord(tipo_pieza[0]) - ord('a')
    color_pieza = input("Ingrese el color de la pieza (blanco o negro): ")
    agregar_pieza(tablero, (fila_pieza, columna_pieza), color_pieza)

posicion_caballo = input("Ingrese la posición actual del caballo (por ejemplo, a1, e4, f8, etc.): ")
fila_caballo = int(posicion_caballo[1]) - 1
columna_caballo = ord(posicion_caballo[0]) - ord('a')

movimientos_caballo = obtener_movimientos_caballo(fila_caballo, columna_caballo, tablero)

print("Movimientos válidos del caballo:")
for movimiento in movimientos_caballo:
    print(f"({chr(movimiento[1] + ord('a'))}{movimiento[0] + 1})")


    