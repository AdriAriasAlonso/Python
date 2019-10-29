#Ejercicio 3 Practica 6: Adrián Arias
"""Escribe un programa que pida notas y los guarde en una lista.
Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10.
El programa termina escribiendo la lista de notas."""

notas=[]
entrada=float(input("Escribe un número\n"))

while entrada>=0 and entrada<=10:
    notas.append(float(entrada))
    entrada=float(input("Dame otra nota o escribe un numero mayor a 10 o menor a 0 para salir\n"))
print("Las notas que has introducido son", notas)
