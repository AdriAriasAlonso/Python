#Ejercicio 7 Practica 3: Adrian Arias
print ("Este programa analiza una fecha:\n")
dia=int(input("Introduce el día:\n"))
mes=int(input("Introduce el mes:\n"))
año=int(input("Introduce el año:\n"))
if dia>31 or dia<1 or año<0:
    print("Fecha incorrecta.")
elif mes>12 or mes<1:
    print("Fecha incorrecta.")
elif mes==2 and dia>28:
    print("Fecha incorrecta.")
elif (mes==4 or mes==6 or mes==7 or mes==11) and dia>30:
    print("Fecha incorrecta.")
else:
    print("Fecha correcta:", dia,"/", mes,"/", año)
