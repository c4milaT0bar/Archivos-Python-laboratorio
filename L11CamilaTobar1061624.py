print("Semana No. 11: Ejercicio 1")

num = int(input("Ingrese un número mayor a 0: "))

if (num <= 0):
    print("Error: el número debe ser mayor a 0")

#Definición de variables

a = 0
b = 1
c = 0
i = 2
resultado = ""

if (num > 0):
    resultado = str(a)

    if (num > 1):
        resultado += ", " + str(b)

    while (i < num):
        c = a + b
        resultado += ", " +str(c)
        a = b
        b = c
        i = i + 1
    print(resultado)
else: 
    print(resultado)

print("Semana No. 11: Ejercicio 2")

num2 = int(input("Ingrese un número mayor a 0: "))

if (num2 <= 0):
    print("Error: el número debe ser mayor a 0")

# inciso a
resultadoA = 0
for x in range (1, num2 +1):
    resultadoA += 1/x

print("Inciso A:", resultadoA)