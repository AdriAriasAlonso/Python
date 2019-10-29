#Ejercicio 6 Practica 6: Adrián Arias
"""Escribe un programa que pida primero dos números (máximo y mínimo) y que
después te pida números intermedios. Para terminar de escribir números,
escribe un número que no esté comprendido entre los dos valores iniciales.
El programa termina escribiendo la lista de números."""

lista=[]

numero1=input("Escribe un numero minimo:\n")
numero2=input("Escribe un unmero maximo:\n")

lista.append(numero1)
lista.append(numero2)

numero=input("Escribe un numero intermedio:\n")

while numero>numero1 and numero<numero2:
    lista.append(numero)
    numero=input("Escribe otro numero intermedio:\n")

print (lista)
