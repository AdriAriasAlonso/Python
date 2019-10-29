#Ejercicio 5 Practica 4: Adrián Arias
print ("Este programa pide al usuario un importe en euros y dice si el\
cajero automático le puede dar dicho importe utilizando el mismo billete\
 y el más grande.\n" )
importe=float(input("Introduce una cantidad que quieres sacar del cajero:\n"))
if importe%500==0 and importe>0:
    x=importe/500
    print ("El cajero le devuelve", x,"billetes de 500 euros")
elif importe%200==0 and importe>0:
    x=importe/200
    print ("El cajero le devuelve", x,"billetes de 200 euros")
elif importe%100==0 and importe>0:
    x=importe/100
    print ("El cajero le devuelve", x,"billetes de 100 euros")
elif importe%50==0 and importe>0:
    x=importe/50
    print ("El cajero le devuelve", x,"billetes de 50 euros")
elif importe%20==0 and importe>0:
    x=importe/20
    print ("El cajero le devuelve", x,"billetes de 20 euros")
elif importe%10==0 and importe>0:
    x=importe/20
    print ("El cajero le devuelve", x,"billetes de 10 euros")
elif importe%5==0 and importe>0:
    x=importe/5
    print ("El cajero le devuelve", x,"billetes de 5 euros")
elif importe<0:
    print ("Cantidad incorrecta")
else:
    print ("El cajero no le puede devolver el importe utilizando el mismo billete y el mas grande a la vez")
