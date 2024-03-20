""" Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se puede calcular? """

import math

a= float(input("a: "))

r2= math.sqrt(a)

r3= pow(a,1/3)

print("r2:",r2,"r3:",r3)