#Ejercicio 7 Practica 5: Adrián Arias
n1=int(input("Escribe la altura de un triángulo\n"))
for i in range (n1,0,-1):
    for j in range (i):
        print ("* ",end="")
    print()
