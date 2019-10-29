#Ejercicio 1 Practica 4: Adrián Arias
print ("Este programa, dados 5 números,indica cual es el de mayor y el de menor valor. \n")
a=float(input("Introduce el primer número\n"))
b=float(input("Introduce el segundo número\n"))
c=float(input("Introduce el tercero número\n"))
d=float(input("Introduce el cuarto número\n"))
e=float(input("Introduce el quinto número\n"))

if a==b and a==c and a==d and a==e:
    print ("Todos los numeros son iguales.")
    
if a>b and a>c and a>d and a>e:
    print ( a,"es el mayor número\n")
elif b>a and b>c and b>d and b>e:
    print ( b,"es el mayor número\n")
elif c>a and c>b and c>d and c>e:
    print ( c,"es el mayor número\n")
elif d>a and d>b and d>c and d>e:
    print ( d,"es el mayor número\n")
elif e>a and e>b and e>c and e>d:
    print ( e,"es el mayor número\n")
    
if a<b and a<c and a<d and a<e:
    print ( a,"es el menor número")
elif b<a and b<c and b<d and b<e:
    print ( b,"es el menor número")
elif c<a and c<b and c<d and c<e:
    print ( c,"es el menor número")
elif d<a and d<b and d<c and d<e:
    print ( d,"es el menor número")
elif e<a and e<b and e<c and e<d:
    print ( e,"es el menor número")
