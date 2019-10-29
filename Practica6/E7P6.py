#Ejercicio 7 Practica 6: Adrián Arias
"""Escribe un programa que pida un número (límite) y luego te pida números
hasta que la suma de los números introducidos supere el límite inicial. El
programa termina escribiendo la lista de números."""

lista=[]

numerolimite=input("Escribe un numero límite:\n")

while suma<numerolimite:
    numero=input("Escribe otro numero:\n")
    lista.append(numero)
    for i in lista:
        suma=suma+i


print (lista)
