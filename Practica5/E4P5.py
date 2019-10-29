#Ejercicio 4 Practica 5: Adrian Arias
n1=int(input("Porfavor, introduzca un número:\n"))
factorial=n1

for i in range (n1-1,1,-1):
    factorial=factorial*i
    
print ("El factorial de", n1, "es igual a", factorial)
