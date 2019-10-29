#Ejercicio 3 Practica 4: Adrián Arias
print ("Este programa puede calcular el area de un triangulo o de un cuadrado.\n")
a=input("Que area quieres calcular? Triangulo(T),o Cuadrado(C)\n")
if a!="C" and a!="T":
    print("Tecla incorrecta")
if a=="T":
    base=float(input("Dime la base de tu triangulo:\n"))
    altura=float(input("Dime la altura de tu triangulo:\n"))
    areaT=(base*altura)/2
    print("El area de tu triangulo es de:", areaT)
elif a=="C":
    base=float(input("Dime la base de tu cuadrado:\n"))
    altura=float(input("Dime la altura de tu cuadrado:\n"))
    areaC=(base*altura)/2
    print("El area de tu triangulo es de:", areaC)
