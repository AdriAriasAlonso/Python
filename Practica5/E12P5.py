#Ejercicio 12 Practica 5: Adrián Arias
"""Escribe un programa que pida un número y escriba si primo o no."""

n1=int(input("Escribe un número mayor que 1 y te diré si es primo o no:\n"))

patata = 0
for i in range (1,n1+1):
    if n1%i==0:
        patata = patata + 1
if patata == 2:
    print ("El número", n1, "es primo.")
else:
    print ("El número", n1, "no es primo.")
