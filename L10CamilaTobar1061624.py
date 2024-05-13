print("Semana No. 10: EJERCICIO 1")

mesEntrada = int(input("Ingrese un número del 1 - 12: "))
mesSalida = ""

match mesEntrada:

    case 1: 
        mesSalida = "Enero"
    case 2: 
        mesSalida = "Febrero"
    case 3:
        mesSalida = "Marzo"
    case 4:
        mesSalida = "Abril"
    case 5:
        mesSalida = "Mayo"
    case 6: 
        mesSalida = "Junio"
    case 7: 
        mesSalida = "Julio"
    case 8:
        mesSalida = "Agosto"
    case 9:
        mesSalida = "Septiembre"
    case 10: 
        mesSalida = "Octubre"
    case 11: 
        mesSalida = "Noviembre"
    case 12:
        mesSalida = "Diciembre"
    
    case _:
        print("Error: El número debe estar contenido entre 1 y 12")

print(f"MES: {mesSalida}")

# Actividad 2

print("Semana No. 10: EJERCICIO 2")
      
a = int(input("Ingrese un primer número mayor a 0: "))
b = int(input("Ingrese un segundo número mayor a 0: "))
c = int(input("Ingrese un tercer número mayor a 0: "))

if(a<= 0 or b<= 0 or c<= 0):
    print("Error: Ingrese un primero número mayor a 0")

if(a>b):
    if(a>c):
        print("A es el mayor")
    else: 
        if(a==c):
            print("A es mayor que B, A es igual a C")
        else:
            print("A es mayor que B, A es menor que C")

elif (a == b):
    if (a > c): 
        print("A es mayor que B y mayor que C")
        