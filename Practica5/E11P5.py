#Ejercicio 11 Practica 5: Adrián Arias
"""Escribe un programa que pida un número e imprima todos sus divisores."""

n1=int(input("Escribe un número y te diré todos sus divisores:\n"))

print ("Los divisores de", n1, "son: ", end="")
for i in range (1,n1+1):
    if n1%i==0:
        print (i, " ", end="")
