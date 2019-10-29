#Ejercicio 5 Practica 6: Adrián Arias
"""Escribe un programa que te pida números cada vez más grandes y que
se guarden en una lista. Para acabar de escribir los números, escribe
un número que no sea mayor que el anterior. El programa termina escribiendo
la lista de números:"""

lista=[]
entrada=int(input("Escribe un número\n"))
entrada2=int(input("Escribe un número\n"))

lista.append(entrada)
lista.append(entrada2)

while lista[-1]>lista[-2]:
    entrada=int(input("Escribe otro numero\n"))
    lista.append(int(entrada))

print ("Los numeros que has escrito son: ", end="" )
for i in range ((len(lista))-1):
    print (lista[i],"", end="")
