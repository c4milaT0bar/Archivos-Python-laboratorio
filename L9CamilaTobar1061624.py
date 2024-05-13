print( "Ejercicio 1: operaciones artiméticas")

numero1 = int(input("Ingrese un número"))
numero2 = int(input("ingrese un segundo numero"))

divisionReal = numero1 / numero2
divisionEntera = numero1 // numero2
mod = numero1 % numero2

suma = numero1 + numero2
resta = numero1 - numero2
multiplicación = numero1 * numero2

print(numero1, "/", numero2, "=" , divisionReal)
print(numero1, "//", numero2, "=" , divisionEntera)
print(numero1, "%", numero2, "=" , mod)

print(numero1, "+", numero2, "=" , suma)
print(numero1, "-", numero2, "=" , resta)
print(numero1, "*", numero2, "=" , multiplicación)


print( "Ejercicio 2: operaciones booleanas")


igualdad = numero1 == numero2
diferentes = numero1 != numero2

mayorque = numero1 > numero2
menorque = numero1 < numero2

print(numero1, "==", numero2, "=" , igualdad)
print(numero1, "!=", numero2, "=" , diferentes)

print(numero1, ">", numero2, "=" , mayorque)
print(numero1, "<", numero2, "=" , menorque)

print( "Ejercicio 3:  jerarquía de operadores")

a = int(input("Ingrese un número"))
b = int(input("ingrese un segundo numero"))
c = int(input("Ingrese un tercer número"))

i = a*b+c
ii = a*b*c
x = b+c
iii = a / x
x = 3 * a 
y = 2 * b
z = x + y
iv = z / c**2

print(a, "*", b, "+", c, "=", i)
print(a, "*", "(", b, "*", c, ")", "=", ii)
print(a, "/", "(", b, "+", c, ")", "=", iii)
print("(3*", a,"+", "2*", b, ")", "/", c**2, "=", iv)




print( "Actividad 3")
print( "Ejercicio 1:  conversión")


metros1 = int(input("Ingrese Metros: "))
Km = metros1 /1000
print(F"Km = {Km}")

metros2 = int(input("Ingrese Metros: "))
yardas = metros2 // 0.9144
modYardas = metros2 % 0.9144
pies = modYardas // 0.333333

print("yardas: ", yardas, "pies", pies)





