#Ejercicio 2 Practica 4: Adrián Arias
print ("Este programa, dados 5 números, indica si estan en orden creciente,decreciente o desordenados\n")
a=float(input("Introduce el primer número\n"))
b=float(input("Introduce el segundo número\n"))
c=float(input("Introduce el tercero número\n"))
d=float(input("Introduce el cuarto número\n"))
e=float(input("Introduce el quinto número\n"))

if a<b<d<e:
    print("Los números estan ordenados en orden creciente")
elif a>b>c>d>e:
    print("Los números estan ordenados en orden decreciente")
else:
    print ("Los numeros no están ordenados.")
