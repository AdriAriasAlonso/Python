#Ejercicio 10 Practica 5: Adrián Arias
"""Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:"""

n1=int(input("Escribe la altura del triángulo:\n"))
for i in range(n1+1):
    for j in range(n1-i):
        print(" ", end="")
    for j in range(1,2*i):
        print("*", end="")
    print()
