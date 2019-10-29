#Ejercicio 1 Practica 6: Adrián Arias
"""Escribe un programa que te pida palabras y las guarde en una lista.
Para terminar de introducir palabras, simplemente pulsa Enter.
El programa termina escribiendo la lista de palabras."""

palabras=[]
entrada=input("Escribe una palabra\n")

while entrada!="":
    palabras.append(entrada)
    entrada=input("Dame otra palabra\n")

print ("Las palabras que has introducido son: ", palabras)
