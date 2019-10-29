#Ejercicio 5 Practica 3: Adrian Arias
a=float(input("Porfavor, introduzca un numero de como máximo 3 dígitos:\n"))
if a>=1000 or a<=-1000:
    print("Incorrecto,", a,"es un número mayor de 3 cifras.")
else:
    print("Número correcto!")
