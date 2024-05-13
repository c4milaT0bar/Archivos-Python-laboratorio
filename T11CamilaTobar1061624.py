##Trabajo entre Camila Tobar, Gabriela Castro, María Sanchez

# inciso a

num = int(input("Ingrese un número mayor a 0: "))

if (num <= 0):
    print("Error: el número debe ser mayor a 0")

resultadoA = 0
for x in range (1, num +1):
    resultadoA += 1/x

print("Inciso A:", resultadoA)

# inciso b

num2 = int(input("Ingrese un número mayor a 0: "))

if (num2 <= 0):
    print("Error: el número debe ser mayor a 0")

num3 = int(input("Ingrese un número mayor a 0: "))

if (num3 <= 0):
    print("Error: el número debe ser mayor a 0")

resultadoB = 0
for w in range (1, num2 +1):
    for y in range (1, num3 +1):
        resultadoA += 1/w**y



print("Inciso B:", resultadoB)

# inciso c

num4 = int(input("Ingrese un número mayor a 0: "))

if (num4 <= 0):
    print("Error: el número debe ser mayor a 0")

a = int(input("Ingrese un número mayor a 0: "))

if (a <= 0):
    print("Error: el número debe ser mayor a 0")

n = int(input("Ingrese un número mayor a 0: "))

if (n <= 0):
    print("Error: el número debe ser mayor a 0")

k = 0
resultadoC = 0
for z in range (1, num4 +1):
    resultadoC += (z*k)*a*(n*-k)
    k += 1
print("Inciso C:", resultadoC)