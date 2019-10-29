#Ejercicio 6 Practica 3: Adrian Arias
print ("Este programa calcula el precio total de un producto con su IVA:\n")
nombre=str(input("Introduzca el nombre de su producto:\n"))
precio=float(input("Introduzca el precio del producto:\n"))
porcent=(precio*21)/100
iva=precio+porcent
print("Tu", nombre,"vale", precio,"euros y con el 21% de IVA se queda en", iva,"euros en total")
