""" Diseñar el algoritmo correspondiente a un programa, que:

Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
Carga la tabla con valores numéricos enteros.
Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla. """

import random

lista=[]

while len(lista)<5:
    lista2=[]
    while len(lista2)<5:
        num= random.randint(0,100)
        lista2.append(num)
        print(str(num)+" ", end="")
    print()
    lista.append(lista2)
    

for fila in lista:
    print(lista.index(fila),"suma:",sum(fila))

col=[]
suma=[]

while len(suma)<5:
    for fila in lista:
        col.append(fila[len(suma)])
    suma.append(sum(col))

for sumas in suma:
    print(suma.index(sumas),"suma:",sumas)