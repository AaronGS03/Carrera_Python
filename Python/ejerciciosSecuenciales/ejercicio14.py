""" Dado un número de dos cifras, diseñe un algoritmo que permita 
obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32. """

import math

num= int(input("Num: "))

iNum= int(str(num)[1]+str(num)[0])

print(iNum)