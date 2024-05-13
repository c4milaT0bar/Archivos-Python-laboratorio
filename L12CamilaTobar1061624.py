print("Semana No. 12: Ejercicio 1")

print("Menú", 
"a. sumatoria", 
"b. Factorial", 
"c. Tablas de multiplicar",
"d. Número perfecto",
sep = "\n")

opcion = input("Ingrese su opción")

match opcion:
    case "a":
        n = int(input("Ingrese un número positivo: "))

        if n <= 0:
            print("Error: ingrese un número positivo")

        else:

            sumatoria = 0
            for contador in range (1, n+1):
                sumatoria += contador

                print("La sumatoria es de: " + str(sumatoria))

    case "b":
        num = int(input("Ingrese un número positivo: "))

        if num <= 0:
            print("Error: ingrese un número positivo")

        else:
            factorial = 1
            for x in range (1, num+1):
                factorial *= x
            if x == num: 
                print("El factorial es de: " + str(factorial))

    case "c":
        titulocol = "\t"

        for col in range (1, 11):
            titulocol += str(col) + "\t"

        print(titulocol)

        textofila = ""
        for fila in range (1, 11):
            textofila = str(fila) + "\t"

            for col in range (1, 11):
                textofila += str(fila * col) + "\t"
            
            print(textofila)

    case "d":
        num2 = int(input("Ingrese un número positivo: "))

        if num2 <= 0:
            print("Error: ingrese un número positivo")

        else:
            suma = 0
            for y in range (1, num2):
                if num2 % y == 0:
                    suma += y
            if suma == num2:
                print("El número es perfecto")
                
            else: 
                print("No es un número perfecto")
