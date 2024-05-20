# Camila Tobar 1061624
# Proyecto No. 2 


# Definir todos los posibles movimientos de un caballo en un tablero
movimientos_caballo = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]



# Convertimos la coordenada en notación algebraica
def convertir_coordenada(coordenada):
    fila = int(coordenada[1]) - 1
    columna = ord(coordenada[0].lower()) - ord('a') 
        # El lower asegura que la letra de la coordenada siempre este en minusculas
            # La funcion lo que hace es convertir las columnas a letras para que sean variables válidas para el código

    return fila, columna
            # Devuelve la coordenada



# Función para verificar si una coordenada está dentro del tablero de 8x8
def coordenada_valida(coordenada):
    fila, columna = coordenada
    return 0 <= fila < 8 and 0 <= columna < 8



# Función para obtener los movimientos posibles del caballo
def obtener_movimientos_posibles(posicion_caballo, posiciones_piezas, color_caballo):
    movimientos_posibles = []
    # cadena vacia para almacenar los movimientos posibles

    fila_caballo, columna_caballo = convertir_coordenada(posicion_caballo)
    # convierte la coordenada de letra y numero a una tupla



    for x in movimientos_caballo:
        nueva_fila = fila_caballo + x[0]
        nueva_columna = columna_caballo + x[1]
        nueva_coordenada = (nueva_fila, nueva_columna)
        # "x" será cada posible movimiento del caballo y se le sumará esa coordenada a la posicion del caballo indicada por el usuario

        if coordenada_valida(nueva_coordenada):
            nueva_coordenada_letras = chr(nueva_columna + ord('a')) + str(nueva_fila + 1)

            if nueva_coordenada_letras not in posiciones_piezas:
                movimientos_posibles.append(f"{nueva_coordenada_letras}, está vacía")
                # verifica si la en la posicion posible del caballo hay alguna pieza, si no, almacena esa coordenada en la cadena vacia

            elif nueva_coordenada_letras in posiciones_piezas and posiciones_piezas[nueva_coordenada_letras]["color"] != color_caballo:
                if "tipo" in posiciones_piezas[nueva_coordenada_letras]:
                    movimientos_posibles.append(f"{nueva_coordenada_letras} con {posiciones_piezas[nueva_coordenada_letras]["tipo"]} {posiciones_piezas[nueva_coordenada_letras]["color"]}")
                # verifica que si sí hay una pieza en esa posicion, verifica que no se del color del caballo 
                #...para que sí se pueda mover a esa casilla, y almacena esa coordenada en la cadena vacia 

    return movimientos_posibles
        # devuele "movimientos posibles" la cual es la cadenaa vacia, pero ahora con las coordenas guardadas





# Se ingresa la posicion, color del caballo
posicion_caballo = input("Ingrese la posición del caballo (por ejemplo a1): ")
color_caballo = input("Ingrese el color del caballo (blanco o negro): ")

posiciones_piezas = {}
    #definimos este diccionario vacío para almacenarlo con cada pieza con su coordenada y color




# Se ingresa la posicion de la pieza y su color
while True:
    posicion_pieza = input("Ingrese la posición de una pieza, no escribas nada para terminar: ")
    if not posicion_pieza:
        break
    #el break indica que si el usuario no ingresó nada, ya terminó de ingresar los datos, entonces rompe el ciclo y pasa a lo siguiente
    color_pieza = input("Ingrese el color de la pieza (blanco o negro): ")

    tipo_pieza = input(f"Ingrese el tipo de pieza en {posicion_pieza} (peon, caballo, alfil, torre, dama, rey): ")

    posiciones_piezas[posicion_pieza] = {'tipo': tipo_pieza, 'color': color_pieza}
    # aqui guarda en el diccionario el color de cada pieza segun su coordenada



movimientos_posibles = obtener_movimientos_posibles(posicion_caballo, posiciones_piezas, color_caballo)
    # Se usa la funcion previamente planteada
print("Los movimientos del posibles para el caballo son: ")
for w in movimientos_posibles:
    print(w)
    # imprime los movimientos posibles para el caballo en lista
