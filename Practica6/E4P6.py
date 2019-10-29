#Ejercicio 4 Practica 6: Adrián Arias
"""Escribe un programa que te pida dos números, de manera que el segundo
sea mayor que el primero. El programa termina escribiendo los dos números
tal y como se pide."""

entrada=int(input("Escribe un número\n"))
entrada2=int(input("Escribe un número mayor que %d " % entrada))
               
while entrada2<=entrada:
    entrada2=int(input(" %d no es mayor que %d " % (entrada2,entrada)))
    
print("Los numeros que has escrito son", entrada, "y", entrada2)
