#Ejercicio 3 Practica 5: Adrian Arias
n1=int(input("Porfavor, introduzca un número:\n"))
n2=int(input("Porfavor, introduzca otro numero mayor que el primero:\n"))
suma = n1
for i in range ((n1+1),(n2+1)):
    suma = suma+i
print ("La suma desde", n1, "hasta", n2, "es", suma)
