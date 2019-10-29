#Ejercicio 1 Practica 4: Adrián Arias
print ("Este programa, dados 5 números,indica cual es el de mayor y el de menor valor. \n")
a=float(input("Introduce el primer número\n"))
b=float(input("Introduce el segundo número\n"))
c=float(input("Introduce el tercero número\n"))
d=float(input("Introduce el cuarto número\n"))
e=float(input("Introduce el quinto número\n"))

m = min([a,b,c,d,e])
l = max([a,b,c,d,e])

if (a == b and a == c and a == d and a == e):
    print('Todos son iguales')
else:
    print('El número mayor es %d' % m)
    print('El número menor es %d' % l)
