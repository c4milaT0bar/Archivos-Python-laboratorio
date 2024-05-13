

filas = 7
columnas = 7
    
  
matriz = [[0 for y in range(columnas)] for z in range(filas)]
letras = 'abcdefgh'
for columna in range(columnas):
    matriz[0][columna] = letras[columna]

for filas print(matriz)


