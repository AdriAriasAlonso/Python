#Ejercicio 2 Practica 5: Adrian Arias
n1=int(input("Porfavor, introduzca un número\n"))
n2=int(input("Porfavor, introduzca otro numero\n"))
for i in range(n1,(n2+1)):
    if i%2==0:
        print ("El numero", i,"Es par")
    else:
        print ("El numero", i,"Es impar")
if n1>n2:
    for i in range(n2,(n1+1)):
        if i%2==0:
            print ("El numero", i,"Es par")
        else:
            print ("El numero", i,"Es impar")
        
