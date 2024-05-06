""" Se quiere realizar un programa que lea por teclado las 5 notas
 obtenidas por un alumno (comprendidas entre 0 y 10).
 A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor. """

import random

lista=[]

while len(lista)<5:
    lista.append(random.randint(1,10))
for num in lista:
    print(num)

print("Media:",sum(lista)/5)
lista.sort()
print("Alta:",lista[-1])
print("Menor:",lista[0])