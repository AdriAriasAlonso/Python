#Ejercicio 9 Practica 5: Adrián Arias
"""Escribe un programa que pida la anchura y la altura de un rectángulo y lo dibuje de la siguiente manera:
Anchura del rectángulo: 5
Altura del rectángulo: 4"""

n1=int(input("Escribe un la anchura de un rectángulo\n"))
n2=int(input("Escribe un la altura del rectángulo\n"))
for i in range (n2): #Marca el numero de filas del rectangulo
    for j in range (n1): #Marca el numero de columnas del rectangulo y lo que hay que hacer dentro de cada punto de la columna
        if (j==0 or j==n1-1 or i==0 or i==n2-1):
            print ("*",end="")
        else:
            print (" ",end="")
    print()
