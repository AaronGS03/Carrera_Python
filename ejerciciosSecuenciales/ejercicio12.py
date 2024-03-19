""" Pide al usuario dos pares de números x1,y2 y x2,y2, que
representen dos puntos en el plano. Calcula y muestra la distancia entre ellos. """

import math

x1= float(input("x1: "))
y1= float(input("y1: "))
x2= float(input("x2: "))
y2= float(input("y2: "))

cat1= x2-x1
cat2= y2-y1
dist= math.sqrt(cat1**2+cat2**2)

print("La distancia entre ellos son:",dist)