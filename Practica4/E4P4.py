#Ejercicio 4 Practica 4: Adrián Arias
print("Este programa comprueba si el cuarto numero de una sucesion de 4 es un divisor de los tres primeros.\n")
a=int(input("Introduce el primer número\n"))
b=int(input("Introduce el segundo número\n"))
c=int(input("Introduce el tercero número\n"))
d=int(input("Introduce el cuarto número\n"))
if a%d==0 and b%d==0 and c%d==0:
    print("El cuarto número es divisor de los 3 primeros.")
else:
    print("El cuarto número no es divisor de los 3 primeros.")
