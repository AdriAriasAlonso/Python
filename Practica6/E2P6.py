#Ejercicio 2 Practica 6: Adrián Arias
"""Escribe un programa que te pida números y los guarde en una lista.
Para terminar de introducir número, simplemente escribe “Salir”.
El programa termina escribiendo la lista de números."""

numeros=[]
entrada=input("Escribe un número\n")

while entrada!="salir":
    numeros.append(int(entrada))
    entrada=input("Dame otro número o escribe salir para ver la lista de numeros\n")
print("Los numeros que has introducido son", numeros)
